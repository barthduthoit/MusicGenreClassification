import os
from PIL import Image
import sys


# original size 432*288
def resize(factor, dir_path):
    new_dir = "{}_{}".format(dir_path, factor)+"/"
    dir_path = dir_path+"/"
    genres = [g for g in os.listdir(dir_path) if os.path.isdir(dir_path + g)]
    for genre in genres:

        PNGs = [f for f in os.listdir(dir_path + genre) if f.endswith(".png")]
        for f in PNGs:
            im = Image.open(dir_path + genre + "/" + f)
            im_resized = im.resize(tuple(int(ti/factor) for ti in im.size), Image.ANTIALIAS)
            im_resized.save(new_dir + genre + "/" + f, "PNG")


if __name__ == '__main__':
    print(sys.argv[1])
    factor = sys.argv[1]
    dir_path = sys.argv[2]
    new_dir = "{}_{}".format(dir_path, factor)
    genres = [g for g in os.listdir(dir_path) if os.path.isdir(dir_path + g)]
    print(dir_path)
    resize(int(factor), dir_path)
