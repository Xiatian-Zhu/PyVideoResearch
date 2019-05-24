#!/usr/bin/env python
# Training 3D ResNet50 from scratch on Kinetics
# using 4 GPUs
# original name: i3d8k
# model_best.txt:
#     loss_train 1.3742251321368457
#     loss_val 1.6312223851680756
#     top1train 66.3049965893588
#     top1val 64.01041666666667
#     top5train 85.77336289222374
#     top5val 83.69791666666667
import sys
import pdb
import traceback
sys.path.insert(0, '.')
from main import main
from bdb import BdbQuit
import os
os.nice(19)
name = __file__.split('/')[-1].split('.')[0]

args = [
    '--name', name,  # name is filename
    '--print-freq', '1',
    '--dataset', 'kinetics_mp4_x',
    '--arch', 'resnet50_3d',
    '--lr', '0.005',
    '--lr-decay-rate', '100',
    '--wrapper', 'default',
    '--criterion', 'softmax_criterion',
    '--epochs', '300',
    '--batch-size', '32',
    '--train-size', '0.2',
    '--weight-decay', '0.0000001',
    '--val-size', '0.1',
    '--cache-dir', '/home/SERILOCAL/xiatian.zhu/caches/Action_Recognition/',
    '--data', '/home/nfs/xiatian.zhu/datasets/Kinetics400/train/',
    '--valdata', '/home/nfs/xiatian.zhu/datasets/Kinetics400/val/',
    '--train-file', '/home/nfs/xiatian.zhu/datasets/Kinetics400/kinetics_train/kinetics_train.csv',
    '--val-file', '/home/nfs/xiatian.zhu/datasets/Kinetics400/kinetics_val/kinetics_val.csv',
    '--pretrained',
    '--nclass', '400',
    '--resume', '/home/SERILOCAL/xiatian.zhu/caches/Action_Recognition/' + name + '/model.pth.tar',
    '--workers', '16',
    '--metric', 'val_top1',
    '--disable-cudnn-benchmark',
]
sys.argv.extend(args)
try:
    main()
except BdbQuit:
    sys.exit(1)
except Exception:
    traceback.print_exc()
    print('')
    pdb.post_mortem()
    sys.exit(1)
