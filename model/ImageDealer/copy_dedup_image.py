# -*- coding:utf-8 -*-
# __author__='ligang'

import os
import sys
import time
import datetime
import exifread
import shutil
from collections import defaultdict
from PIL import Image
from PIL.ExifTags import TAGS
from imagededup.methods import PHash

sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/../../')

from common import common_image_dedup, common_file


def copy_deduped_image(src_path, dest_path):
    all_dirs, all_files = common_file.getAllSubs(src_path)

    image_list = []
    image_path = []
    for fpath in all_files:
        if not fpath.endswith(".jpg"):
            continue
        image_path.append(fpath)

    for idx, fpath in enumerate(image_path):
        print("%d/%d" % (idx, len(image_path)))
        is_similar = False
        image = Image.open(fpath)
        resized_image = common_image_dedup.get_thumbnail(image)

        for copied_image in image_list:
            similarity = common_image_dedup.image_similarity_vectors_via_numpy(copied_image, resized_image)
            if similarity > 0.95:
                is_similar = True
                break

        if is_similar:
            continue
        shutil.copy(fpath, dest_path)
        image_list.insert(0, resized_image)



if __name__ == '__main__':
    print("Hello", os.path.basename(__file__))
    src_path = "D:/code/data/droidbot_output/消灭星星全新版/u2"
    dest_path = "D:/code/data/droidbot_output/消灭星星全新版/deduped2"
    fpath1 = 'D:/code/data/droidbot_output/消灭星星全新版/deduped2/20230505_182715.jpg'
    fpath2 = 'D:/code/data/droidbot_output/消灭星星全新版/deduped2/20230505_182707.jpg'

    print("similarity:", common_image_dedup.calc_similarity(fpath1, fpath2))
    print("distance:", common_image_dedup.calc_hamming_distance(fpath1, fpath2))

    phasher = PHash()

    #encodings = phasher.encode_images(image_dir=src_path)

    #print(encodings)
    #duplicates = phasher.find_duplicates(encoding_map=encodings)
    #print(duplicates)

    img_hash1 = phasher.encode_image('D:/code/data/droidbot_output/消灭星星全新版/deduped2/20230505_184908.jpg')
    img_hash2 = phasher.encode_image('D:/code/data/droidbot_output/消灭星星全新版/deduped2/20230505_184908 - 副本.jpg')
    print(img_hash1)
    print(img_hash2)
    #print("distance:", phasher.hamming_distance(img_hash1, img_hash2))
    '''
    img_hash = phasher.encode_image('D:/code/data/droidbot_output/消灭星星全新版/deduped2/20230505_182620.jpg')
    for fname, hash_str in encodings.items():
        dis = phasher.hamming_distance(img_hash, hash_str)
        if dis <= 10:
            print(fname, dis)
    '''

    '''
    dedup = set()
    for fname, similars in duplicates.items():
        if fname in dedup:
            continue
        for i in similars:
            dedup.add(i)
        fpath = os.path.join(src_path, fname)
        shutil.copy(fpath, dest_path)
    '''
    #from imagededup.utils import plot_duplicates
    #print(plot_duplicates(image_dir=src_path,
    #                duplicate_map=duplicates,
    #                filename='D:/code/data/droidbot_output/消灭星星全新版/deduped2/1.jpg'))

