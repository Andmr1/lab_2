import sys
from PyQt5 import QtCore, QtWidgets
from task1 import create_main_ann
from task2 import copy_to_new_directory
from task2 import create_new_dir_ann
from task3 import copy_to_new_dir_with_random_naming
from task5 import MyIter

editorProgram = 'notepad'


class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiMainWindow, self).__init__()
        self.path1 = ""
        self.path2 = ""
        self.path3 = ""
        self.it_good = MyIter("good")
        self.it_bad = MyIter("bad")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 714)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 531, 41))
        self.label.setStyleSheet("font: 12pt \"Segoe UI Symbol\";")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 421, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(440, 70, 81, 21))
        self.save_button.setObjectName("save_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 521, 61))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.func1 = QtWidgets.QPushButton(self.centralwidget)
        self.func1.setGeometry(QtCore.QRect(30, 180, 191, 81))
        self.func1.setObjectName("func1")
        self.func2 = QtWidgets.QPushButton(self.centralwidget)
        self.func2.setGeometry(QtCore.QRect(30, 290, 191, 81))
        self.func2.setTabletTracking(False)
        self.func2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.func2.setObjectName("func2")
        self.func3 = QtWidgets.QPushButton(self.centralwidget)
        self.func3.setGeometry(QtCore.QRect(230, 180, 301, 81))
        self.func3.setObjectName("func3")
        self.func4 = QtWidgets.QPushButton(self.centralwidget)
        self.func4.setGeometry(QtCore.QRect(180, 590, 181, 61))
        self.func4.setObjectName("func4")
        self.func5 = QtWidgets.QPushButton(self.centralwidget)
        self.func5.setGeometry(QtCore.QRect(230, 290, 301, 81))
        self.func5.setObjectName("func5")
        self.Reviewtype = QtWidgets.QComboBox(self.centralwidget)
        self.Reviewtype.setGeometry(QtCore.QRect(220, 480, 101, 22))
        self.Reviewtype.setObjectName("Reviewtype")
        self.Path = QtWidgets.QLabel(self.centralwidget)
        self.Path.setGeometry(QtCore.QRect(10, 530, 521, 41))
        self.Path.setAlignment(QtCore.Qt.AlignCenter)
        self.Path.setObjectName("Path")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 440, 521, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.func2.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.save_button.raise_()
        self.label_2.raise_()
        self.func1.raise_()
        self.func3.raise_()
        self.func4.raise_()
        self.func5.raise_()
        self.Reviewtype.raise_()
        self.Path.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.save_button.clicked.connect(self.save)
        self.func1.clicked.connect(self.create_annotation_1)
        self.func2.clicked.connect(self.copy_directory_to_one_folder)
        self.func3.clicked.connect(self.create_ann_for_second_dir)
        self.func5.clicked.connect(self.create_random_named_dataset)
        self.func4.clicked.connect(self.show_next)
        self.Reviewtype.addItems(["good", "bad"])

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "you"))
        self.label.setToolTip(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style=\""
                                         "font-size:12pt; font-weight:600;"
                                         "\">Main dataset path</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Main dataset path"))
        self.save_button.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\""
                                               " font-weight:600;\">Save main dataset path</span></p></body></html>"))
        self.save_button.setText(_translate("MainWindow", "Save path"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\""
                                        " font-size:12pt;\">Dataset organisation</span></p></body></html>"))
        self.func1.setText(_translate("MainWindow", "Create main dataset annotation"))
        self.func2.setText(_translate("MainWindow", "Moove main dataset"))
        self.func3.setText(_translate("MainWindow", "Create annotation for mooved dataset"))
        self.func4.setText(_translate("MainWindow", "Next"))
        self.func5.setText(_translate("MainWindow", "Create dataset with random file names and it\'s annotation"))
        self.Path.setText(_translate("MainWindow", "<html><head/><body><p align=\""
                                     "сenter\"><span style=\" font-size:10pt;\">Review path</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\""
                                        "font-size:12pt;\">Iteration</span></p></body></html>"))

    def save(self):
        self.path1 = self.lineEdit.text()

    def create_annotation_1(self):
        if self.path1 != "":
            create_main_ann(self.path1)

    def copy_directory_to_one_folder(self):
        self.path2 = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if self.path1 != "" and self.path2 != "":
            copy_to_new_directory(self.path1 + "/good", self.path2)
            copy_to_new_directory(self.path1 + "/bad", self.path2)

    def create_ann_for_second_dir(self):
        self.path2 = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if self.path2 != "":
            create_new_dir_ann(self.path2)

    def create_random_named_dataset(self):
        if self.path1 != "":
            self.path3 = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
            copy_to_new_dir_with_random_naming(self.path1, self.path3)
            print("Done!")

    def show_next(self):
        if self.Reviewtype.currentText() == "good":
            rev_path = self.it_good.__next__()
            self.Path.setText(rev_path)
            if rev_path != "None":
                process = QtCore.QProcess(self)
                process.start(editorProgram, [rev_path])
                self.setEnabled(False)
                process.finished.connect(lambda: self.setEnabled(True))

        else:
            rev_path = self.it_bad.__next__()
            self.Path.setText(rev_path)
            if rev_path != "None":
                process = QtCore.QProcess(self)
                process.start(editorProgram, [rev_path])
                self.setEnabled(False)
                process.finished.connect(lambda: self.setEnabled(True))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.retranslate_ui()
    MainWindow.show()
    sys.exit(app.exec_())
