#!/usr/bin/env python3

import os
import json
import argparse

import pygame


def _main():

    parser = argparse.ArgumentParser(description="Build or edit a curve.")
    parser.add_argument('image', help='Path to the input image file.')
    parser.add_argument('curve', help='Path to output curve file (JSON).')

    args = parser.parse_args()

    pygame.init()

    img = pygame.image.load(args.image)
    screen = pygame.display.set_mode(img.get_size())  # pygame.RESIZABLE

    points = []
    if os.path.exists(args.curve):
        with open(args.curve, 'r') as f:
            points = json.load(f)

    is_running = True
    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    _update(points, event.pos)

        screen.blit(img, (0, 0))
        _curve(screen, points)

        pygame.display.flip()

    print(points)
    with open(args.curve, 'w') as f:
        json.dump(points, f)

    pygame.quit()


_COLOR = pygame.Color(255, 0, 0, a=127)
_PT_RADIUS = 5
_LINE_WIDTH = 2


def _update(points, pt_new):
    for i, pt in enumerate(points):
        if (pt[0] - pt_new[0]) ** 2 + (pt[1] - pt_new[1]) ** 2 < _PT_RADIUS:
            del points[i]
            return
    points.append(pt_new)
    return points


def _curve(screen, points):
    pt_prev = None
    for pt in points:
        pygame.draw.circle(screen, _COLOR, pt, _PT_RADIUS, _LINE_WIDTH)
        if pt_prev:
            pygame.draw.line(screen, _COLOR, pt_prev, pt, _LINE_WIDTH)
        pt_prev = pt


if __name__ == "__main__":
    _main()
