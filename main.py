from PyQt5 import QtCore, QtGui, QtWidgets
import os
import json
from datetime import datetime
from PIL import Image
from cairosvg import svg2png
import argparse


settings = json.load(open('settings.json', 'r')) 
bg_color = settings["background"]
input_dir_path = "./svg/"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 620)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(460, 30, 531, 431))
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 431, 271))
        self.groupBox.setObjectName("groupBox")
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setGeometry(QtCore.QRect(10, 50, 201, 211))
        self.listView.setObjectName("listView")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 30, 85, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 300, 431, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 401, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinBox_4 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_4.setObjectName("spinBox_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_4)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.spinBox_6 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_6.setObjectName("spinBox_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_6)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.spinBox_5 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_5.setObjectName("spinBox_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_5)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.spinBox_7 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_7.setObjectName("spinBox_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_7)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.spinBox_8 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_8.setObjectName("spinBox_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_8)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.spinBox_9 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_9.setObjectName("spinBox_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_9)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.formLayout_3)
        self.filename = QtWidgets.QLineEdit(self.groupBox_2)
        self.filename.setGeometry(QtCore.QRect(10, 180, 171, 23))
        self.filename.setObjectName("filename")
        self.browse = QtWidgets.QPushButton(self.groupBox_2)
        self.browse.setGeometry(QtCore.QRect(190, 180, 80, 23))
        self.browse.setObjectName("browse")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 160, 81, 16))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 230, 80, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 81, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 230, 171, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(490, 490, 85, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(490, 510, 101, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 470, 381, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Export"))
        self.checkBox_3.setText(_translate("MainWindow", "Select all"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Concatenate"))
        self.label_6.setText(_translate("MainWindow", "Columns"))
        self.label_7.setText(_translate("MainWindow", "Icon width"))
        self.label_8.setText(_translate("MainWindow", "Horizontal icon margin"))
        self.label_5.setText(_translate("MainWindow", "Horizontal image margin"))
        self.label_9.setText(_translate("MainWindow", "Rows"))
        self.label_10.setText(_translate("MainWindow", "Icon height"))
        self.label_11.setText(_translate("MainWindow", "Vertical icon margin"))
        self.label_12.setText(_translate("MainWindow", "Vertical image margin"))
        self.browse.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Source"))
        self.pushButton_3.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Save as"))
        self.checkBox.setText(_translate("MainWindow", "Export"))
        self.checkBox_2.setText(_translate("MainWindow", "Concatenate"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

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

