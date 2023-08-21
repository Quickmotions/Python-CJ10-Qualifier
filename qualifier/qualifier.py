import cv2
import numpy
import math


def valid_input(image_size: tuple[int, int], tile_size: tuple[int, int], ordering: list[int]) -> bool:
    if image_size[0] % tile_size[0] != 0 or image_size[1] % tile_size[1] != 0:
        return False

    total_tiles = math.floor(image_size[0]/tile_size[0] * image_size[1]/tile_size[1])
    if total_tiles != len(ordering):
        return False

    for tile_num in range(total_tiles):
        if tile_num not in ordering:
            return False
    return True


def rearrange_tiles(image_path: str, tile_size: tuple[int, int], ordering: list[int], out_path: str) -> None:
    print(image_path)

    image = cv2.imread(image_path)
    height, width, channels = image.shape
    half_height = height // 2

    top_section = image[:half_height, :]
    bottom_section = image[half_height:, :]

    cv2.imshow('Top', top_section)
    cv2.imshow('Bottom', bottom_section)

    cv2.waitKey(0)
