from PIL import Image
from typing import Tuple, Union

class ImageUtils:
    @staticmethod
    def convert_transparent_to_color(
        img: Image.Image,
        new_color: Tuple[int] = (255, 255, 255),
        color_non_transparents: Union[Tuple[int], None] = None,
    ) -> Image.Image:
        """
        Converts the transparent pixels of image.

        For MNIST dataset, new color for the transparent pixels will be black, and new color for
        existing non transparent pixels will be white, to match the MNIST.

        Args:
            image: PIL.Image.Image - Image with transparent pixels.
            new_color: (int, int, int) - Color to paint. Defaults to white.
            color: Union[Tuple[int], None] - If specified, turns non transparent pixels to that color.

        Returns:
            image: PIL.Image.Image - Updated image.
        """
        if len(new_color) != 3:
            raise ValueError('Color tuple must have exactly 3 parameters (R, G, B)')

        pixels = img.load()

        for y in range(img.height):
            for x in range(img.width):
                r, g, b, a = pixels[x, y]
                if a == 0:
                    pixels[x, y] = new_color
                elif color_non_transparents:
                    pixels[x, y] = color_non_transparents

        return img
