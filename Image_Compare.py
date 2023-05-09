from PIL import Image
import numpy as np


def img_compare():
    im1 = Image.open(f'{image1}.jpg')
    im2 = Image.open(f'{image2}.jpg')

    data1 = np.array(im1)
    red1, green1, blue1 = data1.T
    data2 = np.array(im2)
    red2, green2, blue2 = data2.T

    black_areas = ((red1-red2) == 0) & ((blue1-blue2) == 0) & ((green1-green2) == 0)
    data1[:, :, :3] = (0, 0, 0)
    data1[:, :, :3][black_areas.T] = (255, 255, 255)
    # ref: https://stackoverflow.com/questions/3752476/python-pil-replace-a-single-rgba-color

    im3 = Image.fromarray(data1)
    im3.save('./result.jpg', format='JPEG', subsampling=0, quality=100)


while True:
    print('Compare 2 JPG images~~')
    image1 = input('Path of image 1: ')
    image2 = input('Path of image 2: ')
    img_compare()
    print('saved!\n')
