from PIL import Image
import math


def to_back_white(img: Image):
    result_img = Image.new("L", img.size)

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel_color = img.getpixel((x, y))
            pixel_mean = (pixel_color[0] + pixel_color[1] + pixel_color[2]) / 3
            pixel_mean = math.floor(pixel_mean)
            result_img.putpixel((x, y), pixel_mean)

    return result_img
