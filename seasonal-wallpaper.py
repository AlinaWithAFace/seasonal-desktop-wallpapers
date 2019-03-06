import datetime
import os
import ctypes


def get_full_path_of_image(image_filename):
    return os.path.dirname(os.path.realpath("assets/" + image_filename)) + "\\" + image_filename


def set_as_wallpaper(path):
    SPI = 20
    SPIF = 3
    return ctypes.windll.user32.SystemParametersInfoA(SPI, 0, path.encode("us-ascii"), SPIF)


li = [
    "bkg_01_january.jpg",
    "bkg_02_february.jpg",
    "bkg_03_march.jpg",
    "bkg_04_april.jpg",
    "bkg_05_may.jpg",
    "bkg_06_june.jpg",
    "bkg_07_july.jpg",
    "bkg_08_august.jpg",
    "bkg_09_september.jpg",
    "bkg_10_october.jpg",
    "bkg_11_november.jpg",
    "bkg_12_december.jpg"
]

full_path = get_full_path_of_image(li[datetime.datetime.now().month - 1])

set_as_wallpaper(full_path)
