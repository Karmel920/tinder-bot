from PIL import Image
import os

data_dir = 'data'
data_dir2 = 'data2'

for image_class in os.listdir(data_dir):
    for image in os.listdir(os.path.join(data_dir, image_class)):
        image_path = os.path.join(data_dir, image_class, image)
        im = Image.open(image_path).convert("RGB")
        im.save(os.path.join(data_dir2, image_class, image), "jpeg")
