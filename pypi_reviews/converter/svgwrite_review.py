
# pip3 install Pillow svgwrite
from utilities.common import Common
import argparse
from PIL import Image
import svgwrite


class SVGwriteReview(Common):
    def __init__(self):
        super().__init__()
        self.img_nm = self.parse_arguments().img_nm
        self.input_png = f'./images/{self.img_nm}.png'
        self.output_svg = f'./images/{self.img_nm}.svg'

    def convert(self):
        img = Image.open(self.input_png)
        img = img.convert("RGBA")
        # Create a new SVG drawing
        dwg = svgwrite.Drawing(self.output_svg, profile='tiny')
        # Process each pixel
        for y in range(img.height):
            for x in range(img.width):
                pixel = img.getpixel((x, y))
                # Check if the pixel is not transparent
                if pixel[3] > 0:
                    # Convert the RGBA to hex format
                    fill = svgwrite.rgb(pixel[0], pixel[1], pixel[2], '%')
                    # Draw a rectangle (as a pixel) on the SVG
                    dwg.add(dwg.rect(insert=(x, y), size=(1, 1), fill=fill))
        dwg.save()

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument('-img_nm', default='img_nm')
        return parser.parse_args()


if __name__ == '__main__':
    SVGwriteReview().convert()

