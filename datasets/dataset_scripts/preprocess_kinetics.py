#!/usr/bin/python
# remove whitespaces in the class directories
# Xiatian Zhu
# 2019
#
# Usage: ./download_kinetics_trim.py outdir/ csvfile.csv


# target_dir = '/home/SERILOCAL/x.chang/Datasets/Kinetics400/train/'
# target_dir = '/home/SERILOCAL/xiatian.zhu/test_rename/'


from os import listdir, rename
from os.path import isfile, join, isdir

def rmv_space(target_dir):
    for f in listdir(target_dir):
        if isdir(join(target_dir, f)):
            print('Before: {0}'.format(f))
            fa = f.replace(' ', '_')
            print('After: {0}'.format(fa))

            rename(join(target_dir, f), join(target_dir, fa))

            if isdir(join(target_dir, fa)) and not isfile(f):
                print('Rename done: {0}\n'.format(fa))


# target_dir = '/home/nfs/xiatian.zhu/datasets/Kinetics400/train/'
target_dir = '/home/SERILOCAL/x.chang/Datasets/Kinetics400/train/'
rmv_space(target_dir)

# target_dir = '/home/nfs/xiatian.zhu/datasets/Kinetics400/val/'
target_dir = '/home/SERILOCAL/x.chang/Datasets/Kinetics400/val/'
rmv_space(target_dir)

# target_dir = '/home/nfs/xiatian.zhu/datasets/Kinetics400/test/'
target_dir = '/home/SERILOCAL/x.chang/Datasets/Kinetics400/test/'
rmv_space(target_dir)


