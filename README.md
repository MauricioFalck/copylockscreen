# CopyLockScreen

This package reads the wallpaper images available from Windows Spotlight service and saves it to a specified folder in a jpg format.

## Windows Spotlight

The Windows Spotlight service is an application that defines the lock screen of Windows with pictures from the Bing Image gallery. Every image is provided in two layouts, landscape (1920x1080) and portrait (1080x1920).

## How to install

The module is only published to testpy till now. To install it:

> python -m pip install --index-url https://test.pypi.org/simple/ copylockscreen

## How to run

You can start the script by running it as a module:

> python -m copylockscreen \<OPTIONS>

### Execution options

**--debug, -d**: Execute the script with the debug mode on. This option displays more details in the log file, that is located at the %TEMP% directory with the name _log_cp_spotlight.txt_

**--path, -p**: Define the directory where the images will be saved. Under this directory the script will create two subdirectories, one for the landscape images and another for the portrait images. If a path is not provided, the script will use the Pictures default folder

**--full-check, -fc**: Checks if the images are duplicated by checking all the pixels of the image. Without this flag, the script will only check for duplication of filenames.

### Example

> python -m copylockscreen --full-check
