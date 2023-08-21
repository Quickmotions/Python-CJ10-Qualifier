import cv2
import numpy

def valid_input(image_size: tuple[int, int], tile_size: tuple[int, int], ordering: list[int]) -> bool:
    """
    Return True if the given input allows the rearrangement of the image, False otherwise.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once.
    """
    return True

def rearrange_tiles(image_path: str, tile_size: tuple[int, int], ordering: list[int], out_path: str) -> None:
    print(image_path)
    """
    Rearrange the image.

    The image is given in `image_path`. Split it into tiles of size `tile_size`, and rearrange them by `ordering`.
    The new image needs to be saved under `out_path`.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once. If these conditions do not hold, raise a ValueError with the message:
    "The tile size or ordering are not valid for the given image".
    """
    image = cv2.imread(image_path)
    height, width, channels = image.shape
    half_height = height // 2

    top_section = image[:half_height, :]
    bottom_section = image[half_height:, :]

    cv2.imshow('Top', top_section)
    cv2.imshow('Bottom', bottom_section)

    # cv2.waitKey(0)

