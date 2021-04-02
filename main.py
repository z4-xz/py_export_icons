from PyQt5 import QtCore, QtGui, QtWidgets
import os
import json
from datetime import datetime
from PIL import Image
from cairosvg import svg2png
import argparse
import re


settings = json.load(open('settings.json', 'r')) 
bg_color = settings["background"]
input_dir_path = "./svg/"
args_dict={}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(910, 420))
        MainWindow.setMaximumSize(QtCore.QSize(910, 420))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.result_image_view = QtWidgets.QGraphicsView(self.centralwidget)
        self.result_image_view.setGeometry(QtCore.QRect(500, 10, 401, 401))
        self.result_image_view.setObjectName("result_image_view")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(170, 330, 321, 81))
        self.start_button.setObjectName("start_button")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 40, 231, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.columns_label = QtWidgets.QLabel(self.layoutWidget)
        self.columns_label.setObjectName("columns_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.columns_label)
        self.columns_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.columns_spinbox.setMinimum(1)
        self.columns_spinbox.setMaximum(90)
        self.columns_spinbox.setProperty("value", 5)
        self.columns_spinbox.setObjectName("columns_spinbox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.columns_spinbox)
        self.rows_label = QtWidgets.QLabel(self.layoutWidget)
        self.rows_label.setObjectName("rows_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rows_label)
        self.rows_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.rows_spinbox.setMinimum(1)
        self.rows_spinbox.setMaximum(90)
        self.rows_spinbox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.rows_spinbox.setProperty("value", 10)
        self.rows_spinbox.setObjectName("rows_spinbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rows_spinbox)
        self.icon_width_label = QtWidgets.QLabel(self.layoutWidget)
        self.icon_width_label.setObjectName("icon_width_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.icon_width_label)
        self.icon_width_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.icon_width_spinbox.setMinimum(20)
        self.icon_width_spinbox.setMaximum(700)
        self.icon_width_spinbox.setSingleStep(10)
        self.icon_width_spinbox.setProperty("value", 100)
        self.icon_width_spinbox.setObjectName("icon_width_spinbox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.icon_width_spinbox)
        self.icon_height_label = QtWidgets.QLabel(self.layoutWidget)
        self.icon_height_label.setObjectName("icon_height_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.icon_height_label)
        self.icon_height_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.icon_height_spinbox.setMinimum(20)
        self.icon_height_spinbox.setMaximum(700)
        self.icon_height_spinbox.setSingleStep(10)
        self.icon_height_spinbox.setProperty("value", 100)
        self.icon_height_spinbox.setObjectName("icon_height_spinbox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.icon_height_spinbox)
        self.h_icon_margin_label = QtWidgets.QLabel(self.layoutWidget)
        self.h_icon_margin_label.setObjectName("h_icon_margin_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.h_icon_margin_label)
        self.h_icon_margin_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.h_icon_margin_spinbox.setMinimum(10)
        self.h_icon_margin_spinbox.setMaximum(500)
        self.h_icon_margin_spinbox.setSingleStep(10)
        self.h_icon_margin_spinbox.setObjectName("h_icon_margin_spinbox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.h_icon_margin_spinbox)
        self.v_icon_margin_label = QtWidgets.QLabel(self.layoutWidget)
        self.v_icon_margin_label.setObjectName("v_icon_margin_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.v_icon_margin_label)
        self.v_icon_margin_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.v_icon_margin_spinbox.setMinimum(10)
        self.v_icon_margin_spinbox.setMaximum(500)
        self.v_icon_margin_spinbox.setSingleStep(10)
        self.v_icon_margin_spinbox.setObjectName("v_icon_margin_spinbox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.v_icon_margin_spinbox)
        self.h_image_margin_label = QtWidgets.QLabel(self.layoutWidget)
        self.h_image_margin_label.setObjectName("h_image_margin_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.h_image_margin_label)
        self.h_image_margin_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.h_image_margin_spinbox.setMinimum(10)
        self.h_image_margin_spinbox.setMaximum(500)
        self.h_image_margin_spinbox.setSingleStep(10)
        self.h_image_margin_spinbox.setObjectName("h_image_margin_spinbox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.h_image_margin_spinbox)
        self.v_image_margin_label = QtWidgets.QLabel(self.layoutWidget)
        self.v_image_margin_label.setObjectName("v_image_margin_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.v_image_margin_label)
        self.v_image_margin_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
        self.v_image_margin_spinbox.setMinimum(10)
        self.v_image_margin_spinbox.setMaximum(500)
        self.v_image_margin_spinbox.setSingleStep(10)
        self.v_image_margin_spinbox.setObjectName("v_image_margin_spinbox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.v_image_margin_spinbox)
        self.background_color_label = QtWidgets.QLabel(self.layoutWidget)
        self.background_color_label.setObjectName("background_color_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.background_color_label)
        self.background_color_line_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.background_color_line_edit.setObjectName("background_color_line_edit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.background_color_line_edit)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 290, 201, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.source_line_edit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.source_line_edit.setMaximumSize(QtCore.QSize(160, 23))
        self.source_line_edit.setObjectName("source_line_edit")
        self.horizontalLayout.addWidget(self.source_line_edit)
        self.source_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.source_button.setMinimumSize(QtCore.QSize(40, 23))
        self.source_button.setMaximumSize(QtCore.QSize(40, 23))
        self.source_button.setObjectName("source_button")
        self.horizontalLayout.addWidget(self.source_button)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 350, 111, 50))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.export_checkbox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.export_checkbox.setObjectName("export_checkbox")
        self.verticalLayout.addWidget(self.export_checkbox)
        self.concatenate_checkbox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.concatenate_checkbox.setChecked(True)
        self.concatenate_checkbox.setObjectName("concatenate_checkbox")
        self.verticalLayout.addWidget(self.concatenate_checkbox)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 311))
        self.groupBox.setObjectName("groupBox")
        self.source_label = QtWidgets.QLabel(self.groupBox)
        self.source_label.setGeometry(QtCore.QRect(10, 260, 42, 29))
        self.source_label.setObjectName("source_label")
        self.select_all_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.select_all_checkbox.setGeometry(QtCore.QRect(10, 30, 85, 21))
        self.select_all_checkbox.setObjectName("select_all_checkbox")
        self.files_table = QtWidgets.QTableWidget(self.groupBox)
        self.files_table.setGeometry(QtCore.QRect(10, 50, 201, 211))
        self.files_table.setObjectName("files_table")
        self.files_table.setColumnCount(0)
        self.files_table.setRowCount(0)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 10, 251, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.result_image_view.raise_()
        self.start_button.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget1.raise_()
        self.layoutWidget2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        self.background_color_line_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(r'#[a-fA-F0-9]{6}$')))
        self.concatenate_checkbox.stateChanged.connect(self.concatenate_checkbox_state_changed)
        self.export_checkbox.stateChanged.connect(self.export_checkbox_state_changed)
        self.start_button.clicked.connect(self.start_button_clicked)
        scene = QtWidgets.QGraphicsScene(self.result_image_view)
        pixmap = QtGui.QPixmap("output.png")
        pixmap = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.result_image_view.setScene(scene)
        self.source_button.clicked.connect(self.browse_files)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def browse_files(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(self.source_button, 'Open file', 'E:\GIT\py_export_icons_gui\py_export_icons')
        self.source_label.setText(fname[0])

    def export_checkbox_state_changed(self, state):
        if(state==QtCore.Qt.Checked):
            self.icon_width_spinbox.setEnabled(True)
            self.icon_height_spinbox.setEnabled(True)
        elif not self.concatenate_checkbox.isChecked():
            self.icon_width_spinbox.setEnabled(False)
            self.icon_height_spinbox.setEnabled(False)
    
    def concatenate_checkbox_state_changed(self, state):
        if(state==QtCore.Qt.Checked):
            self.columns_spinbox.setEnabled(True)
            self.rows_spinbox.setEnabled(True)
            self.icon_width_spinbox.setEnabled(True)
            self.icon_height_spinbox.setEnabled(True)
            self.h_icon_margin_spinbox.setEnabled(True)
            self.v_icon_margin_spinbox.setEnabled(True)
            self.h_image_margin_spinbox.setEnabled(True)
            self.v_image_margin_spinbox.setEnabled(True)
            self.background_color_line_edit.setEnabled(True)
        else:
            if not self.export_checkbox.isChecked():
                self.icon_width_spinbox.setEnabled(False)
                self.icon_height_spinbox.setEnabled(False)
            self.columns_spinbox.setEnabled(False)
            self.rows_spinbox.setEnabled(False)
            self.h_icon_margin_spinbox.setEnabled(False)
            self.v_icon_margin_spinbox.setEnabled(False)
            self.h_image_margin_spinbox.setEnabled(False)
            self.v_image_margin_spinbox.setEnabled(False)
            self.background_color_line_edit.setEnabled(False)

    def start_button_clicked(self):
        if (not self.export_checkbox.isChecked()) and (not self.concatenate_checkbox.isChecked()):
            return
        self.start_button.setEnabled(False)
        self.export_checkbox.setEnabled(False)
        self.concatenate_checkbox.setEnabled(False)
        if self.export_checkbox.isChecked():
            print("Export active")
        if self.concatenate_checkbox.isChecked():
            print("Concatenate active")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "py_expor_icons"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.columns_label.setText(_translate("MainWindow", "Columns"))
        self.rows_label.setText(_translate("MainWindow", "Rows"))
        self.icon_width_label.setText(_translate("MainWindow", "Icon width"))
        self.icon_height_label.setText(_translate("MainWindow", "Icon height"))
        self.h_icon_margin_label.setText(_translate("MainWindow", "Horizontal icon margin"))
        self.v_icon_margin_label.setText(_translate("MainWindow", "Vertical icon margin"))
        self.h_image_margin_label.setText(_translate("MainWindow", "Horizontal image margin"))
        self.v_image_margin_label.setText(_translate("MainWindow", "Vertical image margin"))
        self.background_color_label.setText(_translate("MainWindow", "Background color (#HEX)"))
        self.source_button.setText(_translate("MainWindow", "..."))
        self.export_checkbox.setText(_translate("MainWindow", "Export"))
        self.concatenate_checkbox.setText(_translate("MainWindow", "Concatenate"))
        self.groupBox.setTitle(_translate("MainWindow", "Files"))
        self.source_label.setText(_translate("MainWindow", "Source"))
        self.select_all_checkbox.setText(_translate("MainWindow", "Select all"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Properties"))





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

def export(svgs: list):
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

def args_parser():
    global args_dict
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

def main():
    global settings
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
    export(svgs)

    if len(pngs) <= settings["rows"] * settings["columns"]:
        concatenate(pngs, output_dir_path)
    else:
        print("Not enough rows or cols")
    print("Done.")

