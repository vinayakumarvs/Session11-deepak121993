import os
import glob
from PIL import Image
import argparse

def center_crop_size(folder_path: "Folder Path", size: "Size Tuple (W, H)"):
    """
    Function center square/rectangle crops bulk images by user-determined pixels.
    Takes the folder path and size as input.
    The images that are not cropped due to exceeding size are printed.
    """
    if not os.path.isdir(folder_path):
        raise ValueError('No such folder exists.')
    img_paths = []
    for ext in ('*.jpeg', '*.png', '*.jpg'):
        img_paths.extend(glob.glob(os.path.join(folder_path, ext)))

    dst_folder_path = os.path.join(folder_path, 'cropeed_images_size_'+str(size))
    os.mkdir(dst_folder_path)

    skipped_images = []
    for img_path in img_paths:
        head, tail = os.path.split(img_path)
        img = Image.open(img_path)
        img_size = img.size
        if img_size[0]>=size[0] and img_size[1]>=size[1]:
            out = img.crop(((img_size[0] - size[0]) // 2, 
                (img_size[1] - size[1]) // 2,
                (img_size[0] + size[0]) // 2,
                (img_size[1] + size[1]) // 2))
            out.save(os.path.join(dst_folder_path, tail))
        else:
            del img
            skipped_images.append(tail)

    if len(skipped_images) > 0:
        print("The following images couldn't be processed:")
        print("\n".join(skipped_images))


def center_crop_percentage(folder_path: "Folder Path", crop_percentage: "Percentage(int)"):
    """
    Function center square/rectangle crops bulk images by user-determined percentage.
    Takes the folder path and percentage as input.
    The images that are not cropped due to exceeding size are printed.
    """
    if not os.path.isdir(folder_path):
        raise ValueError('No such folder exists.')
    img_paths = []
    for ext in ('*.jpeg', '*.png', '*.jpg'):
        img_paths.extend(glob.glob(os.path.join(folder_path, ext)))

    dst_folder_path = os.path.join(folder_path, 'cropeed_images_percentage_'+str(crop_percentage))
    os.mkdir(dst_folder_path)

    skipped_images = []
    for img_path in img_paths:
        head, tail = os.path.split(img_path)
        img = Image.open(img_path)
        img_size = img.size
        ratio = crop_percentage / 100
        size = (int(ratio*img_size[0]), int(ratio*img_size[1]))
        if img_size[0]>=size[0] and img_size[1]>=size[1]:
            out = img.crop(((img_size[0] - size[0]) // 2, 
                (img_size[1] - size[1]) // 2,
                (img_size[0] + size[0]) // 2,
                (img_size[1] + size[1]) // 2))
            out.save(os.path.join(dst_folder_path, tail))
        else:
            del img
            skipped_images.append(tail)

    if len(skipped_images) > 0:
        print("The following images couldn't be processed:")
        print("\n".join(skipped_images))


if __name__ == '__main__':
    command_parser = argparse.ArgumentParser()

    subparsers = command_parser.add_subparsers(help='Choose a functionality.', dest='functionality')

    crp_px_parser = subparsers.add_parser('crp_px', help='center crop images of required dimensions')
    crp_px_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    crp_px_parser.add_argument('-w', '--width', type=int, required=True, help='reqired width for the output images')
    crp_px_parser.add_argument('-H', '--height', type=int, required=True, help='reqired height for the output images')

    crp_p_parser = subparsers.add_parser('crp_p', help='center crop images of required relative percentage')
    crp_p_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    crp_p_parser.add_argument('-p', '--percentage', type=int, required=True, help='reqired relative percentage size for the output images')

    args = command_parser.parse_args()
    if args.functionality == 'crp_px':
        center_crop_size(args.folder_path, (args.width, args.height))
    elif args.functionality == 'crp_p':
        center_crop_percentage(args.folder_path, args.percentage)