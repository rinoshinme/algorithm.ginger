"""
Peak Signal to Noise ratio, which is commonly used as a measure of
    reconstruction quality in image compression.
"""
import cv2
import numpy as np
import math
import os


def psnr(original, contrast):
    mse = np.mean((original - contrast) ** 2)
    if mse == 0:
        return 100

    pixel_max = 255.0
    psnr_value = 20 * math.log10(pixel_max / math.sqrt(mse))
    return psnr_value


def ssim():
    pass


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    original = cv2.imread(os.path.join(dir_path, 'original_image.png'))
    compressed = cv2.imread(os.path.join(dir_path, 'compressed_image.png'))

    print(psnr(original, compressed))


if __name__ == '__main__':
    main()


