import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--train_image_dir', type=str, default='images/', help="image dir")
    parser.add_argument('--output_dir', type=str, default='output/', help="output dir")
    parser.add_argument('--rotation_range', type=int, default=90, help="rotation range")
    parser.add_argument('--width_shift_range', type=float, default=0.05, help="Horizontal displacement, the value is the proportion of width")
    parser.add_argument('--height_shift_range', type=float, default=0.05, help="Vertical displacement, the value is the proportion of width")
    parser.add_argument('--shear_range', type=float, default=0, help="Scope of perspective transformation")
    parser.add_argument('--zoom_range', type=float, default=0, help="Range of random scale")
    parser.add_argument('--horizontal_flip', type=bool, default=False, help="Horizontal flip")
    parser.add_argument('--vertical_flip', type=bool, default=False, help="Vertical flip")
    parser.add_argument('--fill_mode', type=str, default='nearest', help="How to fill in the newly created pixels")
    parser.add_argument('--img_width', type=int, default=1024, help="The width of image")
    parser.add_argument('--img_height', type=int, default=1024, help="The height of image")
    parser.add_argument('--gen_size', type=int, default=100, help="The number of generate images per image")
    parser.add_argument('--img_type', type=str, default='png', help="The type of image")

    flags, _ = parser.parse_known_args()
    if not os.path.exists(flags.output_dir):
        os.makedirs(flags.output_dir)

    return flags


flags = parse_args()

a = 1
