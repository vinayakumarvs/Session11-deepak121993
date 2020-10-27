from PIL import Image
import os
import argparse


def convert(img_path: "Image Path"):
    """
    Function converts png images to jpg and saves it at the same location
    as that of the original image.
    Takes image path as input.
    """
    if not os.path.isfile(img_path):
        raise ValueError('No such image file exists.')
    elif img_path.split('.')[-1] != 'png':
        raise ValueError('Image is not a png file..')

    new_path = img_path.split("."+img_path.split('.')[-1])[0]+'.jpg'
    img = Image.open(img_path).convert('RGB')
    img.save(new_path, 'jpeg')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='png to jpg conversion')
    parser.add_argument('-ip', '--image_path', type=str, required=True, help='path of the source image')

    args = parser.parse_args()
    convert(args.image_path)