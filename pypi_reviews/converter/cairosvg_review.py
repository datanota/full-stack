
# pip3 install CairoSVG
from utilities.common import Common
from cairosvg import svg2png


class CairoSVGReview(Common):
    def __init__(self):
        super().__init__()

    @staticmethod
    def convert():
        svg2png(
            url='./images/green.svg',
            write_to='./images/greensvg2png.png',
            output_width=400,
            output_height=400
        )


if __name__ == '__main__':
    CairoSVGReview().convert()

