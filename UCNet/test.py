import torch
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np
import pdb, os, argparse
import time
# from scipy import misc
import imageio
from model.ResNet_models import Generator
from data import test_dataset

os.environ["CUDA_VISIBLE_DEVICES"] = '1'

parser = argparse.ArgumentParser()
parser.add_argument('--testsize', type=int, default=352, help='testing size')
parser.add_argument('--latent_dim', type=int, default=3, help='latent dim')
parser.add_argument('--feat_channel', type=int, default=32, help='reduced channel of saliency feat')
opt = parser.parse_args()

dataset_path = '/content/'
depth_path = '/content/'

generator = Generator(channel=opt.feat_channel, latent_dim=opt.latent_dim)
generator.load_state_dict(torch.load('/content/UCNet/models/Model_100_gen_trained.pth'))

generator.cuda()
generator.eval()

test_datasets = ['Objectscale', 'Multiobjects', 'Illumination', 'Complexbackground', 'small', 'medium', 'large', 'Single', 'Multi', 'Low', 'High'
                    'simple', 'uncertain', 'complex']
#test_datasets = ['STERE']

for dataset in test_datasets:
    save_path = '/content/pred_maps/' + dataset + '/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    image_root = dataset_path + dataset + '/RGB/'
    depth_root = dataset_path + dataset + '/depth/'
    test_loader = test_dataset(image_root, depth_root, opt.testsize)
    img_num = test_loader.size
    ti = 0
    for i in range(test_loader.size):
        print(i)
        image, depth, HH, WW, name = test_loader.load_data()
        image = image.cuda()
        depth = depth.cuda()
        torch.cuda.synchronize()
        time_s = time.time()
        generator_pred = generator.forward(image, depth, training=False)
        torch.cuda.synchronize()
        time_e = time.time()
        res = generator_pred
        res = F.upsample(res, size=[WW,HH], mode='bilinear', align_corners=False)
        res = res.sigmoid().data.cpu().numpy().squeeze()
        imageio.imwrite(save_path+name, res)
        t = time_e - time_s
        ti += t
    print('Speed: %f FPS' % (img_num / ti))