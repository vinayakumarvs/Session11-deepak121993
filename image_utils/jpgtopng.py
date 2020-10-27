from PIL import Image
import os
import argparse


def convert(img_path: "Image Path"):
    """
    Function converts jpg/jpeg images to png and saves it at the same location
    as that of the original image.
    Takes image path as input.
    """
    if not os.path.isfile(img_path):
        raise ValueError('No such image file exists.')
    elif img_path.split('.')[-1] not in ['jpg', 'jpeg']:
        raise ValueError('Image is not jpg/jpeg.')

    new_path = img_path.split("."+img_path.split('.')[-1])[0]+'.png'
    img = Image.open(img_path).convert('RGB')
    img.save(new_path, 'png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='jpg/jpeg to png conversion')
    parser.add_argument('-ip', '--image_path', type=str, required=True, help='path of the source image')

    args = parser.parse_args()
    convert(args.image_path)
