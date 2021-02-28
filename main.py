from datetime import datetime
import os
import sys
from PIL import Image
from cairosvg import svg2png
import argparse

def concatenate(
        icons: list, 
        path: str, 
        horizontal_icon_margin: int = 10, vertical_icon_margin: int = 10, 
        horizontal_image_margin: int = 20, vertical_image_margin: int = 20):
    number_of_icons = len(icons)
    image_width = 2 * horizontal_image_margin + (columns - 1) * horizontal_icon_margin + columns * icon_width
    image_height = 2 * vertical_image_margin + (rows - 1) * vertical_icon_margin + rows * icon_height
    result_image = Image.new('RGB', (image_width, image_height), (36, 41, 46))
    in_row_counter = 0
    in_column_counter = 0
    for icon in icons:
        ap_icon_x_pos = horizontal_image_margin + icon_width * in_row_counter + horizontal_icon_margin * in_row_counter
        ap_icon_y_pos = vertical_image_margin + icon_height * in_column_counter + vertical_icon_margin * in_column_counter
        with Image.open(path + str(icon)) as ap_icon:
            ap_icon = ap_icon.resize((icon_width, icon_height)) #TODO disable resizing -r
            result_image.paste(ap_icon, (ap_icon_x_pos, ap_icon_y_pos), ap_icon.convert('RGBA'))
        if(in_row_counter < columns - 1):
            in_row_counter += 1
        else:
            in_row_counter = 0
            in_column_counter += 1
    result_image.save("output.png", "PNG")

#def add_logo(logo_file: str, input_image)


'''
now_str = datetime.now().strftime("%d_%m_%Y_%H-%M")
report_file = open("report_file_" + str(now_str) + ".txt", "a")
report_file.write("Report file generated at " + now_str + "\n")
'''

parser = argparse.ArgumentParser(description="z4-xz.github.io")
parser.add_argument('-r', '--rows', help='Number of ROWS to draw in output file', default=15, type=int)
parser.add_argument('-c', '--columns', help='Number of COLUMNS to draw in output file', default=15, type=int)
parser.add_argument('-ih', '--iconheight', help='Single icon height in pixels', default=200, type=int)
parser.add_argument('-iw', '--iconwidth', help='Single icon width in pixels', default=200, type=int)
args_dict  = vars(parser.parse_args())

columns = abs(args_dict['columns'])
rows = abs(args_dict['rows'])
icon_width = abs(args_dict['iconwidth'])
icon_height = abs(args_dict['iconheight'])

input_folder_path = "./svg/"
output_folder_path = "./png/"
svgs = []
pngs = []
svgs += [file for file in (os.listdir(input_folder_path)) if(file.endswith(".svg"))]
#print(str(svgs))

for svg in svgs:
    try:
        png = svg.replace(".svg", ".png")
        svg2png(url = input_folder_path + str(svg), write_to = output_folder_path + str(png), output_width = icon_width, output_height = icon_height)
        pngs += [png]

    except:
        print("ERROR")

#print(pngs)
concatenate(pngs, output_folder_path) if len(pngs)<=rows*columns else print("Not enough rows or cols")

