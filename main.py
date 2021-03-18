import os
import json
from datetime import datetime
from PIL import Image
from cairosvg import svg2png
import argparse

settings = json.load(open('settings.json', 'r')) 
bg_color = settings["background"]
input_dir_path = "./svg/"

def concatenate(icons: list, path: str):
    """Paste images one by one into summary PNG file.

        Keyword arguments:

        icons: list -- list of image names e.g.  ["foo.png", "oof.png"] to be merged 

        path: str -- path to png images directory 
    """
    #Result image width and height calculation using settings values
    image_width = (2 * settings["hor_image_margin"]
                    + (settings["columns"] - 1) * settings["hor_icon_margin"]
                    + settings["columns"] * settings["icon_width"])
    image_height = (2 * settings["vert_image_margin"]
                    + (settings["rows"] - 1) * settings["vert_icon_margin"]
                    + settings["rows"] * settings["icon_height"])
    #Create new summary image
    result_image = Image.new('RGB', (image_width, image_height),
                            (bg_color["red"], bg_color["green"], bg_color["blue"]))
    #Number of elements in row/column
    in_row_counter = 0
    in_column_counter = 0
    for icon in icons:
        icon_x_pos = (settings["hor_image_margin"]
                    + settings["icon_width"] * in_row_counter
                    + settings["hor_icon_margin"] * in_row_counter)
        icon_y_pos = (settings["vert_image_margin"]
                    + settings["icon_height"] * in_column_counter
                    + settings["vert_icon_margin"] * in_column_counter)
        with Image.open(path + str(icon)) as ap_icon:
            ap_icon = ap_icon.resize((settings["icon_width"], settings["icon_height"]))
            result_image.paste(ap_icon, (icon_x_pos, icon_y_pos), ap_icon.convert("RGBA"))
        if(in_row_counter < settings["columns"] - 1):
            in_row_counter += 1
        else:
            in_row_counter = 0
            in_column_counter += 1
    result_image.save("output.png", "PNG")

def main():
    global settings
    parser = argparse.ArgumentParser(epilog = "### z4-xz.github.io ###")
    parser.add_argument("-r", "--rows", 
                        help = "Number of ROWS to draw in output file", 
                        default = settings["rows"], 
                        type = int)
    parser.add_argument("-c", "--columns", 
                        help = "Number of COLUMNS to draw in output file", 
                        default = settings["columns"], 
                        type = int)
    parser.add_argument("-ih", "--iconheight", 
                        help = "Single icon height in pixels", 
                        default = settings["icon_height"], 
                        type = int)
    parser.add_argument("-iw", "--iconwidth", 
                        help = "Single icon width in pixels", 
                        default = settings["icon_width"], 
                        type = int)
    args_dict  = vars(parser.parse_args())

    settings["columns"] = abs(args_dict["columns"])
    settings["rows"] = abs(args_dict["rows"])
    settings["icon_height"] = abs(args_dict["iconheight"])
    settings["icon_width"] = abs(args_dict["iconwidth"])
    output_dir_path = str(datetime.now().strftime("%d_%m_%Y_%H-%M-%S")) + "/"
    os.mkdir(output_dir_path)
    print("Directory {} created".format(output_dir_path))
    svgs = []
    pngs = []
    svgs += [file for file in (os.listdir(input_dir_path)) if(file.endswith(".svg"))]
    print("Listing...")
    for svg in svgs:
        try:
            png = svg.replace(".svg", ".png")
            svg2png(url = input_dir_path + str(svg), 
                    write_to = output_dir_path + str(png), 
                    output_width = settings["icon_width"], 
                    output_height = settings["icon_height"])
            pngs += [png]
        except Exception:
            print("Exception occured")

    if len(pngs) <= settings["rows"] * settings["columns"]:
        concatenate(pngs, output_dir_path)
    else:
        print("Not enough rows or cols")
    print("Done.")

if __name__ == '__main__':
    main()