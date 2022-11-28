from os import path, environ, name
import argparse
from copylockscreen.logger import log


def init():
    global PACKAGE_PATH
    global DESTINATION_PATH
    global DBG_ENABLED
    global DUP_MODE

    # Validate OS
    if not name == 'nt':
        print('Invalid operating system. Must be executed on Windows')
        exit()
    args = parse_args()
    PACKAGE_PATH = path.join(environ.get('LOCALAPPDATA'),
                             'Packages\\Microsoft.Windows.'
                             'ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets')

    # Check if the package is installed
    if not path.exists(PACKAGE_PATH):
        print('Spotlight package not found')
        exit()

    # Parse arguments
    args = parse_args()

    if path.exists(args.path):
        DESTINATION_PATH = args.path
    else:
        print('Invalid destination path - using default', 1)
        DESTINATION_PATH = path.join(
            environ.get('USERPROFILE'), 'Pictures')

    DBG_ENABLED = args.debug
    DUP_MODE = args.full_check

    # Creates the initial Log message
    log('INIT',  0, DBG_ENABLED)

    log('Debug enabled: %s' % DBG_ENABLED, 0, DBG_ENABLED)
    log('Destination path: %s' % DESTINATION_PATH, 0, DBG_ENABLED)
    log('Duplication mode: %s' % DUP_MODE, 0, DBG_ENABLED)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Copy files from the Spotlight folder to the destination folder')

    parser.add_argument(
        '-p', '--path',
        type=str,
        help='destination path where the images are stored',
        default=path.join(environ.get('USERPROFILE'), 'Pictures'),
        required=False)
    parser.add_argument(
        '-d', '--debug',
        help='enable debug mode',
        action='store_true')
    parser.add_argument(
        '-fc', '--full-check',
        help='enable full duplication check',
        action='store_true')
    args = parser.parse_args()

    return args


init()
