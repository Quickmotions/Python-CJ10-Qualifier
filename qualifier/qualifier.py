import cv2
import numpy as np


def valid_input(image_size: tuple[int, int], tile_size: tuple[int, int], ordering: list[int]) -> bool:
    # image divides into tiles neatly
    if image_size[0] % tile_size[0] != 0 or image_size[1] % tile_size[1] != 0:
        return False

    # ordering is the correct length for total tiles
    total_tiles = int(image_size[0] / tile_size[0] * image_size[1] / tile_size[1])
    if total_tiles != len(ordering):
        return False

    # no duplicates in ordering
    for tile_num in range(total_tiles):
        if tile_num not in ordering:
            return False

    return True


def rearrange_tiles(image_path: str, tile_size: tuple[int, int], ordering: list[int], out_path: str) -> None:
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)  # Read image with alpha channel
    full_height, full_width, num_channels = image.shape

    # input validation
    if not valid_input((int(full_width), int(full_height)), tile_size, ordering):
        raise ValueError("The tile size or ordering are not valid for the given image")

    # calculate tile properties
    column_tile_amount = int(full_width / tile_size[0])
    row_tile_amount = int(full_height / tile_size[1])
    tile_width = int(full_width / column_tile_amount)
    tile_height = int(full_height / row_tile_amount)

    scrambled_tiles = []
    for ih in range(row_tile_amount):
        for iw in range(column_tile_amount):
            # calculate the coordinates and dimensions of the current tile
            x = tile_size[0] * iw
            y = tile_size[1] * ih
            h = tile_size[1]
            w = tile_size[0]

            # save tile positions into tile array
            img = image[y:y + h, x:x + w]
            scrambled_tiles.append(img)

    # reorder tile positions by ordering list
    unscrambled_tiles = []
    for array_position in ordering:
        unscrambled_tiles.append(scrambled_tiles[array_position])

    canvas = np.zeros((full_height, full_width, num_channels), dtype=np.uint8)

    # iterate through each tile and place it on the canvas row by row
    for row in range(row_tile_amount):
        for col in range(column_tile_amount):
            tile_index = row * column_tile_amount + col
            if tile_index < len(unscrambled_tiles):
                tile = unscrambled_tiles[tile_index]
                x_offset = col * tile_width
                y_offset = row * tile_height
                canvas[y_offset:y_offset + tile_height, x_offset:x_offset + tile_width] = tile

    cv2.imwrite(out_path, canvas)
