# !usr/bin/env python
# coding:utf-8
'''
usage
python jp2a.py yourjpg_path output_path
'''
import Image

HEIGHT = 36
chars = "   ..',;:ciodxkO0KXNWMMM%%%%"


def pic2ascii(filename):
    output = ''
    image = Image.open(filename)
    size = convert_size(image)
    image = image.resize(size)
    image = image.convert('L')
    pixs = image.load()
    print pixs
    for y in range(size[1]):
        for x in range(size[0]):
            output += chars[pixs[x, y] / 10]
        output += '\n'
    print output
    with open(OUTPUT_PATH, 'wb') as w:
        w.write(output)


def convert_size(image):
    # Calculate the target picture size
    s_width = image.size[0]
    s_height = image.size[1]
    t_height = HEIGHT
    t_width = (t_height * s_width)/s_height
    t_width = int(t_width * 1.8)
    t_size = (t_width, t_height)
    return t_size

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    OUTPUT_PATH = sys.argv[2]
    pic2ascii(filename)
