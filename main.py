import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QListWidgetItem,  QMessageBox
from PyQt5.QtGui import QPixmap

import sqlite3
# from time import deltatime

#TODO Create an query to insert unusual_schedules
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)
        self.createDBs()

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

    def createDBs(self):
        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS Task( Nombre varchar(60), 
                completed VARCHAR(100), 
                date DATE, 
                hour VARCHAR(255)
                ); '''
            )
            db.commit()
            db.close()
        except Exception as e:
            print(e)
        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS "Unusual_task" (
	            "Description"	TEXT,
	            "Completed"	TEXT,
	            "Date"	DATE,
                "Hour"	TEXT);
                '''
                )
            db.commit()
            db.close()
        except Exception as e:
            print(e)
        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()
            cursor.execute(
                '''
            CREATE TABLE IF NOT EXISTS "Unusual_Schedules" (
	        "id"	INTEGER NOT NULL UNIQUE,
	        "description"	TEXT NOT NULL,
	        "sesion"	INTEGER,
	        PRIMARY KEY("id" AUTOINCREMENT));
                '''
                )
            db.commit()
            db.close()
        except Exception as e:
            print(e)
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

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainWindow.ui",self)
        self.citarScreen.clicked.connect(self.gotoCreateDate)
        self.createKidScreen.clicked.connect(self.gotocreate)
        self.agendaScreen.clicked.connect(self.gotoCreateAgendaScreen)
        self.computoScreen.clicked.connect(self.gotoCreatComputoScreen)
        self.infoScreen.clicked.connect(self.gotoCreateInfoScreen)
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
    def gotoCreateInfoScreen(self):
        infoScreen = CreateInfoScreen()
        widget.addWidget(infoScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoCreatComputoScreen(self):
        computoScreen = CreatComputoScreen()
        widget.addWidget(computoScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)



    
## ---------------------------------------------------------------------------

class CreateDateScreen(QDialog):
    def __init__(self):
        super(CreateDateScreen, self).__init__()
        loadUi("QCalendar.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        #self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)

        self.PopulateComboBox()
        self.BtnAddNew.clicked.connect(self.addNewDate)
        self.BtnAddSpecialDate.clicked.connect(self.addNewSpecialDate)

    def addNewDate(self):
        hourselected = str(self.timefield.text())
        kid = str(self.ComboPekes.currentText())
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        # if len(hourselected) ==0 or len(kid)==0 or dateSelected ==0: 
        #     self.lblFeedback.setText(f"Asegúrate de haber rellendao todos los campos")
        #else:       
        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()
            query = "INSERT INTO Task (Nombre, completed, date, hour) VALUES (?,?,?,?)"
            row = (kid, "NO", dateSelected, hourselected)
            cursor.execute(query, row)
            db.commit()
            self.lblFeedback.setText(f"Hemos añadido una cita con {kid} el {dateSelected} a las {hourselected}")
            db.close()
        except Exception as e:
                   # self.lblFeedback.setText(e)
                   print(e)
    
    def addNewSpecialDate(self):
        hourselected = str(self.timefield.text())
        description = self.SpecialDateDesc.text()
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()
            query = "INSERT INTO Unusual_task (Description, Completed, Date, Hour) VALUES (?,?,?,?)"
            row = (description, "NO", dateSelected, hourselected)
            cursor.execute(query, row)
            db.commit()
            self.lblFeedback.setText(f"Hemos añadido una cita con {description} el {dateSelected} a las {hourselected}")
            db.close()
        except Exception as e:
                   # self.lblFeedback.setText(e)
                   print(e)    
     
    def PopulateComboBox(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * From Pekes;"
        pekes = cursor.execute(query)
        for i in pekes:
            self.ComboPekes.addItem(str(i[0]))  

    def gotoMainWindow(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
## ---------------------------------------------------------------------------
class CreateAgendaScreen(QDialog):
    def __init__(self):
        super(CreateAgendaScreen, self).__init__()
        loadUi("Agenda.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)

    def calendarDateChanged(self):
        self.TaskListWidget.clear()
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * FROM Task WHERE completed = 'NO' AND date = ?"
        row = (dateSelected,)
        results = cursor.execute(query, row).fetchall()
        for result in results:
            item = QListWidgetItem(str(result))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(QtCore.Qt.Unchecked)
            self.TaskListWidget.addItem(item)
        
        query2 = "SELECT * FROM Unusual_task WHERE completed = 'NO' AND date = ?"
        row2 = (dateSelected,)
        results = cursor.execute(query2, row2).fetchall()
        for result in results:
            item = QListWidgetItem(str(result))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(QtCore.Qt.Unchecked)
            self.TaskListWidget.addItem(item)


    def saveChanges(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        for i in range(self.TaskListWidget.count()):
            item = self.TaskListWidget.item(i)
            print(f"El item es{item}")
            auxAtributos = item.text()  
            nombrePreparado = auxAtributos.replace("(","").replace(")","").replace("'","")
            tupla = nombrePreparado.split(",")
            nombre = tupla[0]
            fecha = tupla[2].strip()
            hora = tupla[3].strip()
            sesion = "{} --> {}".format(fecha,hora)
            # print("Nombre = {} Bool = {} Fecha = {} Hora = {}".format(tupla[0],tupla[1],tupla[2],tupla[3]))
            print('Checking')
            
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE Task SET completed = 'YES' WHERE Nombre = '{}' AND date = DATE('{}')".format(nombre,fecha)
            else:
                query = "UPDATE Task SET completed = 'NO' WHERE Nombre = '{}' AND date = DATE('{}')".format(nombre,fecha)
            # cursor.execute(query)
            # db.commit() 
            try:
                querySession = "INSERT INTO Schedules (nombre,sesion) VALUES ('{}','{}')".format(nombre,sesion)
                cursor.execute(query)
                db.commit() 
                cursor.execute(querySession)
                print("Query ejecutada")
                db.commit()
                #db.close()
            except Exception as e:
                print(e)
        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()


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
            query = '''
                    INSERT INTO Pekes (Nombre, Progenitor1, Tfn1, Progenitor2, Tfn2, Origen, Email, Cumpleaños) VALUES (?,?,?,?,?,?,?,?)
            '''
            row = (nombre,progenitor1,tfn1,progenirtor2,tfn2,origen,email,birthday)
            cursor.execute(query, row)
            db.commit()
            db.close()
        except Exception as e:
            print(e)

    def gotoMainWindow(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateInfoScreen(QDialog):
    def __init__(self):
        super(CreateInfoScreen, self).__init__()
        loadUi("Info.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        self.PopulateComboBox()
        self.BtnShow.clicked.connect(self.showComputo)
        self.BtnEdit.clicked.connect(self.editPeke)

    def PopulateComboBox(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * From Pekes;"
        pekes = cursor.execute(query)
        for i in pekes:
            self.ComboPekes.addItem(str(i[0])) 
    
    def gotoMainWindow(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def showComputo(self):
        db = sqlite3.connect("data.db")
        self.ShowListWidget.clear()
        kid = str(self.ComboPekes.currentText())
        cursor = db.cursor()
        query = "SELECT * FROM Schedules WHERE nombre = '{}'".format(kid)
        results = cursor.execute(query).fetchall()
        if len(results) == 0:
            item = QListWidgetItem(f"No hay registros para {kid}")
            self.ShowListWidget.addItem(item)
        else:
            for result in results:
              item = QListWidgetItem(str(result[2]))
              self.ShowListWidget.addItem(item)
        
        self.lblcount.setText(f"Has realizado {self.ShowListWidget.count()} horas a {kid}")

        query2 = "SELECT * FROM Pekes WHERE nombre = '{}'".format(kid)
        PekeInfo = cursor.execute(query2).fetchall()
        self.nombrefield.setText(PekeInfo[0][0])
        self.progenitor1field.setText(PekeInfo[0][1])
        self.tfn1field.setText(PekeInfo[0][2])
        self.progenitor2field.setText(PekeInfo[0][3])
        self.tfn2field.setText(PekeInfo[0][4])
       # self.birthdayfield.setDate(PekeInfo[0][5])
        self.Public.setText(PekeInfo[0][6])
        self.emailfield.setText(PekeInfo[0][7])

    def editPeke(self):
        print('Trying to edit')
        nombre = self.nombrefield.text()
        progenitor1 = self.progenitor1field.text()
        tfn1 = self.tfn1field.text()
        progenirtor2 = self.progenitor2field.text()
        tfn2 = self.tfn2field.text()
       # birthday = self.birthdayfield.text()
        if self.Public.isChecked() == True:
            origen = "Público"
        else:
            origen = "Privado"
        email = self.emailfield.text()

       # if len(email)==0 or len(nombre)==0 or len(progenitor1)==0 or len(tfn1)==0 or len(progenirtor2)==0 or len(tfn2)==0: 
        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()
            query =  "UPDATE PEKES SET Nombre = '{}', Progenitor1 = '{}', Tfn1 = '{}', Progenitor2 = '{}', Tfn2 = '{}', Origen = '{}', Email = '{}' WHERE Nombre = '{}'".format(nombre,progenitor1,tfn1,progenirtor2,tfn2,origen,email,nombre)

            # '''
            #         INSERT INTO Pekes (Nombre, Progenitor1, Tfn1, Progenitor2, Tfn2, Origen, Email)
            # '''

            #row = (nombre,progenitor1,tfn1,progenirtor2,tfn2,origen,email)
            cursor.execute(query)
            db.commit()
            print('Editting')
            db.close()
            messageBox = QMessageBox()
            messageBox.setText("Changes saved.")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
        except Exception as e:
                print(e)
# -----------------------


class CreatComputoScreen(QDialog):
    def __init__(self):
        super(CreatComputoScreen, self).__init__()
        loadUi("Computo.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        self.PopulateComboBox()
        self.BtnShow.clicked.connect(self.showComputo)
        self.BtnShowScheudeles.clicked.connect(self.showSchedules)
        self.BtnShowAllToDo.clicked.connect(self.showAllToDo)

    def PopulateComboBox(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * From Pekes;"
        pekes = cursor.execute(query)
        for i in pekes:
            self.ComboPekes.addItem(str(i[0])) 
    
    def gotoMainWindow(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def showComputo(self):
        print('Show Computo')
        db = sqlite3.connect("data.db")
        self.ShowListWidget.clear()
        kid = str(self.ComboPekes.currentText())
        cursor = db.cursor()
        query = "SELECT * FROM Schedules WHERE nombre = '{}'".format(kid)
        results = cursor.execute(query).fetchall()
        if len(results) == 0:
            item = QListWidgetItem(f"No hay registros para {kid}")
            self.ShowListWidget.addItem(item)
        else:
            for result in results:
              item = QListWidgetItem(str(result[2]))
              self.ShowListWidget.addItem(item)
        
       # self.lblcount.setText(f"Has realizado {self.ShowListWidget.count()} horas a {kid}")
        
    def showSchedules (self):
        self.ShowListWidget.clear()
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * FROM Schedules"
        results = cursor.execute(query).fetchall()
        for result in results:
              item = QListWidgetItem(str(result[1])+"---->" + str(result[2]))
              self.ShowListWidget.addItem(item)

    def showAllToDo(self):
        self.ShowListWidget.clear()
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * FROM Task WHERE completed = 'NO'"
        results = cursor.execute(query).fetchall()
        for result in results:
            item = QListWidgetItem(str(result))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(QtCore.Qt.Unchecked)
            self.ShowListWidget.addItem(item)

    # def calendarDateChanged(self):
    #     self.TaskListWidget.clear()
    #     dateSelected = self.calendarWidget.selectedDate().toPyDate()
    #     db = sqlite3.connect("data.db")
    #     cursor = db.cursor()
    #     query = "SELECT * FROM Task WHERE completed = 'NO' AND date = ?"
    #     row = (dateSelected,)
    #     results = cursor.execute(query, row).fetchall()
    #     for result in results:
    #         item = QListWidgetItem(str(result))
    #         item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
    #         if result[1] == "YES":
    #             item.setCheckState(QtCore.Qt.Checked)
    #         elif result[1] == "NO":
    #             item.setCheckState(QtCore.Qt.Unchecked)
    #         self.TaskListWidget.addItem(item)
        
    #     query2 = "SELECT * FROM Unusual_task WHERE completed = 'NO' AND date = ?"
    #     row2 = (dateSelected,)
    #     results = cursor.execute(query2, row2).fetchall()
    #     for result in results:
    #         item = QListWidgetItem(str(result))
    #         item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
    #         if result[1] == "YES":
    #             item.setCheckState(QtCore.Qt.Checked)
    #         elif result[1] == "NO":
    #             item.setCheckState(QtCore.Qt.Unchecked)
    #         self.TaskListWidget.addItem(item)
        
#------------------

    

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