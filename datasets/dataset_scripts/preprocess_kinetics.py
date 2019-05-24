#!/usr/bin/python
# remove whitespaces in the class directories
# Xiatian Zhu
# 2019
#
# Usage: ./download_kinetics_trim.py outdir/ csvfile.csv


target_dir = '/home/SERILOCAL/x.chang/Datasets/Kinetics400/train/'

from os import listdir
from os.path import isfile, join

for f in listdir(target_dir):
    print(f)

# onlyfiles = [f for f in listdir(target_dir) if isfile(join(mypath, f))]

