from datasets.utils import default_loader
import torchvision

torchvision.set_image_backend('accimage')

path = '/home/nfs/x.chang/Datasets/Kinetics400/train_frms/lunge/Ku56XQb3N40_000004_000014/00000000.jpg'
img = default_loader(path)
