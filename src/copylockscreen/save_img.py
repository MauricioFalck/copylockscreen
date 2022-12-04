from os import path
from shutil import copyfile
from . import DESTINATION_PATH, DBG_ENABLED
from copylockscreen.wallpaper import ImageType, WallpaperImage
from copylockscreen.logger import log


def save(wallpaper: WallpaperImage):
    """Saves the wallpaper to the destination directory defined

    Args:
        wallpaper (WallpaperImage): the wallpaper image to be copied
    """

    if (wallpaper.type == ImageType.LANDSCAPE):
        final_path = path.join(
            DESTINATION_PATH, 'Landscape', wallpaper.src_filename + '.' + wallpaper.extension)
    else:
        final_path = path.join(
            DESTINATION_PATH, 'Portrait', wallpaper.src_filename + '.' + wallpaper.extension)
    try:
        copyfile(wallpaper.src_path, final_path)
        log('File %s was saved' % final_path, 1, DBG_ENABLED)
    except Exception as e:
        log("Error saving image %s" % wallpaper.src_filename +
            '.' + wallpaper.extension, 1, DBG_ENABLED)
        log(e, 1, DBG_ENABLED)
