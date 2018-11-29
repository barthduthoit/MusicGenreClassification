import os
from PIL import Image
import argparse
from tqdm import tqdm


# original size 432*288
def resize(factor, dir_path):
    new_dir = "{}_{}".format(dir_path, factor)

    for root, _, files in tqdm(list(os.walk(dir_path)), desc='Looping genres'):
        genre = os.path.basename(root)
        genre_path = os.path.join(new_dir, genre)
        for f in tqdm([f for f in files if f.endswith('.png')], desc=genre):
            im = Image.open(os.path.join(root, f))
            im_resized = im.resize(tuple(int(ti / factor) for ti in im.size), Image.ANTIALIAS)
            im_resized.save(os.path.join(genre_path, f), "PNG")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='resize images by a factor')
    parser.add_argument('factor', type=int, help='factor by which the image size should be divided')
    parser.add_argument('dir_path', type=str,
                        choices=[os.path.join("data/", f) for f in os.listdir("data/") if "spectogram" in f],
                        help='path of the spectograms to resize')
    args = parser.parse_args()
    os.system("./init_genre_dir.sh {}_{}".format(args.dir_path, args.factor))
    resize(args.factor, args.dir_path)
