# Form implementation generated from reading ui file 'newui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(35, 35, 67, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.ConnectionTypeComboBox = ComboBox(parent=self.centralwidget)
        self.ConnectionTypeComboBox.setGeometry(QtCore.QRect(140, 35, 300, 34))
        self.ConnectionTypeComboBox.setStyleSheet("ComboBox {\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-radius: 5px;\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    padding: 5px 31px 6px 11px;\n"
"    font: 14px \'Segoe UI\', \'Microsoft YaHei\';\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 0.7);\n"
"    text-align: left;\n"
"}\n"
"\n"
"ComboBox:hover {\n"
"    background-color: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"ComboBox:pressed {\n"
"    background-color: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"}\n"
"\n"
"ComboBox:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"\n"
"ComboBoxMenu>MenuActionListWidget {\n"
"    border: 1px solid rgba(0, 0, 0, 0.1);\n"
"    border-radius: 9px;\n"
"    background-color: rgb(249, 249, 249);\n"
"    outline: none;\n"
"    font: 14px \'Segoe UI\', \'Microsoft YaHei\';\n"
"}\n"
"\n"
"ComboBoxMenu>MenuActionListWidget::item {\n"
"    margin-top: 4px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"ComboBoxMenu>MenuActionListWidget::item:disabled {\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"    color: black;\n"
"}\n"
"\n"
"ComboBoxMenu>MenuActionListWidget::item:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"}\n"
"\n"
"ComboBoxMenu>MenuActionListWidget::item:selected {\n"
"    background-color: rgba(0, 0, 0, 7);\n"
"    color: black;\n"
"}\n"
"\n"
"ComboBoxMenu>MenuActionListWidget::item:selected:active {\n"
"    background-color: rgba(0, 0, 0, 0.06);\n"
"    color: rgba(0, 0, 0, 0.7);\n"
"}")
        self.ConnectionTypeComboBox.setText("")
        self.ConnectionTypeComboBox.setObjectName("ComboBox")
        self.ConnectBtn = PushButton(parent=self.centralwidget)
        self.ConnectBtn.setGeometry(QtCore.QRect(330, 100, 106, 34))
        self.ConnectBtn.setObjectName("PushButton")
        self.ListView = ListView(parent=self.centralwidget)
        self.ListView.setGeometry(QtCore.QRect(10, 280, 461, 351))
        self.ListView.setObjectName("ListView")
        self.StartBtn = PushButton(parent=self.centralwidget)
        self.StartBtn.setGeometry(QtCore.QRect(20, 220, 106, 34))
        self.StartBtn.setObjectName("PushButton_2")
        self.PauseBtn = PushButton(parent=self.centralwidget)
        self.PauseBtn.setGeometry(QtCore.QRect(140, 220, 106, 34))
        self.PauseBtn.setObjectName("PushButton_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 100, 100, 34))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "碧蓝档案初始号工具"))
        self.label.setText(_translate("MainWindow", "连接模式"))
        self.ConnectBtn.setText(_translate("MainWindow", "连接"))
        self.StartBtn.setText(_translate("MainWindow", "开始"))
        self.PauseBtn.setText(_translate("MainWindow", "暂停"))
        self.label_2.setText(_translate("MainWindow", "未连接"))
from qfluentwidgets import ComboBox, ListView, PushButton
