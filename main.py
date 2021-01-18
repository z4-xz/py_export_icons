from datetime import datetime
import os

now_str = datetime.now().strftime("%d_%m_%Y_%H;%M")
report_file = open("report_file_" + str(now_str) + ".txt", "a")
report_file.write("Report file generated at " + now_str)
report_file.close()
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)