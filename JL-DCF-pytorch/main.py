import argparse
import os
from dataset import get_loader
from solver import Solver
import time


def get_test_info(config):
    if config.sal_mode == 'Objectscale':
        image_root = '/content/Objectscale/'
        image_source = '/content/Objectscale/test.lst'
    elif config.sal_mode == 'Multiobjects':
        image_root = '/content/Multiobjects/'
        image_source = '/content/Multiobjects/test.lst'
    elif config.sal_mode == 'Illumination':
        image_root = '/content/Illumination/'
        image_source = '/content/Illumination/test.lst'
    elif config.sal_mode == 'Complexbackground':
        image_root = '/content/Complexbackground/'
        image_source = '/content/Complexbackground/test.lst'
    elif config.sal_mode == 'small':
        image_root = '/content/small/'
        image_source = '/content/small/test.lst'
    elif config.sal_mode == 'medium':
        image_root = '/content/medium/'
        image_source = '/content/medium/test.lst'
    elif config.sal_mode == 'large':
        image_root = '/content/large/'
        image_source = '/content/large/test.lst'
    elif config.sal_mode == 'Single':
        image_root = '/content/Single/'
        image_source = '/content/Single/test.lst'
    elif config.sal_mode == 'Multi':
        image_root = '/content/Multi/'
        image_source = '/content/Multi/test.lst'
    elif config.sal_mode == 'Low':
        image_root = '/content/Low/'
        image_source = '/content/Low/test.lst'
    elif config.sal_mode == 'High':
        image_root = '/content/High/'
        image_source = '/content/High/test.lst'
    elif config.sal_mode == 'simple':
        image_root = '/content/simple/'
        image_source = '/content/simple/test.lst'
    elif config.sal_mode == 'uncertain':
        image_root = '/content/uncertain/'
        image_source = '/content/uncertain/test.lst'
    elif config.sal_mode == 'complex':
        image_root = '/content/complex/'
        image_source = '/content/complex/test.lst'
    else:
        raise Exception('Invalid config.sal_mode')

    config.test_root = image_root
    config.test_list = image_source


def main(config):
    if config.mode == 'train':
        train_loader = get_loader(config)

        if not os.path.exists("%s/demo-%s" % (config.save_folder, time.strftime("%d"))):
            os.mkdir("%s/demo-%s" % (config.save_folder, time.strftime("%d")))
        config.save_folder = "%s/demo-%s" % (config.save_folder, time.strftime("%d"))
        train = Solver(train_loader, None, config)
        train.train()
    elif config.mode == 'test':
        get_test_info(config)
        test_loader = get_loader(config, mode='test')
        if not os.path.exists(config.test_folder): os.makedirs(config.test_folder)
        test = Solver(None, test_loader, config)
        test.test()
    else:
        raise IOError("illegal input!!!")


if __name__ == '__main__':
    resnet101_path = 'pretrained/resnet101-5d3b4d8f.pth'
    resnet50_path = 'pretrained/resnet50-19c8e357.pth'
    vgg16_path = 'pretrained/vgg16-397923af.pth'
    densenet161_path = 'pretrained/densenet161-8d451a50.pth'
    pretrained_path = {'resnet101': resnet101_path, 'resnet50': resnet50_path, 'vgg16': vgg16_path,
                       'densenet161': densenet161_path}

    parser = argparse.ArgumentParser()

    # Hyper-parameters
    parser.add_argument('--n_color', type=int, default=3)
    parser.add_argument('--lr', type=float, default=0.00005)  # Learning rate resnet:5e-5
    parser.add_argument('--wd', type=float, default=0.0005)  # Weight decay
    parser.add_argument('--momentum', type=float, default=0.99)
    parser.add_argument('--image_size', type=int, default=320)
    parser.add_argument('--cuda', type=bool, default=True)
    parser.add_argument('--device_id', type=str, default='cuda:0')

    # Training settings
    parser.add_argument('--arch', type=str, default='vgg'
                        , choices=['resnet', 'vgg','densenet'])  # resnet, vgg or densenet
    parser.add_argument('--pretrained_model', type=str, default=pretrained_path)  # pretrained backbone model
    parser.add_argument('--epoch', type=int, default=45)
    parser.add_argument('--batch_size', type=int, default=1)  # only support 1 now
    parser.add_argument('--num_thread', type=int, default=1)
    parser.add_argument('--load', type=str, default='')  # pretrained JL-DCF model
    parser.add_argument('--save_folder', type=str, default='checkpoints/')
    parser.add_argument('--epoch_save', type=int, default=5)
    parser.add_argument('--iter_size', type=int, default=10)
    parser.add_argument('--show_every', type=int, default=50)
    parser.add_argument('--network', type=str, default='vgg16'
                        , choices=['resnet50', 'resnet101', 'vgg16', 'densenet161'])  # Network Architecture

    # Train data
    parser.add_argument('--train_root', type=str, default='/content/RGBDcollection')
    parser.add_argument('--train_list', type=str, default='/content/RGBDcollection/train_ori.lst')

    # Testing settings
    parser.add_argument('--model', type=str, default='checkpoints/vgg16.pth')  # Snapshot
    parser.add_argument('--test_folder', type=str, default='test/vgg16/LFSD/')  # Test results saving folder
    parser.add_argument('--sal_mode', type=str, default='Objectscale',
                        choices=['Objectscale', 'Multiobjects', 'Illumination', 'Complexbackground', 'small', 'medium', 'large',
                                    'Single', 'Multi', 'Low', 'High', 'simple', 'uncertain', 'complex'])  # Test image dataset

    # Misc
    parser.add_argument('--mode', type=str, default='train', choices=['train', 'test'])
    config = parser.parse_args()

    if not os.path.exists(config.save_folder):
        os.mkdir(config.save_folder)

    get_test_info(config)

    main(config)
