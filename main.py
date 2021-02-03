from datetime import datetime
import os
import sys
from PIL import Image
from cairosvg import svg2png

icons_per_row: int = 13
icons_per_column: int = 11
icon_width: int = 300
icon_height: int = 300

def concatenate(icons: list, path: str, horizontal_icon_margin: int = 10, vertical_icon_margin: int = 10, horizontal_image_margin: int = 20, vertical_image_margin: int = 20):
    image_width = 2 * horizontal_image_margin + (icons_per_row - 1) * horizontal_icon_margin + icons_per_row * icon_width
    image_height = 2 * vertical_image_margin + (icons_per_column - 1) * vertical_icon_margin + icons_per_column * icon_height
    result_image = Image.new('RGB', (image_width, image_height), (36, 41, 46))
    in_row_counter = 0
    in_column_counter = 0
    for icon in icons:
        ap_icon_x_pos = horizontal_image_margin + icon_width * in_row_counter + horizontal_icon_margin * in_row_counter
        ap_icon_y_pos = vertical_image_margin + icon_height * in_column_counter + vertical_icon_margin * in_column_counter
        with Image.open(path + str(icon)) as ap_icon:
            ap_icon = ap_icon.resize((icon_width, icon_height)) #TODO disable resizing -r
            result_image.paste(ap_icon, (ap_icon_x_pos, ap_icon_y_pos), ap_icon.convert('RGBA'))
        if(in_row_counter < icons_per_row - 1):
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

input_folder_path = "./svg/"
output_folder_path = "./png/"
svgs = []
pngs = []
svgs += [file for file in (os.listdir(input_folder_path)) if(file.endswith(".svg"))]
print(str(svgs))

for svg in svgs:
    try:
        png = svg.replace(".svg", ".png")
        svg2png(url = input_folder_path + str(svg), write_to = output_folder_path + str(png), output_width = icon_width, output_height = icon_height)
        pngs += [png]

    except:
        print("ERROR")

print(pngs)
concatenate(pngs, output_folder_path) if len(pngs)<=icons_per_column*icons_per_row else print("Not enough rows or cols")

