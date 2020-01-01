"""
This module contains the GUI's theme properties: the colors, icon paths and
fonts.

In the future, these properties could be modified if dark mode was enabled.
"""

import os

from PySide2.QtGui import QFont

from vidify import Platform, CURRENT_PLATFORM


# The vidify installation path's resources folder, having in account that this
# module is vidify.gui and that the resources folder is vidify.gui.res.
RESOURCES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              'res')


class Colors:
    """
    Contains the theme colors in hexadecimal. This will be useful in the
    future when dark mode is implemented.
    """

    bg = '#eff0eb'
    light = '#eff0eb'
    fg = '#282828'
    dark = '#282828'
    black = '#000000'
    lighterror = '#fc9086'
    darkerror = '#e33120'


def res_path(rel_path: str) -> str:
    """
    Converts a path relative to the vidify module to an absolute path in
    respect to the user's installation. That way, the module can be launched
    from directories other than the main one.
    """

    return os.path.join(RESOURCES_PATH, rel_path)


class Res:
    """
    Contains the paths for all the resources used in this program.
    """

    fonts = (res_path("Inter/Inter-Regular.otf"),
             res_path("Inter/Inter-Italic.otf"),
             res_path("Inter/Inter-Bold.otf"),
             res_path("Inter/Inter-BoldItalic.otf"),
             res_path("Inter/Inter-Medium.otf"),
             res_path("Inter/Inter-MediumItalic.otf"))

    default_video = res_path("default_video.mp4")

    icon = res_path("icon16x16.ico") \
        if CURRENT_PLATFORM == Platform.WINDOWS \
        else res_path("icon.svg")
    default_api_icon = res_path("api_icons/default.svg")
    cross = res_path("cross.svg")


class Fonts:
    """
    Contains the fonts for the different types of text.
    """

    smalltext = QFont("Inter", 10, QFont.Medium)
    text = QFont("Inter", 12, QFont.Medium)
    bigtext = QFont("Inter", 14, QFont.Medium)
    title = QFont("Inter", 24, QFont.Bold)
    title.setItalic(True)
    header = QFont("Inter", 20, QFont.Bold)
    header.setItalic(True)

    mediumbutton = QFont("Inter", 15, QFont.Bold)
    bigbutton = QFont("Inter", 18, QFont.Bold)
