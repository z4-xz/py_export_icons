from datetime import datetime
import os
import sys
from PIL import Image

def export_to_png(raw_files: list = [], type: str = ".png"):
    test=2

def concatenate(icons: list, path: str, icons_per_row: int = 5, icons_per_column: int = 2, horizontal_icon_margin: int = 10, vertical_icon_margin: int = 10, horizontal_image_margin: int = 20, vertical_image_margin: int = 20, icon_width: int = 300, icon_height: int = 300):
    image_width = 2 * horizontal_image_margin + (icons_per_row - 1) * horizontal_icon_margin + icons_per_row * icon_width
    image_height = 2 * vertical_image_margin + (icons_per_column - 1) * vertical_icon_margin + icons_per_column * icon_height
    result_image = Image.new('RGB', (image_width, image_height), (100, 100, 100))
    in_row_counter = 0
    in_column_counter = 0
    for icon in icons:
        if(in_row_counter < icons_per_row - 1):
            in_row_counter += 1
        else:
            in_row_counter = 0
            in_column_counter += 1
        ap_icon_x_pos = horizontal_image_margin + icon_width * in_row_counter + horizontal_icon_margin * in_row_counter
        ap_icon_y_pos = vertical_image_margin + icon_height * in_column_counter + vertical_icon_margin * in_column_counter
        ap_icon = Image.open(path + str(icon))
        ap_icon.thumbnail((icon_width, icon_height))
        result_image.paste(ap_icon, (ap_icon_x_pos, ap_icon_y_pos), ap_icon)
    result_image.save("output.png", "PNG")

#def add_logo(logo_file: str, input_image)

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
folder_path = "./icons/"

concatenate(list_files(".png", str(folder_path)), folder_path)

