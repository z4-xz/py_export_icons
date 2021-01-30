from datetime import datetime
import os
import sys
from PIL import Image

def export(raw_files: list = [], type: str = ".png"):


def layout(horizontal: int, vertical: int, images: list =  [])->bool:
    list_length = len(images)


def concatenate(images: list):
    test=2
def list_files(type: str = "", dir: str = '.')-> list:
    _files = os.listdir(dir)
    listed_files = []
    for _file in _files:
        if(_file.endswith(type)):
            listed_files = listed_files + [_file]
    return listed_files
        
def report(files_list: list, exec_time: str = "00_00_0000_00-00"):
    test=2



now_str = datetime.now().strftime("%d_%m_%Y_%H-%M")
report_file = open("report_file_" + str(now_str) + ".txt", "a")
report_file.write("Report file generated at " + now_str + "\n")

print(list_files(".svg", "./icons"))

report_file.close()
