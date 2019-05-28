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
    image_num = 0
    for f in listdir(target_dir):
        file_full_path = join(target_dir, f)
        if isfile(file_full_path):
            read_one_iamge(file_full_path)
            image_num += 1

    time_cost = timer.thetime() - timer.end
    print('Load images from disk: {0:.3f} sec'.format(time_cost))
    return time_cost, image_num


print('========== Image backend: {0}'.format(get_image_backend()))
target_dir = '/home/nfs/x.chang/Datasets/Kinetics400/train_frms/lunge/Ku56XQb3N40_000004_000014/'
time_cost_pil, image_num_pil = read_multi_images(target_dir)

torchvision.set_image_backend('accimage')
print('========== Image backend: {0}'.format(get_image_backend()))
time_cost_acc, image_num_acc = read_multi_images(target_dir)

print('Speedup by accimage: {time_cost_pil}/{time_cost_acc} ({image_num_pil/image_num_acc})')







