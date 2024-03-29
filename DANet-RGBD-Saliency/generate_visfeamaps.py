import numpy as np
import os
import time
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from PIL import Image
from torch.autograd import Variable
from torchvision import transforms
from config import test_data
from misc import check_mkdir, AvgMeter
from DANet import RGBD_sal

torch.manual_seed(2018)
torch.cuda.set_device(0)

ckpt_path = '/content/DANet-RGBD-Saliency-master/model_train_pth'
exp_name = ''


args = {
    'snapshot': '20500',
    'crf_refine':False,
    'save_results': True
}

img_transform = transforms.Compose([

    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

depth_transform = transforms.ToTensor()
target_transform = transforms.ToTensor()
to_pil = transforms.ToPILImage()

to_test = {'test':test_data}

def main():
    t0 = time.time()
    net = RGBD_sal().cuda()
    print ('load snapshot \'%s\' for testing' % args['snapshot'])
    net.load_state_dict(torch.load(os.path.join(ckpt_path, exp_name, args['snapshot'] + '.pth'),map_location={'cuda:1': 'cuda:1'}))
    net.eval()
    with torch.no_grad():

        for name, root in to_test.items():

            check_mkdir(os.path.join(ckpt_path, exp_name, '(%s) %s_%s' % (exp_name, name, args['snapshot'])))
            root1 = os.path.join(root,'RGB')
            img_list = [os.path.splitext(f)[0] for f in os.listdir(root1) if f.endswith('.jpg')]
            for idx, img_name in enumerate(img_list):
                print ('predicting for %s: %d / %d' % (name, idx + 1, len(img_list)))


                img1 = Image.open(os.path.join(root,'RGB',img_name + '.jpg')).convert('RGB')
                depth = Image.open(os.path.join(root,'depth',img_name + '.png')).convert('L')
                w,h = img1.size
                img1 = img1.resize([384,384])
                depth = depth.resize([384,384])
                img_var = Variable(img_transform(img1).unsqueeze(0), volatile=True).cuda()
                depth = Variable(depth_transform(depth).unsqueeze(0), volatile=True).cuda()
                outputs,outputs_fg,outputs_bg,attention1,attention2,attention3,attention4,attention5, c1, c2, c3, c4, c5 = net(img_var,depth)
                
                outputs = to_pil(outputs.data.squeeze(0).cpu())
                outputs_fg = to_pil(outputs_fg.data.squeeze(0).cpu())
                outputs_bg = to_pil(outputs_bg.data.squeeze(0).cpu())
                attention1 = to_pil(attention1.data.squeeze(0).cpu())
                attention2 = to_pil(attention2.data.squeeze(0).cpu())
                attention3 = to_pil(attention3.data.squeeze(0).cpu())
                attention4 = to_pil(attention4.data.squeeze(0).cpu())
                attention5 = to_pil(attention5.data.squeeze(0).cpu())

                outputs = outputs.resize((w, h), Image.BILINEAR)
                outputs_fg = outputs_fg.resize((w, h), Image.BILINEAR)
                outputs_bg = outputs_bg.resize((w, h), Image.BILINEAR)
                attention1 = attention1.resize((w, h), Image.BILINEAR)
                attention2 = attention2.resize((w, h), Image.BILINEAR)
                attention3 = attention3.resize((w, h), Image.BILINEAR)
                attention4 = attention4.resize((w, h), Image.BILINEAR)
                attention5 = attention5.resize((w, h), Image.BILINEAR)

                outputs = np.array(outputs)
                outputs_fg = np.array(outputs_fg)
                outputs_bg = np.array(outputs_bg)
                attention1 = np.array(attention1)
                attention2 = np.array(attention2)
                attention3 = np.array(attention3)
                attention4 = np.array(attention4)
                attention5 = np.array(attention5)

                # Afficher les cartes de features 
                # pour chaque bloc de l'encodeur
                E = [c1, c2, c3, c4, c5]
                enc = 0
                for c in E:
                  enc += 1
                  for i in range(16):
                      plt.subplot(2, 8, i + 1)
                      fm = c[0][i].cpu().detach().numpy()
                      plt.imshow(fm, cmap='viridis')
                      plt.axis("off")
                  plt.savefig('E'+str(enc)+'_feat_DANet.jpg', dpi=300)

                if args['save_results']:
                    Image.fromarray(outputs).save(os.path.join(ckpt_path, exp_name ,'(%s) %s_%s' % (
                            exp_name, name, args['snapshot'],), img_name + 'outputs' +'.png'))

                    Image.fromarray(outputs_fg).save(os.path.join(ckpt_path, exp_name ,'(%s) %s_%s' % (
                            exp_name, name, args['snapshot'],), img_name + 'outputs_fg' +'.png'))
                    
                    Image.fromarray(outputs_bg).save(os.path.join(ckpt_path, exp_name ,'(%s) %s_%s' % (
                            exp_name, name, args['snapshot'],), img_name + 'outputs_bg' +'.png'))

                    Image.fromarray(attention1).save(os.path.join(ckpt_path, exp_name ,'(%s) %s_%s' % (
                            exp_name, name, args['snapshot'],), img_name + 'attention1' +'.png'))

                    Image.fromarray(attention2).save(os.path.join(ckpt_path, exp_name ,'(%s) %s_%s' % (
                            exp_name, name, args['snapshot'],), img_name + 'attention2' +'.png'))

                    Image.fromarray(attention3).save(os.path.join(ckpt_path, exp_name ,'(%s) %s_%s' % (
                            exp_name, name, args['snapshot'],), img_name + 'attention3' +'.png'))

                    Image.fromarray(attention4).save(os.path.join(ckpt_path, exp_name ,'(%s) %s_%s' % (
                            exp_name, name, args['snapshot'],), img_name + 'attention4' +'.png'))

                    Image.fromarray(attention5).save(os.path.join(ckpt_path, exp_name ,'(%s) %s_%s' % (
                            exp_name, name, args['snapshot'],), img_name + 'attention5' +'.png'))

if __name__ == '__main__':
    main()