# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vicdoblepe/Escritorio/Psico-project/pyqt5-full-app-tutorial-for-beginners-main/QCalendar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calendar(object):
    def setupUi(self, Calendar):
        Calendar.setObjectName("Calendar")
        Calendar.resize(1213, 759)
        Calendar.setStyleSheet("background-color:rgb(144, 158, 184);")
        self.calendarWidget = QtWidgets.QCalendarWidget(Calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 180, 531, 351))
        self.calendarWidget.setStyleSheet("background:white;\n"
"font: 13pt;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.listWidget = QtWidgets.QListWidget(Calendar)
        self.listWidget.setGeometry(QtCore.QRect(790, 180, 391, 351))
        self.listWidget.setStyleSheet("background:white")
        self.listWidget.setObjectName("listWidget")
        self.timefield = QtWidgets.QTimeEdit(Calendar)
        self.timefield.setGeometry(QtCore.QRect(50, 580, 118, 26))
        self.timefield.setStyleSheet("background:white;\n"
"font: 13pt;\n"
"")
        self.timefield.setObjectName("timefield")
        self.BtnSaveChanges = QtWidgets.QPushButton(Calendar)
        self.BtnSaveChanges.setGeometry(QtCore.QRect(790, 570, 381, 51))
        self.BtnSaveChanges.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.BtnSaveChanges.setObjectName("BtnSaveChanges")
        self.BtnAddNew = QtWidgets.QPushButton(Calendar)
        self.BtnAddNew.setGeometry(QtCore.QRect(700, 650, 121, 41))
        self.BtnAddNew.setObjectName("BtnAddNew")
        self.BtnBack = QtWidgets.QPushButton(Calendar)
        self.BtnBack.setGeometry(QtCore.QRect(990, 110, 141, 31))
        self.BtnBack.setObjectName("BtnBack")
        self.label = QtWidgets.QLabel(Calendar)
        self.label.setGeometry(QtCore.QRect(-10, 0, 1241, 91))
        self.label.setStyleSheet("\n"
"color:white;\n"
"font-size: 32px;\n"
"background: #01BFFF;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.nombreField = QtWidgets.QLineEdit(Calendar)
        self.nombreField.setGeometry(QtCore.QRect(360, 570, 281, 41))
        self.nombreField.setStyleSheet("background:white")
        self.nombreField.setObjectName("nombreField")
        self.label_2 = QtWidgets.QLabel(Calendar)
        self.label_2.setGeometry(QtCore.QRect(200, 570, 131, 41))
        self.label_2.setStyleSheet("background:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lblFeedback = QtWidgets.QLabel(Calendar)
        self.lblFeedback.setGeometry(QtCore.QRect(40, 640, 621, 71))
        self.lblFeedback.setStyleSheet("Color: green;\n"
"font:12pt;")
        self.lblFeedback.setText("")
        self.lblFeedback.setObjectName("lblFeedback")

        self.retranslateUi(Calendar)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        _translate = QtCore.QCoreApplication.translate
        Calendar.setWindowTitle(_translate("Calendar", "Form"))
        self.BtnSaveChanges.setText(_translate("Calendar", "Save Changes"))
        self.BtnAddNew.setText(_translate("Calendar", "Add-new"))
        self.BtnBack.setText(_translate("Calendar", "Back to Main"))
        self.label.setText(_translate("Calendar", "Agenda"))
        self.label_2.setText(_translate("Calendar", "Nombre del niño"))
