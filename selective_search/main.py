# -*- coding: utf-8 -*-
from __future__ import (
    division,
    print_function,
)

import os 
import sys
import numpy as np
import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PIL import Image, ImageFilter
import selective_search


def main():

    # loading astronaut image
    #img = skimage.data.astronaut()
    path = os.path.abspath(os.path.dirname(__file__))
    image = Image.open(path+"/seg_test.jpg",mode="r")
    img = np.asarray(image)
    #plt.imshow(img)
    #plt.savefig("origin.jpg")

    plt.hist(img[:,:,0],100, facecolor="red", edgecolor="black", alpha=0.7)
    plt.savefig("origin_his_red.jpg")
    plt.clf

    plt.hist(img[:,:,1],100, facecolor="red", edgecolor="black", alpha=0.7)
    plt.savefig("origin_his_green.jpg")
    plt.clf

    plt.hist(img[:,:,2],100, facecolor="red", edgecolor="black", alpha=0.7)
    plt.savefig("origin_his_blue.jpg")
    plt.clf

    # perform selective search
    img_lbl, regions = selective_search.selective_search(
        img, scale=500, sigma=0.9, min_size=10)

    candidates = set()
    for r in regions:
        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            continue
        # excluding regions smaller than 2000 pixels
        if r['size'] < 2000:
            continue
        # distorted rects
        x, y, w, h = r['rect']
        if w / h > 1.2 or h / w > 1.2:
            continue
        candidates.add(r['rect'])

    # draw rectangles on the original image
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    ax.imshow(img)
    for x, y, w, h in candidates:
        print(x, y, w, h)
        rect = mpatches.Rectangle(
            (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
        ax.add_patch(rect)

    #plt.show()

if __name__ == "__main__":
    print(sys.version)
    print(sys.version_info)
    main()