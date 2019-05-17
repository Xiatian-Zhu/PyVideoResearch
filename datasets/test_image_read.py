""" Video loader for the Charades dataset """
import torch
import torchvision.transforms as transforms
import numpy as np
from glob import glob
from datasets.charades import Charades
from datasets.utils import default_loader
import datasets.video_transforms as videotransforms
from misc_utils.utils import AverageMeter, Timer



# path = '/home/SERILOCAL/xiatian.zhu/Data/test_video/ZZXQF-000002.jpg'
path = '/home/nfs/x.chang/Datasets/Charades/Charades/Charades_v1_rgb/ZZXQF/ZZXQF-000002.jpg'

for i in range(10):
    try:
        # ============ Temp ===================
        timer = Timer()
        img = default_loader(path)
        # ============ Temp ===================
        load_img_cost = timer.thetime() - timer.end
        timer.tic()
        print('Load image from disk: {0:.3f} sec'.format(load_img_cost))
    except Exception as e:
        print('failed to load image {}'.format(path))
        print(e)
        raise
