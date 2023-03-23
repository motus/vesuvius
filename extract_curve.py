#!/usr/bin/env python3

import glob
import json
import argparse

import numpy as np
import PIL.Image as Image


def _main():

    parser = argparse.ArgumentParser(description="Extract pixels along the curve.")
    parser.add_argument('curve', help='Path to the curve file (JSON).')
    parser.add_argument('path', help='Path to the input images.')

    args = parser.parse_args()

    with open(args.curve) as f:
        points = json.load(f)

    res = []
    for img_name in sorted(glob.glob(args.path)):
        img = Image.open(img_name)
        res.append(_curve_pixels(img, points))

    print(np.array(res))


def _curve_pixels(img, points):
    res = []
    if len(points) < 2:
        return res
    pt_prev = points[0]
    for pt in points[1:]:
        seg_len = np.linalg.norm(np.array(pt) - pt_prev)
        for coord_xy in np.linspace(pt_prev, pt, int(seg_len), dtype=int):
            res.append(img.get_at(coord_xy)[0] / 255.0)
        pt_prev = pt
    return res


if __name__ == "__main__":
    _main()
