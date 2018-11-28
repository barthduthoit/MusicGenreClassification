import os
from PIL import Image
import argparse
from tqdm import tqdm


# original size 432*288
def resize(factor, dir_path):
    new_dir = "{}_{}".format(dir_path, factor) + "/"
    dir_path = dir_path + "/"
    genres = [g for g in os.listdir(dir_path) if os.path.isdir(dir_path + g)]
    for genre in tqdm(genres):

        PNGs = [f for f in os.listdir(dir_path + genre) if f.endswith(".png")]
        for f in PNGs:
            im = Image.open(dir_path + genre + "/" + f)
            im_resized = im.resize(tuple(int(ti / factor) for ti in im.size), Image.ANTIALIAS)
            im_resized.save(new_dir + genre + "/" + f, "PNG")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='resize images by a factor')
    parser.add_argument('factor', type=int, help='factor by which the image size should be divided')
    parser.add_argument('dir_path', type=str, help='path of the spectograms to resize')
    args = parser.parse_args()
    os.system("./init_genre_dir.sh {}_{}".format(args.dir_path, args.factor))
    resize(args.factor, args.dir_path)
