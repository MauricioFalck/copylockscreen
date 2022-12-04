from os import path, listdir
import cv2

from . import DBG_ENABLED, DESTINATION_PATH, DUP_MODE, PACKAGE_PATH
from copylockscreen.wallpaper import ImageType, WallpaperImage
from copylockscreen.logger import log


def is_duplicated(wallpaper: WallpaperImage):
    """
    Checks if the wallpaper is already in the DESTINATION.
    If the DUP_MODE is FALSE, it only checks for file duplication using the name.
    If the DUP_MODE is TRUE, it compares the images in every pixel.

    Args:
        wallpaper(WallpaperImage): The wallpaper image to be compared

    Returns:
        bool: TRUE if duplicated, FALSE if not
    """

    if wallpaper.type == ImageType.LANDSCAPE:
        dest_path = path.join(
            DESTINATION_PATH, 'Landscape', wallpaper.src_filename + '.' + wallpaper.extension)
    else:
        dest_path = path.join(
            DESTINATION_PATH, 'Portrait', wallpaper.src_filename + '.' + wallpaper.extension)
    if path.exists(dest_path):
        log("File {} is duplicated".format(
            wallpaper.src_filename + '.' + wallpaper.extension), 1, DBG_ENABLED)
        return True
    if DUP_MODE == True:
        list_images = listdir(dest_path)
        src_image = cv2.imread(path.join(PACKAGE_PATH, wallpaper.src_filename))
        for file in list_images:
            dest_image = cv2.imread(path.join(dest_path, file))
            same_shape = False
            if src_image.shape == dest_image.shape:
                same_shape = True

            diff = cv2.subtract(src_image, dest_image)
            b, g, r = cv2.split(diff)
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0 and same_shape:
                log("File %s is duplicated" %
                    wallpaper.src_filename, 1, DBG_ENABLED)
                return True
    return False
