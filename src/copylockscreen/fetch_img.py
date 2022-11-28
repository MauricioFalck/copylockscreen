from os import listdir, path
from . import DBG_ENABLED, PACKAGE_PATH
import copylockscreen.wallpaper as cpw
from copylockscreen.logger import log


def get_images():
    """
    Retrieves the valid wallpaper images from the Windows spotlight folder as a list of WallpaperImage

    Returns:
        list[WallpaperImage]: The list of the images

    """
    invalid_files = 0
    list_images = []
    # Get the list of files in the directory
    source_file_list = listdir(PACKAGE_PATH)
    # Checks each file
    log("**  Analyzing {} files found...".format(len(source_file_list)), 0, DBG_ENABLED)
    for file in source_file_list:
        # Try to convert the file to an image
        # UnidentifiedImageError raised if conversion is not possible
        try:
            img = cpw.WallpaperImage(path.join(PACKAGE_PATH, file))
            log("File {} is a valid image".format(file), 1, DBG_ENABLED)
            if not img.type == cpw.ImageType.OTHER:
                list_images.append(img)
            else:
                log("File {} is not a valid wallpaper image".format(
                    file), 1, DBG_ENABLED)
                invalid_files += 1
        except Exception:
            # File is not an image. Increase the invalid_files variable
            log("File {} is not a valid image".format(file), 1, DBG_ENABLED)
            invalid_files += 1
            continue
    log("**  Invalid files: {}".format(invalid_files), 0, DBG_ENABLED)
    log("**  Valid Wallpaper images: {}".format(len(list_images)), 0, DBG_ENABLED)
    return list_images
