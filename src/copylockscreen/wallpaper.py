from pathlib import Path
from PIL import Image, UnidentifiedImageError
from enum import Enum


class ImageType(Enum):
    LANDSCAPE = 1
    PORTRAIT = 2
    OTHER = 3


class WallpaperImage:
    """
    The object that represents a wallpaper image.

    Args:
        filename: the full path of te image to be parsed

    Throws:
        UnidentifiedImageError

    """

    def __init__(self, filename: str):
        self.src_path = filename
        # The filename of the file, without the path
        self.src_filename = Path(filename).name
        try:
            image = Image.open(filename)
            if image.height == 1080 and image.width == 1920:
                self.type = ImageType.LANDSCAPE
            elif image.height == 1920 and image.width == 1080:
                self.type = ImageType.PORTRAIT
            else:
                self.type = ImageType.OTHER
            self.extension = image.format.lower()

        except UnidentifiedImageError as e:
            raise e
