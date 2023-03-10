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
        self.timefield = QtWidgets.QTimeEdit(Calendar)
        self.timefield.setGeometry(QtCore.QRect(50, 565, 151, 41))
        self.timefield.setStyleSheet("background:white;\n"
"font: 13pt;\n"
"")
        self.timefield.setObjectName("timefield")
        self.BtnAddNew = QtWidgets.QPushButton(Calendar)
        self.BtnAddNew.setGeometry(QtCore.QRect(60, 640, 121, 41))
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
        self.lblFeedback = QtWidgets.QLabel(Calendar)
        self.lblFeedback.setGeometry(QtCore.QRect(430, 560, 741, 151))
        self.lblFeedback.setStyleSheet("Color: green;\n"
"font:12pt;")
        self.lblFeedback.setText("")
        self.lblFeedback.setObjectName("lblFeedback")
        self.ComboPekes = QtWidgets.QComboBox(Calendar)
        self.ComboPekes.setEnabled(True)
        self.ComboPekes.setGeometry(QtCore.QRect(610, 110, 201, 25))
        self.ComboPekes.setStyleSheet("color: black; \n"
"background: white;\n"
"")
        self.ComboPekes.setEditable(True)
        self.ComboPekes.setObjectName("ComboPekes")
        self.BtnAddSpecialDate = QtWidgets.QPushButton(Calendar)
        self.BtnAddSpecialDate.setGeometry(QtCore.QRect(980, 280, 151, 31))
        self.BtnAddSpecialDate.setObjectName("BtnAddSpecialDate")

        self.retranslateUi(Calendar)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        _translate = QtCore.QCoreApplication.translate
        Calendar.setWindowTitle(_translate("Calendar", "Form"))
        self.BtnAddNew.setText(_translate("Calendar", "A??adir Cita"))
        self.BtnBack.setText(_translate("Calendar", "Back to Main"))
        self.label.setText(_translate("Calendar", "Preprarar cita"))
        self.BtnAddSpecialDate.setText(_translate("Calendar", "A??adir cita especial"))
