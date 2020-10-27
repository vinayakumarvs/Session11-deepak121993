import argparse
import jpgtopng
import pngtojpg
import imageresizer
import imagecropper

# print(f'loading __main__.py: __name__ = {__name__}')


if __name__ == '__main__':
    command_parser = argparse.ArgumentParser()

    subparsers = command_parser.add_subparsers(help='Choose a functionality.', dest='functionality')

    j2p_parser = subparsers.add_parser('j2p', help='jpg/jpeg to png conversion')
    j2p_parser.add_argument('-ip', '--image_path', type=str, required=True, help='path of the source image')

    p2j_parser = subparsers.add_parser('p2j', help='png to jpg conversion')
    p2j_parser.add_argument('-ip', '--image_path', type=str, required=True, help='path of the source image')

    res_p_parser = subparsers.add_parser('res_p', help='image resize using realtive percentage')
    res_p_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    res_p_parser.add_argument('-p', '--percentage', type=int, required=True, help='relative size percentage of the output images')

    res_w_parser = subparsers.add_parser('res_w', help='image resize to new width')
    res_w_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    res_w_parser.add_argument('-w', '--width', type=int, required=True, help='reqired width for the output images')

    res_h_parser = subparsers.add_parser('res_h', help='image resize to new height')
    res_h_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    res_h_parser.add_argument('-H', '--height', type=int, required=True, help='reqired height for the output images')

    crp_px_parser = subparsers.add_parser('crp_px', help='center crop images of required dimensions')
    crp_px_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    crp_px_parser.add_argument('-w', '--width', type=int, required=True, help='reqired width for the output images')
    crp_px_parser.add_argument('-H', '--height', type=int, required=True, help='reqired height for the output images')

    crp_p_parser = subparsers.add_parser('crp_p', help='center crop images of required relative percentage')
    crp_p_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    crp_p_parser.add_argument('-p', '--percentage', type=int, required=True, help='reqired relative percentage size for the output images')

    args = command_parser.parse_args()
    # print(args)

    if args.functionality == 'j2p':
        jpgtopng.convert(args.image_path)
    elif args.functionality == 'p2j':
        pngtojpg.convert(args.image_path)
    elif args.functionality == 'res_p':
        imageresizer.resize_percentage(args.folder_path, args.percentage)
    elif args.functionality == 'res_w':
        imageresizer.resize_width(args.folder_path, args.width)
    elif args.functionality == 'res_h':
        imageresizer.resize_height(args.folder_path, args.height)
    elif args.functionality == 'crp_px':
        imagecropper.center_crop_size(args.folder_path, (args.width, args.height))
    elif args.functionality == 'crp_p':
        imagecropper.center_crop_percentage(args.folder_path, args.percentage)
