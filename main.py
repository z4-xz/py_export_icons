from datetime import datetime
import os
import cairosvg

now_str = datetime.now().strftime("%d_%m_%Y_%H;%M")
report_file = open("report_file_" + str(now_str) + ".txt", "a")
report_file.write("Report file generated at " + now_str + "\n")
files = os.listdir('./icons')
for file in files:
    if(file.endswith(".svg")):
        report_file.write(file + "\n")

report_file.close()