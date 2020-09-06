import multiprocessing
from random import randint
from keras.preprocessing.image import ImageDataGenerator
from parse_args import parse_args


class Augmentation(object):
    def __init__(self, rotation_range, shear_range, zoom_range,
                 width_shift_range, height_shift_range,
                 horizontal_flip, vertical_flip,
                 img_width, img_height,
                 img_type, fill_mode, output_dir, gen_size):
        self.rotation_range = rotation_range
        self.shear_range = shear_range
        self.zoom_range = zoom_range
        self.width_shift_range = width_shift_range
        self.height_shift_range = height_shift_range
        self.horizontal_flip = horizontal_flip
        self.vertical_flip = vertical_flip
        self.img_width = img_width
        self.img_height = img_height
        self.img_type = img_type
        self.fill_mode = fill_mode
        self.output_dir = output_dir
        self.gen_size = gen_size
        self.generator = ImageDataGenerator(
            rotation_range=self.rotation_range,
            width_shift_range=self.width_shift_range,
            height_shift_range=self.height_shift_range,
            shear_range=self.shear_range,
            zoom_range=self.zoom_range,
            fill_mode=self.fill_mode,
            horizontal_flip=self.horizontal_flip,
            vertical_flip=self.vertical_flip,
            brightness_range=[0.0, 2.0]
        )

    def gen(self):
        generator = self.generator.flow_from_directory(
            directory=flags.train_image_dir,
            target_size=(self.img_height, self.img_width),
            color_mode='rgb',
            batch_size=32,
            save_to_dir=flags.output_dir,
            save_prefix=randint(0, 100000),
            save_format=flags.img_type)
        for i in range(self.gen_size):
            generator.next()


def gain():
    augmented = Augmentation(rotation_range=flags.rotation_range,
                             shear_range=flags.shear_range,
                             zoom_range=flags.zoom_range,
                             width_shift_range=flags.width_shift_range,
                             height_shift_range=flags.height_shift_range,
                             horizontal_flip=flags.horizontal_flip,
                             vertical_flip=flags.vertical_flip,
                             img_width=flags.img_width,
                             img_height=flags.img_height,
                             img_type=flags.img_type,
                             fill_mode=flags.fill_mode,
                             output_dir=flags.output_dir,
                             gen_size=flags.gen_size)

    augmented.gen()


if __name__ == "__main__":
    flags = parse_args()

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    for i in range(10):
        pool.apply_async(gain)

    pool.close()
    pool.join()
