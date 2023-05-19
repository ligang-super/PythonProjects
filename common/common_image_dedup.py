# -*- coding:utf-8 -*-
# __author__='LiGang'

import os
import sys
import cv2
import time
from PIL import Image
from numpy import average, linalg, dot
from imagededup.methods import PHash


def calc_equation(img1, img2, shape=(100, 100)):
    if img1.shape[0] == shape[0] and img1.shape[1] == shape[1]:
        pass
    else:
        img1 = cv2.resize(img1, shape)

    if img2.shape[0] == shape[0] and img2.shape[1] == shape[1]:
        pass
    else:
        img2 = cv2.resize(img2, shape)

    even_cnt = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            if img1[i][j].tolist() == img2[i][j].tolist():
                even_cnt += 1

    return float(even_cnt) / float(shape[0] * shape[1])


def get_thumbnail(image, size=(100, 100), greyscale=False):
    image = image.resize(size, Image.LANCZOS)

    if greyscale:
        image = image.convert('L')

    return image


def image_similarity_vectors_via_numpy(image1, image2):
    images = [image1, image2]
    vectors = []
    norms = []

    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    res = dot(a / a_norm, b / b_norm)
    return res


def calc_hamming_distance(fpath1, fpath2):
    tbegin = time.time()
    phasher = PHash()
    img_hash1 = phasher.encode_image(fpath1)
    img_hash2 = phasher.encode_image(fpath2)
    dis = phasher.hamming_distance(img_hash1, img_hash2)
    cost = time.time() - tbegin
    print("distance:", dis, "cost:", cost)
    return dis


def calc_image_similarity(image_path1, image_path2, func_type=1):
    print(image_path1, os.path.exists(image_path1))
    print(image_path2, os.path.exists(image_path2))
    if func_type == 1:
        # 直接计算相等
        imgnp1 = cv2.imread(image_path1)
        imgnp2 = cv2.imread(image_path2)
        print(type(imgnp1), type(imgnp2))
        return calc_equation(imgnp1, imgnp2)
    elif func_type == 2:
        # 直接计算余弦值
        image1 = Image.open(image_path1)
        image2 = Image.open(image_path2)
        print(type(image1), type(image2))
        cosin = image_similarity_vectors_via_numpy(image1, image2)
        return cosin
    elif func_type == 3:
        # resize后计算余弦值
        image1 = Image.open(image_path1)
        image2 = Image.open(image_path2)
        image1 = get_thumbnail(image1)
        image2 = get_thumbnail(image2)
        print(type(image1), type(image2))
        cosin = image_similarity_vectors_via_numpy(image1, image2)
        return cosin
    elif func_type == 4:
        # 计算汉明距离
        return calc_hamming_distance(image_path1, image_path2)



if __name__ == '__main__':
    print(__file__)

    dir_path = "D:/code/data/workspace/calc"
    jpg_path1 = os.path.join(dir_path, "20230505_164105.jpg")
    jpg_path2 = os.path.join(dir_path, "20230505_164317.jpg")

    desc = {
        1: "直接计算相等",
        2: "直接计算余弦值",
        3: "resize后计算余弦值",
        4: "计算汉明距离",
    }

    for i in range(1, 5):
        tbegin = time.time()
        r = calc_image_similarity(jpg_path1, jpg_path2, i)
        cost = (time.time() - tbegin) * 1000

        log_string = "%s: %s, cost: %.0fms" % (desc[i], r, cost)
        print(log_string)

