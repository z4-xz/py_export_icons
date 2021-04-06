import sys
from PyQt5 import QtWidgets as QtW
from PyQt5 import QtCore as QtC
from PyQt5 import QtGui as QtG
from PyQt5 import uic
import os
Ui_MainWindow, baseClass = uic.loadUiType("gui.ui")

class MainWindow(baseClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.background_color_line_edit.setValidator(QtG.QRegExpValidator(QtC.QRegExp(r'#[a-fA-F0-9]{6}$')))
        self.ui.concatenate_checkbox.stateChanged.connect(self.concatenate_checkbox_state_changed)
        self.ui.export_checkbox.stateChanged.connect(self.export_checkbox_state_changed)
        self.ui.start_button.clicked.connect(self.start_button_clicked)
        scene = QtW.QGraphicsScene(self.ui.result_image_view)
        pixmap = QtG.QPixmap("output.png")
        pixmap = pixmap.scaled(400, 400, QtC.Qt.KeepAspectRatio)
        item = QtW.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.ui.result_image_view.setScene(scene)
        self.ui.source_button.clicked.connect(self.browse_files)
        #
        self.show()
        
    
    
    def browse_files(self):
        fname = QtW.QFileDialog.getExistingDirectory(self.ui.source_button, 'Open file', '')
        self.ui.source_line_edit.setText(fname)
        svgs=[]
        svgs += [file for file in (os.listdir(fname)) if(file.endswith(".svg"))]
        self.ui.files_table.clear()
        for i in svgs:
            self.ui.files_table.addItem(i)
            self.ui.files_table.itemDoubleClcked.connect()

    def export_checkbox_state_changed(self, state):
        if(state==QtC.Qt.Checked):
            self.ui.icon_width_spinbox.setEnabled(True)
            self.ui.icon_height_spinbox.setEnabled(True)
        elif not self.ui.concatenate_checkbox.isChecked():
            self.ui.icon_width_spinbox.setEnabled(False)
            self.ui.icon_height_spinbox.setEnabled(False)
    
    def concatenate_checkbox_state_changed(self, state):
        if(state==QtC.Qt.Checked):
            self.ui.columns_spinbox.setEnabled(True)
            self.ui.rows_spinbox.setEnabled(True)
            self.ui.icon_width_spinbox.setEnabled(True)
            self.ui.icon_height_spinbox.setEnabled(True)
            self.ui.h_icon_margin_spinbox.setEnabled(True)
            self.ui.v_icon_margin_spinbox.setEnabled(True)
            self.ui.h_image_margin_spinbox.setEnabled(True)
            self.ui.v_image_margin_spinbox.setEnabled(True)
            self.ui.background_color_line_edit.setEnabled(True)
        else:
            if not self.ui.export_checkbox.isChecked():
                self.ui.icon_width_spinbox.setEnabled(False)
                self.ui.icon_height_spinbox.setEnabled(False)
            self.ui.columns_spinbox.setEnabled(False)
            self.ui.rows_spinbox.setEnabled(False)
            self.ui.h_icon_margin_spinbox.setEnabled(False)
            self.ui.v_icon_margin_spinbox.setEnabled(False)
            self.ui.h_image_margin_spinbox.setEnabled(False)
            self.ui.v_image_margin_spinbox.setEnabled(False)
            self.ui.background_color_line_edit.setEnabled(False)

    def start_button_clicked(self):
        if (not self.ui.export_checkbox.isChecked()) and (not self.ui.concatenate_checkbox.isChecked()):
            return
        self.ui.start_button.setEnabled(False)
        self.ui.export_checkbox.setEnabled(False)
        self.ui.concatenate_checkbox.setEnabled(False)
        if self.ui.export_checkbox.isChecked():
            print("Export active")
        if self.ui.concatenate_checkbox.isChecked():
            print("Concatenate active")


if __name__ == "__main__":
    app = QtW.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())