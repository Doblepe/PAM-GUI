# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vicdoblepe/Escritorio/Psico-project/pyqt5-full-app-tutorial-for-beginners-main/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1769, 1011)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(-60, 0, 1831, 1011))
        self.bgwidget.setStyleSheet("background-color:rgb(144, 158, 184);")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(120, 100, 251, 61))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 190, 391, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.citarScreen = QtWidgets.QPushButton(self.bgwidget)
        self.citarScreen.setGeometry(QtCore.QRect(110, 350, 341, 51))
        self.citarScreen.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.citarScreen.setObjectName("citarScreen")
        self.createKidScreen = QtWidgets.QPushButton(self.bgwidget)
        self.createKidScreen.setGeometry(QtCore.QRect(490, 350, 341, 51))
        self.createKidScreen.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.createKidScreen.setObjectName("createKidScreen")
        self.agendaScreen = QtWidgets.QPushButton(self.bgwidget)
        self.agendaScreen.setGeometry(QtCore.QRect(860, 350, 331, 51))
        self.agendaScreen.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.agendaScreen.setObjectName("agendaScreen")
        self.computoScreen = QtWidgets.QPushButton(self.bgwidget)
        self.computoScreen.setGeometry(QtCore.QRect(100, 460, 361, 51))
        self.computoScreen.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.computoScreen.setObjectName("computoScreen")
        self.infoScreen = QtWidgets.QPushButton(self.bgwidget)
        self.infoScreen.setGeometry(QtCore.QRect(490, 460, 361, 51))
        self.infoScreen.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.infoScreen.setObjectName("infoScreen")
        self.actionHome = QtWidgets.QAction(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/vicdoblepe/Escritorio/Psico-project/pyqt5-full-app-tutorial-for-beginners-main/fugue-icons-3.5.6/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon)
        self.actionHome.setObjectName("actionHome")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.label_2.setText(_translate("Dialog", "Choose your option"))
        self.citarScreen.setText(_translate("Dialog", "Citar"))
        self.createKidScreen.setText(_translate("Dialog", "Create a Kid"))
        self.agendaScreen.setText(_translate("Dialog", "Agenda"))
        self.computoScreen.setText(_translate("Dialog", "C??mputo"))
        self.infoScreen.setText(_translate("Dialog", "Informaci??n"))
        self.actionHome.setText(_translate("Dialog", "Home"))
