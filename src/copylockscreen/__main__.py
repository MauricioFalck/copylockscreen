from . import DBG_ENABLED
from copylockscreen.logger import log
from copylockscreen.fetch_img import get_images
from copylockscreen.dup_check import is_duplicated
from copylockscreen.save_img import save

# For every valid file in the Spotlight folder, try to create a CPImage object
log('Starting to fetch images from Spotlight folder', 0, DBG_ENABLED)
wallpaper_images = get_images()
files_saved = 0
files_duplicated = 0
for wallpaper in wallpaper_images:
    log('Analyzing image: ' + wallpaper.src_filename, 1, DBG_ENABLED)

    if (is_duplicated(wallpaper)):
        files_duplicated += 1
        continue
    else:
        try:
            save(wallpaper)
            files_saved += 1

        except Exception as e:
            continue
log('** Total duplicated files: ' + str(files_duplicated), 0, DBG_ENABLED)
log('** Total files saved: ' + str(files_saved), 0, DBG_ENABLED)
