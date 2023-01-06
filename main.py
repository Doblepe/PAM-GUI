import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QListWidgetItem,  QMessageBox
from PyQt5.QtGui import QPixmap
import xlsxwriter

import sqlite3
# from time import deltatime

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("templates/login.ui",self)
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
        loadUi("templates/MainWindow.ui",self)
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
        loadUi("templates/QCalendar.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        #self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.PopulateComboBox()
        self.BtnAddNew.clicked.connect(self.addNewDate)
        self.BtnAddSpecialDate.clicked.connect(self.gotoSpecialDateScreen)


    def gotoSpecialDateScreen(self):
        specialDate = CreateSpecialDateScreen()
        widget.addWidget(specialDate)
        widget.setCurrentIndex(widget.currentIndex()+1)

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
            ret = QMessageBox.question(self, 'MessageBox', f"¿Estás segura de agendar una cita con {kid} el {dateSelected} a las {hourselected}", QMessageBox.Yes | QMessageBox.No )
            if ret == QMessageBox.Yes:  
                    db.commit()
                    self.lblFeedback.setText(f"Hemos añadido una cita con {kid} el {dateSelected} a las {hourselected}")
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
class CreateModifyDateScreen(QDialog):
    def __init__(self, query):
        super(CreateModifyDateScreen, self).__init__()
        loadUi("templates/QCalendarModifyDate.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        self.BtnAddNew.clicked.connect(self.addNewDate)
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        dateToChange = cursor.execute(query).fetchall()
        db.commit()
        item = QListWidgetItem(str(dateToChange))
        self.listWidget.addItem(item)
        db.close()
       

    def addNewDate(self):
        hourselected = str(self.timefield.text())
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
      
        # if len(hourselected) ==0 or len(kid)==0 or dateSelected ==0: 
        #     self.lblFeedback.setText(f"Asegúrate de haber rellendao todos los campos")
        #else:       
        try:
            for i in range(self.listWidget.count()):
                item = self.listWidget.item(i)
                auxAtributos = item.text()  
                nombrePreparado = auxAtributos.replace("(","").replace(")","").replace("'","").replace("[","")
                tupla = nombrePreparado.split(",")
                nombre = tupla[0]
                fecha = tupla[2].strip()
                db = sqlite3.connect("data.db")
                cursor = db.cursor()
                query = '''
                        UPDATE Task
                            SET date = ?,
                                Hour = ?
                            WHERE Nombre = ? AND date = ?
                '''
                row = (dateSelected, hourselected, nombre, fecha)
                #queryModify = "UPDATE Task SET date = CAST('{}' AS DATETIME) AND Hour = ('{}') WHERE Nombre = ('{}') AND date = DATE('{}');".format(dateSelected,hourselected,nombre, fecha)
                cursor.execute(query, row)
                db.commit()
                db.close()
                messageBox = QMessageBox()
                messageBox.setText("La cita ha sido cambiada.")
                messageBox.setStandardButtons(QMessageBox.Ok)
                messageBox.exec()
        except Exception as e:
                   self.lblFeedback.setText(e)
                   print(e)
       

    def gotoMainWindow(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateSpecialDateScreen(QDialog):
    def __init__(self):
        super(CreateSpecialDateScreen, self).__init__()
        loadUi("templates/QCalendarSpecialDate.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        self.BtnAddSpecialDate.clicked.connect(self.addNewSpecialDate)
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
## -------------------------------------------------------------------------
class CreateAgendaScreen(QDialog):
    def __init__(self):
        super(CreateAgendaScreen, self).__init__()
        loadUi("templates/Agenda.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.SpecialAgenda.clicked.connect(self.gotospecialAgenda)
        self.BtnchangeDate.clicked.connect(self.gotoCreateModifyDateScreen)
    

    def gotoCreateModifyDateScreen(self):
        for i in range(self.TaskListWidget.count()):
            item = self.TaskListWidget.item(i)
            auxAtributos = item.text()  
            nombrePreparado = auxAtributos.replace("(","").replace(")","").replace("'","")
            tupla = nombrePreparado.split(",")
            nombre = tupla[0]
            fecha = tupla[2].strip()
            hora = tupla[3].strip()
            sesion = "{} --> {}".format(fecha,hora)
            
        if item.checkState() == QtCore.Qt.Checked:
            query = "Select * FROM Task WHERE Nombre = '{}' AND date = DATE('{}')".format(nombre,fecha)
        #print(query)
            modifyDate = CreateModifyDateScreen(query)
            widget.addWidget(modifyDate)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def changeDate(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        for i in range(self.TaskListWidget.count()):
            item = self.TaskListWidget.item(i)
            auxAtributos = item.text()  
            nombrePreparado = auxAtributos.replace("(","").replace(")","").replace("'","")
            tupla = nombrePreparado.split(",")
            nombre = tupla[0]
            fecha = tupla[2].strip()
            hora = tupla[3].strip()
            sesion = "{} --> {}".format(fecha,hora)
            
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE Task SET completed = 'YES' WHERE Nombre = '{}' AND date = DATE('{}')".format(nombre,fecha)
            else:
                query = "UPDATE Task SET completed = 'NO' WHERE Nombre = '{}' AND date = DATE('{}')".format(nombre,fecha)
            try:
                querySession = "INSERT INTO Schedules (nombre,sesion) VALUES ('{}','{}')".format(nombre,sesion)
               # querySpecialSesion = "INSERT INTO Unusual_Schedules (description,sesion) VALUES ('{}','{}')".format(nombre,sesion)
                cursor.execute(query)
                cursor.execute(querySession)
                db.commit()
            except Exception as e:
                print(e)

   
    def gotospecialAgenda(self):
        specialAgenda = CreateSpecialAgendaScreen()
        widget.addWidget(specialAgenda)
        widget.setCurrentIndex(widget.currentIndex()+1)

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
        


    def saveChanges(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        ret = QMessageBox.question(self, 'MessageBox', "¿Estás segura de guardar estas citas?", QMessageBox.Yes | QMessageBox.No )
        if ret == QMessageBox.Yes:
            for i in range(self.TaskListWidget.count()):
                item = self.TaskListWidget.item(i)
                auxAtributos = item.text()  
                nombrePreparado = auxAtributos.replace("(","").replace(")","").replace("'","")
                tupla = nombrePreparado.split(",")
                nombre = tupla[0]
                fecha = tupla[2].strip()
                hora = tupla[3].strip()
                sesion = "{} --> {}".format(fecha,hora)
                # print("Nombre = {} Bool = {} Fecha = {} Hora = {}".format(tupla[0],tupla[1],tupla[2],tupla[3]))
                
                if item.checkState() == QtCore.Qt.Checked:
                    query = "UPDATE Task SET completed = 'YES' WHERE Nombre = '{}' AND date = DATE('{}')".format(nombre,fecha)
                    #UnusualQuery = "UPDATE Unusual_Task SET completed = 'YES' WHERE Description = '{}' AND date = DATE('{}')".format(nombre,fecha)
                else:
                    query = "UPDATE Task SET completed = 'NO' WHERE Nombre = '{}' AND date = DATE('{}')".format(nombre,fecha)
                    #UnusualQuery = "UPDATE Unusual_Task SET completed = 'NO' WHERE Description = '{}' AND date = DATE('{}')".format(nombre,fecha)
                # cursor.execute(query)
                # db.commit() 
                try:
                    querySession = "INSERT INTO Schedules (nombre,sesion) VALUES ('{}','{}')".format(nombre,sesion)
                    cursor.execute(query)
        
                    cursor.execute(querySession)
                    db.commit()
                except Exception as e:
                    print(e)
        self.TaskListWidget.clear()
        db.close()
        


    def gotoMainWindow(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

## -------------------------------------------------------------------------
class CreateSpecialAgendaScreen(QDialog):
    def __init__(self):
        super(CreateSpecialAgendaScreen, self).__init__()
        loadUi("templates/Special_Agenda.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)


    def calendarDateChanged(self):
        self.TaskListWidget.clear()
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
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
        ret = QMessageBox.question(self, 'MessageBox', "¿Estás segura de guardar estas citas?", QMessageBox.Yes | QMessageBox.No )
        if ret == QMessageBox.Yes:
            for i in range(self.TaskListWidget.count()):
                item = self.TaskListWidget.item(i)
                auxAtributos = item.text()  
                nombrePreparado = auxAtributos.replace("(","").replace(")","").replace("'","")
                tupla = nombrePreparado.split(",")
                nombre = tupla[0]
                fecha = tupla[2].strip()
                hora = tupla[3].strip()
                sesion = "{} --> {}".format(fecha,hora)
                # print("Nombre = {} Bool = {} Fecha = {} Hora = {}".format(tupla[0],tupla[1],tupla[2],tupla[3]))
                
                if item.checkState() == QtCore.Qt.Checked:
                # query = "UPDATE Task SET completed = 'YES' WHERE Nombre = '{}' AND date = DATE('{}')".format(nombre,fecha)
                    UnusualQuery = "UPDATE Unusual_Task SET completed = 'YES' WHERE Description = '{}' AND date = DATE('{}')".format(nombre,fecha)
                else:
                    #query = "UPDATE Task SET completed = 'NO' WHERE Nombre = '{}' AND date = DATE('{}')".format(nombre,fecha)
                    UnusualQuery = "UPDATE Unusual_Task SET completed = 'NO' WHERE Description = '{}' AND date = DATE('{}')".format(nombre,fecha)
                # cursor.execute(query)
                # db.commit() 
                try:
                # querySession = "INSERT INTO Schedules (nombre,sesion) VALUES ('{}','{}')".format(nombre,sesion)
                    querySpecialSesion = "INSERT INTO Unusual_Schedules (description,sesion) VALUES ('{}','{}')".format(nombre,sesion)
                    #cursor.execute(query)
                    cursor.execute(UnusualQuery)
                    cursor.execute(querySpecialSesion)
                # cursor.execute(querySession)
                    db.commit()
                except Exception as e:
                    print(e)
        db.close()



    def gotoMainWindow(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)


## -------------------------------------------------------------------------
class CreatekidScreen(QDialog):
    def __init__(self):
        super(CreatekidScreen, self).__init__()
        loadUi("templates/Createkid.ui",self)
        self.savekid.clicked.connect(self.savekidfunction)
        self.back.clicked.connect(self.gotoMainWindow)
    def savekidfunction(self):
        ret = QMessageBox.question(self, 'MessageBox', "¿Estás segura de guardar estos datos?", QMessageBox.Yes | QMessageBox.No )
        if ret == QMessageBox.Yes:
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
        loadUi("templates/Info.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        self.PopulateComboBox()
        self.BtnShow.clicked.connect(self.showComputo)
        self.BtnEdit.clicked.connect(self.gotoEditPeke)

    def gotoEditPeke(self):
        edittingpeke = CreateEdittingInfoScreen()
        widget.addWidget(edittingpeke)
        widget.setCurrentIndex(widget.currentIndex()+1)

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
        self.Public.setText(PekeInfo[0][5])
        self.emailfield.setText(PekeInfo[0][6])

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
            messageBox.setText("La información se ha cargado")
            messageBox.setStandardButtons(QMessageBox.information)
            messageBox.exec()
        except Exception as e:
                print(e)
# -----------------------
class CreateEdittingInfoScreen(QDialog):
    def __init__(self):
        super(CreateEdittingInfoScreen, self).__init__()
        loadUi("templates/Edit_info.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        self.PopulateComboBox()
        self.loadData()
        self.ComboPekes.currentTextChanged.connect(self.loadData)
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

    def loadData(self):
        db = sqlite3.connect("data.db")
        kid = str(self.ComboPekes.currentText())
        cursor = db.cursor()
        query2 = "SELECT * FROM Pekes WHERE nombre = '{}'".format(kid)
        PekeInfo = cursor.execute(query2).fetchall()
        for peke in PekeInfo:
            print(peke)

        self.nombrefield.setText(PekeInfo[0][0])
        self.progenitor1field.setText(PekeInfo[0][1])
        self.tfn1field.setText(PekeInfo[0][2])
        self.progenitor2field.setText(PekeInfo[0][3])
        self.tfn2field.setText(PekeInfo[0][4])
        self.Public.setText(PekeInfo[0][5])
        self.emailfield.setText(PekeInfo[0][6])

    def editPeke(self):
        db = sqlite3.connect("data.db")
        ret = QMessageBox.question(self, 'MessageBox', "¿Estás segura de los datos a modificar?", QMessageBox.Yes | QMessageBox.No )
        if ret == QMessageBox.Yes:
            kid = str(self.ComboPekes.currentText())
            print('Trying to edit')
            nombre = self.nombrefield.text()
            progenitor1 = self.progenitor1field.text()
            tfn1 = self.tfn1field.text()
            progenirtor2 = self.progenitor2field.text()
            tfn2 = self.tfn2field.text()
            if self.Public.isChecked() == True:
                origen = "Público"
            else:
                origen = "Privado"
            email = self.emailfield.text()
        # if len(email)==0 or len(nombre)==0 or len(progenitor1)==0 or len(tfn1)==0 or len(progenirtor2)==0 or len(tfn2)==0: 
            try:
                db = sqlite3.connect("data.db")
                cursor = db.cursor()
                query =  "UPDATE PEKES SET Nombre = '{}', Progenitor1 = '{}', Tfn1 = '{}', Progenitor2 = '{}', Tfn2 = '{}', Origen = '{}', Email = '{}' WHERE Nombre = '{}'".format(nombre,progenitor1,tfn1,progenirtor2,tfn2,origen,email,kid)
                print(query)
                cursor.execute(query)
                db.commit()
                db.close()
            except Exception as e:
                    print(e)




#-----------------------------------------------------------------------------------


class CreatComputoScreen(QDialog):
    def __init__(self):
        super(CreatComputoScreen, self).__init__()
        loadUi("templates/Computo.ui",self)
        self.BtnBack.clicked.connect(self.gotoMainWindow)
        self.PopulateComboBox()
        self.BtnShow.clicked.connect(self.showComputo)
        self.BtnShowScheudeles.clicked.connect(self.showSchedules)
        self.BtnShowAllToDo.clicked.connect(self.showAllToDo)
        #self.ComboPekes.currentTextChanged.connect(self.loadData)
        self.BtnShowUnusualScheudeles.clicked.connect(self.showUnusualSchedules)
        self.Btnexportxlsx.clicked.connect(self.exportXLSX)

    def exportXLSX(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * From Pekes;"
        pekes = cursor.execute(query)
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('Horas.xlsx')
        worksheet = workbook.add_worksheet(self.ComboMes.currentText())
       
        #Setting the schema
        header_cell = workbook.add_format({'bold': True, 'font_color': 'white', 'bg_color': 'rgb(214, 234, 248)'})
        worksheet.write(0, 0, 'Atención temprana', header_cell)
        worksheet.write(0, 1, 'Semana 1', header_cell)
        worksheet.write(0, 2, 'Semana 2', header_cell)
        worksheet.write(0, 3, 'Semana 3', header_cell)
        worksheet.write(0, 4, 'Semana 5', header_cell)
        worksheet.write(0, 5, 'Prescripción', header_cell)
        worksheet.write(0, 6, 'Realizadas', header_cell)
        worksheet.write(0, 7, 'No Realizadas', header_cell)
        worksheet.write(0, 8, 'Recuperadas', header_cell)
        # Privados
        worksheet.write(40, 0, 'PRIVADOS', header_cell)
        worksheet.write(40, 1, 'Semana 1', header_cell)
        worksheet.write(40, 2, 'Semana 2', header_cell)
        worksheet.write(40, 3, 'Semana 3', header_cell)
        worksheet.write(40, 4, 'Semana 5', header_cell)
        worksheet.write(40, 5, 'Prescripción - BONO', header_cell)
        worksheet.write(40, 6, 'Realizadas', header_cell)
        worksheet.write(40, 7, 'No Realizadas', header_cell)
        worksheet.write(40, 8, 'Recuperadas', header_cell)

   # Start from the first cell. Rows and columns are zero indexed.
        row = 1
        col = 0
        # Iterate over the data and write it out row by row.
        Atencion_temprana_list = []
        Privados_list = []
        for item in (pekes):
            if item[5] == 'Público':
                Atencion_temprana_list.append(item)
                worksheet.write(row, col, item[0])
                row += 1
            else:
                Privados_list.append(item)
       #Seteo para que empiece con los privados 
        row = 41
        for item in Privados_list:
            worksheet.write(row, col, item[0])
            row += 1
        
        query_all_schedules = "SELECT * FROM Schedules"
        results = cursor.execute(query_all_schedules).fetchall()
        sesiones_del_mes = []
        try: 
            row = 1
            col = 1
            for result in results:
                i = 0
                #Esta línea coge el mes de la cita y la compara con el mes seleccionado en el CB
                month = result[2][5] + result[2][6] 
                if month == str(self.ComboMes.currentText()):
                    sesiones_del_mes.append(result)
                    #Todas las sesinoes realizadas durante el mes
                else:
                    print('La cita es de otro mes')    
            print(f"{sesiones_del_mes} Sesiones del mes")
            print(f"{Atencion_temprana_list} Atención temprana")

            # for sesion in sesiones_del_mes:
            #     i+=1
            #     if Atencion_temprana_list[i][0] == sesiones_del_mes[i][1]:
            #         worksheet.write(row, col, sesiones_del_mes[i][2])
            #         col +=1
                
            #print(i)
               
        except Exception as e:
                    print(e)

 
        #worksheet.write(row, col + 1, cost)
        workbook.close()
        print('editting xmlsx')
    def PopulateComboBox(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * From Pekes;"
        pekes = cursor.execute(query)
        for i in pekes:
            self.ComboPekes.addItem(str(i[0])) 
        calendarmonthlist  = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
        for i in calendarmonthlist:
            self.ComboMes.addItem(i)
    
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
            try: 
                for result in results:
                    month = result[2][5] + result[2][6]
                    if month == str(self.ComboMes.currentText()):
                        item = QListWidgetItem(str(result[2]))
                        self.ShowListWidget.addItem(item)                    
            except Exception as e:
                    print(e)
                    
        
       
        
    def showSchedules (self):
        self.ShowListWidget.clear()
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * FROM Schedules"
        results = cursor.execute(query).fetchall()
        try: 
            for result in results:
                month = result[2][5] + result[2][6] 
                if month == str(self.ComboMes.currentText()):
                    item = QListWidgetItem(str(result[1])+"---->" + str(result[2]))
                    self.ShowListWidget.addItem(item)
                   
        except Exception as e:
                    print(e)
        self.lblcount.setText(f"En el mes {str(self.ComboMes.currentText())} has realizado {self.ShowListWidget.count()} sesiones")
    def showUnusualSchedules (self):
        self.ShowListWidget.clear()
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * FROM Unusual_Schedules"
        results = cursor.execute(query).fetchall()
        try: 
            for result in results:
                month = result[2][5] + result[2][6] 
                if month == str(self.ComboMes.currentText()):
                    item = QListWidgetItem(str(result[1])+"---->" + str(result[2]))
                    self.ShowListWidget.addItem(item)
                    
        except Exception as e:
                    print(e)
        self.lblcount.setText(f"En el mes {str(self.ComboMes.currentText())} has realizado {self.ShowListWidget.count()} coordinaciones ")
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
        
#------------------

    

# main
app = QApplication(sys.argv)
Login = LoginScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(Login)
widget.setFixedHeight(1080)
widget.setFixedWidth(1920)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")