from datasets.utils import default_loader
import torchvision
from torchvision import get_image_backend
from misc_utils.utils import Timer

from os import listdir, rename
from os.path import isfile, join, isdir


#######################################################################
def read_one_iamge(path):
    # path = '/home/nfs/x.chang/Datasets/Kinetics400/train_frms/lunge/Ku56XQb3N40_000004_000014/00000000.jpg'
    return default_loader(path)


def read_multi_images(target_dir):
    timer = Timer()

    for f in listdir(target_dir):
        if isfile(join(target_dir, f)):
            read_one_iamge(f)

    time_cost = timer.thetime() - timer.end
    print('Load images from disk: {0:.3f} sec'.format(time_cost))


print('========== Image backend: {0}'.format(get_image_backend()))
target_dir = '/home/nfs/x.chang/Datasets/Kinetics400/train_frms/lunge/Ku56XQb3N40_000004_000014/'
read_multi_images(target_dir)

torchvision.set_image_backend('accimage')
print('========== Image backend: {0}'.format(get_image_backend()))
read_multi_images(target_dir)







