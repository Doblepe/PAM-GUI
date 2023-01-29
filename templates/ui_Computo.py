# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/victorperez/Escritorio/gui/PAM-GUI/templates/Computo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calendar(object):
    def setupUi(self, Calendar):
        Calendar.setObjectName("Calendar")
        Calendar.resize(1120, 715)
        Calendar.setStyleSheet("background-color:rgb(144, 158, 184);")
        self.BtnBack = QtWidgets.QPushButton(Calendar)
        self.BtnBack.setGeometry(QtCore.QRect(930, 110, 141, 61))
        self.BtnBack.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(214, 234, 248);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.BtnBack.setObjectName("BtnBack")
        self.label = QtWidgets.QLabel(Calendar)
        self.label.setGeometry(QtCore.QRect(0, 0, 1120, 91))
        self.label.setStyleSheet("\n"
"color:white;\n"
"font-size: 32px;\n"
"background: #01BFFF;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ComboPekes = QtWidgets.QComboBox(Calendar)
        self.ComboPekes.setGeometry(QtCore.QRect(40, 130, 241, 41))
        self.ComboPekes.setStyleSheet("color: black; \n"
"background: white;\n"
"")
        self.ComboPekes.setEditable(True)
        self.ComboPekes.setObjectName("ComboPekes")
        self.label_2 = QtWidgets.QLabel(Calendar)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 81, 21))
        self.label_2.setStyleSheet("background: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ShowListWidget = QtWidgets.QListWidget(Calendar)
        self.ShowListWidget.setGeometry(QtCore.QRect(620, 190, 461, 481))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        self.ShowListWidget.setFont(font)
        self.ShowListWidget.setStyleSheet("background:white")
        self.ShowListWidget.setObjectName("ShowListWidget")
        self.BtnShow = QtWidgets.QPushButton(Calendar)
        self.BtnShow.setGeometry(QtCore.QRect(40, 430, 83, 25))
        self.BtnShow.setStyleSheet("background: white;")
        self.BtnShow.setObjectName("BtnShow")
        self.lblcount = QtWidgets.QLabel(Calendar)
        self.lblcount.setGeometry(QtCore.QRect(1070, 970, 471, 31))
        self.lblcount.setStyleSheet("font-size:13pt\n"
"")
        self.lblcount.setText("")
        self.lblcount.setObjectName("lblcount")
        self.BtnShowAllToDo = QtWidgets.QPushButton(Calendar)
        self.BtnShowAllToDo.setGeometry(QtCore.QRect(40, 470, 191, 25))
        self.BtnShowAllToDo.setStyleSheet("background: white;")
        self.BtnShowAllToDo.setObjectName("BtnShowAllToDo")
        self.BtnShowScheudeles = QtWidgets.QPushButton(Calendar)
        self.BtnShowScheudeles.setGeometry(QtCore.QRect(40, 510, 191, 25))
        self.BtnShowScheudeles.setStyleSheet("background: white;")
        self.BtnShowScheudeles.setObjectName("BtnShowScheudeles")
        self.ComboMes = QtWidgets.QComboBox(Calendar)
        self.ComboMes.setGeometry(QtCore.QRect(320, 130, 241, 41))
        self.ComboMes.setStyleSheet("color: black; \n"
"background: white;\n"
"")
        self.ComboMes.setEditable(True)
        self.ComboMes.setObjectName("ComboMes")
        self.label_3 = QtWidgets.QLabel(Calendar)
        self.label_3.setGeometry(QtCore.QRect(320, 100, 81, 21))
        self.label_3.setStyleSheet("background: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.BtnShowUnusualScheudeles = QtWidgets.QPushButton(Calendar)
        self.BtnShowUnusualScheudeles.setGeometry(QtCore.QRect(40, 550, 191, 25))
        self.BtnShowUnusualScheudeles.setStyleSheet("background: white;")
        self.BtnShowUnusualScheudeles.setObjectName("BtnShowUnusualScheudeles")
        self.Btnexportxlsx = QtWidgets.QPushButton(Calendar)
        self.Btnexportxlsx.setGeometry(QtCore.QRect(40, 610, 161, 61))
        self.Btnexportxlsx.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(165, 238, 185);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.Btnexportxlsx.setObjectName("Btnexportxlsx")

        self.retranslateUi(Calendar)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        _translate = QtCore.QCoreApplication.translate
        Calendar.setWindowTitle(_translate("Calendar", "Form"))
        self.BtnBack.setText(_translate("Calendar", "Back "))
        self.label.setText(_translate("Calendar", "Computo de horas"))
        self.label_2.setText(_translate("Calendar", "Pekes"))
        self.BtnShow.setText(_translate("Calendar", "Mostrar"))
        self.BtnShowAllToDo.setText(_translate("Calendar", "Mostrar citas por hacer"))
        self.BtnShowScheudeles.setText(_translate("Calendar", "Mostrar citas realizadas"))
        self.label_3.setText(_translate("Calendar", "Mes"))
        self.BtnShowUnusualScheudeles.setText(_translate("Calendar", "Coordinacinoes realizadas"))
        self.Btnexportxlsx.setText(_translate("Calendar", "Exportar XLSX"))