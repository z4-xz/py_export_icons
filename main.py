from datetime import datetime
import os
import sys
from PIL import Image

def export(raw_files: list = [], type: str = ".png"):
    test=2
def layout(horizontal: int, vertical: int, images: list = [])->bool:
    test=2
def concatenate(images: list, icons_per_row: int = 1, icons_per_column: int = 1, horizontal_icon_margin: int = 1, vertical_icon_margin: int = 1, horizontal_image_margin: int = 20, vertical_image_margin: int = 20, icon_width: int = 10, icon_height: int = 10):
    image_width = 2 * horizontal_image_margin + (icons_per_row - 1) * horizontal_icon_margin + icons_per_row * icon_width
    image_height = 2 * vertical_image_margin + (icons_per_column - 1) * vertical_icon_margin + icons_per_column * icon_height
    red_value, green_value, blue_value = 0, 0, 0
    icons = images
    for icon in icons:
        for i in range(icons_per_column):
            for j in range(icons_per_row):
                test=2
    
    print("image_height:" + str(image_height))


def list_files(type: str = "", dir: str = '.')-> list:
    _files = os.listdir(dir)
    listed_files = []
    for _file in _files:
        if(_file.endswith(type)):
            listed_files = listed_files + [_file]
    return listed_files
        
def report(listed_files: list, exec_time: str = "00_00_0000_00-00"):
    test=2

'''
now_str = datetime.now().strftime("%d_%m_%Y_%H-%M")
report_file = open("report_file_" + str(now_str) + ".txt", "a")
report_file.write("Report file generated at " + now_str + "\n")
'''
print(list_files(".svg", "./icons"))
concatenate(list_files(".svg", "./icons"))

