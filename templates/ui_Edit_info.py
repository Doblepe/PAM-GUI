# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/victorperez/Escritorio/gui/PAM-GUI/templates/Edit_info.ui'
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
        self.ComboPekes.setGeometry(QtCore.QRect(120, 130, 241, 41))
        self.ComboPekes.setStyleSheet("color: black; \n"
"background: white;\n"
"")
        self.ComboPekes.setEditable(True)
        self.ComboPekes.setObjectName("ComboPekes")
        self.label_2 = QtWidgets.QLabel(Calendar)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 62, 17))
        self.label_2.setStyleSheet("background: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lblcount = QtWidgets.QLabel(Calendar)
        self.lblcount.setGeometry(QtCore.QRect(680, 600, 471, 31))
        self.lblcount.setStyleSheet("font-size:13pt\n"
"")
        self.lblcount.setText("")
        self.lblcount.setObjectName("lblcount")
        self.lblNombre = QtWidgets.QLabel(Calendar)
        self.lblNombre.setGeometry(QtCore.QRect(20, 220, 71, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblNombre.setFont(font)
        self.lblNombre.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lblNombre.setObjectName("lblNombre")
        self.lblProge1 = QtWidgets.QLabel(Calendar)
        self.lblProge1.setGeometry(QtCore.QRect(10, 260, 81, 20))
        self.lblProge1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lblProge1.setObjectName("lblProge1")
        self.lblTfn2 = QtWidgets.QLabel(Calendar)
        self.lblTfn2.setGeometry(QtCore.QRect(20, 460, 61, 21))
        self.lblTfn2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lblTfn2.setObjectName("lblTfn2")
        self.lblTfn1 = QtWidgets.QLabel(Calendar)
        self.lblTfn1.setGeometry(QtCore.QRect(20, 300, 61, 21))
        self.lblTfn1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lblTfn1.setObjectName("lblTfn1")
        self.lblEmail = QtWidgets.QLabel(Calendar)
        self.lblEmail.setGeometry(QtCore.QRect(30, 350, 61, 20))
        self.lblEmail.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lblEmail.setObjectName("lblEmail")
        self.lblProge2 = QtWidgets.QLabel(Calendar)
        self.lblProge2.setGeometry(QtCore.QRect(10, 400, 81, 20))
        self.lblProge2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lblProge2.setObjectName("lblProge2")
        self.lblOrigne = QtWidgets.QLabel(Calendar)
        self.lblOrigne.setGeometry(QtCore.QRect(10, 510, 81, 20))
        self.lblOrigne.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lblOrigne.setObjectName("lblOrigne")
        self.progenitor1field = QtWidgets.QLineEdit(Calendar)
        self.progenitor1field.setGeometry(QtCore.QRect(120, 260, 271, 31))
        self.progenitor1field.setStyleSheet("background-color:white;\n"
"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.progenitor1field.setObjectName("progenitor1field")
        self.emailfield = QtWidgets.QLineEdit(Calendar)
        self.emailfield.setGeometry(QtCore.QRect(120, 360, 271, 31))
        self.emailfield.setStyleSheet("background-color:white;\n"
"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.emailfield.setObjectName("emailfield")
        self.tfn1field = QtWidgets.QLineEdit(Calendar)
        self.tfn1field.setGeometry(QtCore.QRect(120, 310, 271, 31))
        self.tfn1field.setStyleSheet("background-color:white;\n"
"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.tfn1field.setObjectName("tfn1field")
        self.progenitor2field = QtWidgets.QLineEdit(Calendar)
        self.progenitor2field.setGeometry(QtCore.QRect(120, 410, 271, 31))
        self.progenitor2field.setStyleSheet("background-color:white;\n"
"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.progenitor2field.setObjectName("progenitor2field")
        self.nombrefield = QtWidgets.QLineEdit(Calendar)
        self.nombrefield.setGeometry(QtCore.QRect(120, 210, 271, 31))
        self.nombrefield.setStyleSheet("background-color:white;\n"
"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.nombrefield.setText("")
        self.nombrefield.setObjectName("nombrefield")
        self.tfn2field = QtWidgets.QLineEdit(Calendar)
        self.tfn2field.setGeometry(QtCore.QRect(120, 460, 271, 31))
        self.tfn2field.setStyleSheet("background-color:white;\n"
"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.tfn2field.setObjectName("tfn2field")
        self.Public = QtWidgets.QCheckBox(Calendar)
        self.Public.setGeometry(QtCore.QRect(120, 510, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Public.setFont(font)
        self.Public.setStyleSheet("background-color:white;\n"
"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"padding-left: 15px")
        self.Public.setChecked(True)
        self.Public.setObjectName("Public")
        self.BtnBack = QtWidgets.QPushButton(Calendar)
        self.BtnBack.setGeometry(QtCore.QRect(940, 110, 141, 61))
        self.BtnBack.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(214, 234, 248);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.BtnBack.setObjectName("BtnBack")
        self.BtnEdit = QtWidgets.QPushButton(Calendar)
        self.BtnEdit.setGeometry(QtCore.QRect(820, 620, 231, 41))
        self.BtnEdit.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(214, 234, 248);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.BtnEdit.setObjectName("BtnEdit")

        self.retranslateUi(Calendar)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        _translate = QtCore.QCoreApplication.translate
        Calendar.setWindowTitle(_translate("Calendar", "Form"))
        self.label.setText(_translate("Calendar", "Editar Información"))
        self.label_2.setText(_translate("Calendar", "Pekes"))
        self.lblNombre.setText(_translate("Calendar", "Nombre"))
        self.lblProge1.setText(_translate("Calendar", "Progenitor 1"))
        self.lblTfn2.setText(_translate("Calendar", "Teléfono"))
        self.lblTfn1.setText(_translate("Calendar", "Teléfono"))
        self.lblEmail.setText(_translate("Calendar", "Email"))
        self.lblProge2.setText(_translate("Calendar", "Progenitor 2"))
        self.lblOrigne.setText(_translate("Calendar", "Proviene de"))
        self.Public.setText(_translate("Calendar", "Público"))
        self.BtnBack.setText(_translate("Calendar", "Back"))
        self.BtnEdit.setText(_translate("Calendar", "Guardar edición"))
