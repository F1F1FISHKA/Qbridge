import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import os
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo 

portList = []
ports = QSerialPortInfo().availablePorts()

for port in ports:
    portList.append(port.portName())
print(portList)

dir_path = os.path.dirname(os.path.realpath(__file__))
print (dir_path)
path_to_file = dir_path + "/cfg.txt"

with open(path_to_file) as file: 
    data = file.read().splitlines()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Qsettings")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 299)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 121, 71))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.lineEdit.setText(data[0])
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 30, 31, 20))
        self.lineEdit_2.setText(data[2])
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 30, 20, 20))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 30, 121, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.lineEdit_3.setText(data[4])
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 30, 31, 20))
        self.lineEdit_4.setText(data[6])
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 20, 20))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(310, 30, 121, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.lineEdit_5.setText(data[8])
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 30, 31, 20))
        self.lineEdit_6.setText(data[10])
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 20, 20))
        self.label_3.setObjectName("label_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(460, 30, 121, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.lineEdit_7.setText(data[12])
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 30, 31, 20))
        self.lineEdit_8.setText(data[14])
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 20, 20))
        self.label_4.setObjectName("label_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 110, 121, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_9.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.lineEdit_9.setText(data[16])
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_10.setGeometry(QtCore.QRect(70, 30, 31, 20))
        self.lineEdit_10.setText(data[18])
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(50, 30, 20, 20))
        self.label_5.setObjectName("label_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(160, 110, 121, 71))
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_13.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.lineEdit_13.setText(data[20])
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_14.setGeometry(QtCore.QRect(70, 30, 31, 20))
        self.lineEdit_14.setText(data[22])
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(50, 30, 20, 20))
        self.label_7.setObjectName("label_7")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(310, 110, 121, 71))
        self.groupBox_7.setObjectName("groupBox_7")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_15.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.lineEdit_15.setText(data[24])
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_16.setGeometry(QtCore.QRect(70, 30, 31, 20))
        self.lineEdit_16.setText(data[26])
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_8 = QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setGeometry(QtCore.QRect(50, 30, 20, 20))
        self.label_8.setObjectName("label_8")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(460, 110, 121, 71))
        self.groupBox_8.setObjectName("groupBox_8")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_17.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.lineEdit_17.setText(data[28])
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_18.setGeometry(QtCore.QRect(70, 30, 31, 20))
        self.lineEdit_18.setText(data[30])
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_9 = QtWidgets.QLabel(self.groupBox_8)
        self.label_9.setGeometry(QtCore.QRect(50, 30, 20, 20))
        self.label_9.setObjectName("label_9")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(240, 200, 121, 71))
        self.groupBox_9.setObjectName("groupBox_9")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_19.setGeometry(QtCore.QRect(10, 30, 31, 20))
        self.lineEdit_19.setText(data[32])
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_20.setGeometry(QtCore.QRect(70, 30, 31, 20))
        self.lineEdit_20.setText(data[34])
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_10 = QtWidgets.QLabel(self.groupBox_9)
        self.label_10.setGeometry(QtCore.QRect(50, 30, 20, 20))
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 101, 61))
        self.pushButton.setObjectName("pushButton")
        #self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_2.setGeometry(QtCore.QRect(440, 200, 121, 61))
       # self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 210, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 190, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 240, 111, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(120, 260, 101, 16))
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QSettings"))
        self.groupBox.setTitle(_translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "+"))
        self.groupBox_2.setTitle(_translate("MainWindow", "2"))
        self.label_2.setText(_translate("MainWindow", "+"))
        self.groupBox_3.setTitle(_translate("MainWindow", "3"))
        self.label_3.setText(_translate("MainWindow", "+"))
        self.groupBox_4.setTitle(_translate("MainWindow", "4"))
        self.label_4.setText(_translate("MainWindow", "+"))
        self.groupBox_5.setTitle(_translate("MainWindow", "5"))
        self.label_5.setText(_translate("MainWindow", "+"))
        self.groupBox_6.setTitle(_translate("MainWindow", "6"))
        self.label_7.setText(_translate("MainWindow", "+"))
        self.groupBox_7.setTitle(_translate("MainWindow", "7"))
        self.label_8.setText(_translate("MainWindow", "+"))
        self.groupBox_8.setTitle(_translate("MainWindow", "8"))
        self.label_9.setText(_translate("MainWindow", "+"))
        self.groupBox_9.setTitle(_translate("MainWindow", "9"))
        self.label_10.setText(_translate("MainWindow", "+"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        #self.pushButton_2.setText(_translate("MainWindow", "перезапустить\n Qbridge"))
        self.label_6.setText(_translate("MainWindow", "Порт COM1 нельзя использовать"))
        self.label_11.setText(_translate("MainWindow", "текущий порт :"))
        self.label_12.setText(_translate("MainWindow", data[1]))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
        self.comboBox.currentTextChanged.connect(self.current_text_changed)

    def current_text_changed(self, text):
        print(f'Изменяется currentText, новое значение: {text}')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self._save)
        self.comboBox.addItems(["выберете"] + portList)

    
    





        
        
    def _save(self):
        lineEdits =  self.findChildren(QtWidgets.QLineEdit)
        
        with open(path_to_file, 'w', encoding='utf-8') as f:
            for lineEdit in lineEdits:
                f.write(f'{lineEdit.text()}\n' + f'{self.comboBox.currentText()}\n')
            msg = QtWidgets.QMessageBox.information(
                self, 
                'Успешно сохранено', 
                'Перезапустите программу Qbridge'
            )   

    
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
