import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        self.login.clicked.connect(self.gotoMainWindow)
        # if len(user)==0 or len(password)==0:
        #     self.error.setText("Please input all fields.")

        # else:
        #     conn = sqlite3.connect("shop_data.db")
        #     cur = conn.cursor()
        #     query = 'SELECT password FROM login_info WHERE username =\''+user+"\'"
        #     cur.execute(query)
        #     result_pass = cur.fetchone()[0]
        #     if result_pass == password:
        #         print("Successfully logged in.")
        #         self.error.setText("")
                
        #     else:
        #         self.error.setText("Invalid username or password")

    def gotoMainWindow(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainWindow.ui",self)
        self.citarScreen.clicked.connect(self.gotoCreateDate)
        self.createKidScreen.clicked.connect(self.gotocreate)
        self.agendaScreen.clicked.connect(self.gotoCreateAgendaScreen)

    def gotoCreateDate(self):
        createDate = CreateDateScreen()
        widget.addWidget(createDate)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotocreate(self):
        createKid = CreatekidScreen()
        widget.addWidget(createKid)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoCreateAgendaScreen(self):
        createCalendar = CreateAgendaScreen()
        widget.addWidget(createCalendar)
        widget.setCurrentIndex(widget.currentIndex() + 1)

## ---------------------------------------------------------------------------

class CreateDateScreen(QDialog):
    def __init__(self):
        super(CreateDateScreen, self).__init__()
        loadUi("QCalendar.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        #self.calendarDateChanged()
        self.BtnAddNew.clicked.connect(self.addNewDate)
        self.BtnPopulate.clicked.connect(self.PopulateComboBox)

    def calendarDateChanged(self):
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
     
    def gotoMainWindow(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def addNewDate(self):
        hourselected = str(self.timefield.text())
        kid = str(self.nombreField.text())
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        # try:
        #     db = sqlite3.connect("data.db")
        #     cursor = db.cursor()
        #     cursor.execute(
        #         '''CREATE TABLE IF NOT EXISTS Task( Nombre varchar(60) 
        #         PRIMARY KEY, 
        #         completed VARCHAR(100), 
        #         date DATE, 
        #         hour VARCHAR(255)
        #         ); '''
        #     )
        #     db.commit()
        #     print('TAbla creada')
        # except Exception as e:
        #     print(e)

        if len(hourselected) ==0 or len(kid)==0 or dateSelected ==0: 
            self.lblFeedback.setText(f"Asegúrate de haber rellendao todos los campos")
        else:       
            try:
                    self.lblFeedback.setText(f"Asegúrate de haber rellendao todos los campos")
                    db = sqlite3.connect("data.db")
                    cursor = db.cursor()
                    query = "INSERT INTO Task(Nombre, completed, date, hour) VALUES (?,?,?,?)"
                    row = (kid, "NO", dateSelected, hourselected)
                    cursor.execute(query, row)
                    db.commit()
                    self.lblFeedback.setText(f"Hemos añadido una cita con {kid} el {dateSelected} a las {hourselected}")
                    db.close()
            except Exception as e:
                    self.lblFeedback.setText(e)
    
    def PopulateComboBox(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * From Pekes;"
        pekes = cursor.execute(query)
        for i in pekes:
            print(i[0])

    
        # cita = kid + dateSelected + hourselected
        # print(str(cita))

## ---------------------------------------------------------------------------
class CreateAgendaScreen(QDialog):
    def __init__(self):
        super(CreateAgendaScreen, self).__init__()
        loadUi("Agenda.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        #self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
    
    def gotoMainWindow(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

## -------------------------------------------------------------------------
class CreatekidScreen(QDialog):
    def __init__(self):
        super(CreatekidScreen, self).__init__()
        loadUi("Createkid.ui",self)
        self.savekid.clicked.connect(self.savekidfunction)
        self.back.clicked.connect(self.gotoMainWindow)
    def savekidfunction(self):
        nombre = self.nombrefield.text()
        progenitor1 = self.progenitor1field.text()
        tfn1 = self.tfn1field.text()
        progenirtor2 = self.progenitor2field.text()
        tfn2 = self.tfn2field.text()
        birthday = self.birthdayfield.text()
        if self.Public.isChecked() == True:
            origen = "Público"
        else:
            origen = "Privado"
        email = self.emailfield.text()

        if len(email)==0 or len(nombre)==0 or len(progenitor1)==0 or len(tfn1)==0 or len(progenirtor2)==0 or len(tfn2)==0 or len(birthday)==0: 
            self.error.setText("Please fill in all inputs.")
        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS Pekes( Nombre varchar(60) 
                PRIMARY KEY, 
                Progenitor1 VARCHAR(100),
                Tfn1 VARCHAR(100),
                Progenitor2 VARCHAR(100),
                Tfn2 VARCHAR(100),
                Origen VARCHAR(100),
                Email VARCHAR(100),
                Cumpleaños DATE
                ); '''
            )
            db.commit()
        except Exception as e:
            print(e)
        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()
            query = '''
                    INSERT INTO Pekes (Nombre, Progenitor1, Tfn1, Progenitor2, Tfn2, Origen, Email, Cumpleaños) VALUES (?,?,?,?,?,?,?,?)
            '''
            row = (nombre,progenitor1,tfn1,progenirtor2,tfn2,origen,email,birthday)
            cursor.execute(query, row)
            db.commit()
            db.close()
        except Exception as e:
            print(e)


        # db = sqlite3.connect("data.db")
        #             cursor = db.cursor()
        #             query = "INSERT INTO Task(Nombre, completed, date, hour) VALUES (?,?,?,?)"
        #             row = (kid, "NO", dateSelected, hourselected)
        #             cursor.execute(query, row)
        #             db.commit()
        # elif password!=confirmpassword:
        #     self.error.setText("Passwords do not match.")
        # else:
        #     conn = sqlite3.connect("shop_data.db")
        #     cur = conn.cursor()

        #     user_info = [user, password]
        #     cur.execute('INSERT INTO login_info (username, password) VALUES (?,?)', user_info)

        #     conn.commit()
        #     conn.close()

    def gotoMainWindow(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

# class CreateKid(QDialog):
#     def __init__(self):
#         super(CreateKid, self).__init__()
#         loadUi("createkid.ui",self)
#        # self.image.setPixmap(QPixmap('placeholder.png'))
#     def gotoMainWindow(self):
#         calendar = MainWindow()
#         widget.addWidget(calendar)
#         widget.setCurrentIndex(widget.currentIndex()+1)


# main
app = QApplication(sys.argv)
Login = LoginScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(Login)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")