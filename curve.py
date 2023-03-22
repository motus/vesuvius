#!/usr/bin/env python3

import pickle
import argparse

import pygame


def _main():

    parser = argparse.ArgumentParser(description="Build or edit a curve.")
    parser.add_argument('image', help='Path to the input image file.')
    parser.add_argument('curve', help='Path to output curve file.')

    args = parser.parse_args()

    pygame.init()

    img = pygame.image.load(args.image)
    screen = pygame.display.set_mode(img.get_size())

    is_running = True
    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break

        screen.blit(img, (0, 0))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    _main()
