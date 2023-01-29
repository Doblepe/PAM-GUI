import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QListWidgetItem,  QMessageBox
from PyQt5.QtGui import QPixmap
import xlsxwriter
#import Timing


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
        if len(user)==0 or len(password)==0:
            self.error.setText("Please input all fields.")
            self.gotoMainWindow() #Acomodo esta parte de la función para no tener que logearme todas las veces

        else:
            conn = sqlite3.connect("data.db")
            cur = conn.cursor()
            query = "SELECT password FROM login_info WHERE username = '{}'".format(user)
            result = cur.execute(query).fetchone()[0]
            if result == password:
                 print("Successfully logged in.")
                 self.error.setText("")
            self.gotoMainWindow()
            # else:
            #     self.error.setText("Invalid username or password")

    def gotoMainWindow(self):
        main = MainWindow()
        main.adjustSize()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.adjustSize()

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
        except Exception as e:
            print(e)
        try:
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
        except Exception as e:
            print(e)
        try: 
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS "Schedules" (
	            "ID"	INTEGER NOT NULL UNIQUE,
	            "nombre"	TEXT NOT NULL,
	            "sesion"	TEXT NOT NULL,
	            PRIMARY KEY("ID" AUTOINCREMENT)
                )'''
            )
            db.commit()
        except Exception as e:
            print(e)
        try:
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
        except Exception as e:
            print(e)
        try:
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS Pekes( Nombre varchar(60) 
                PRIMARY KEY, 
                Progenitor1 VARCHAR(100),
                Tfn1 VARCHAR(100),
                Progenitor2 VARCHAR(100),
                Tfn2 VARCHAR(100),
                Origen VARCHAR(100),
                Email VARCHAR(100),
                h_asignadas VARCHAR(100)
                ); '''
            )
            db.commit()
        except Exception as e:
            print(e)

        try: 
            cursor.execute('''CREATE TABLE IF NOT EXISTS "login_info" (
	            "username"	VARCHAR(100),
	            "password"	VARCHAR(100),
	            PRIMARY KEY("username"));''')
            db.commit()
        
        
            db.close()
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
        self.BtnIschecked.clicked.connect(self.is_checked)

    def is_checked(self):
        if self.activate_whats.isChecked() == True:
            messageBox = QMessageBox()
            messageBox.setText("La función de avisar está ACTIVADA")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            # import Timing
            # Timing.buscar_citas_dia_siguiente()
        else:
            messageBox = QMessageBox()
            messageBox.setText("La función de avisar está DESACTIVADA. Usa el módulo llamado TIMING.")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()

    def gotoCreateDate(self):
        createDate = CreateDateScreen()
        widget.addWidget(createDate)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.adjustSize()
    def gotocreate(self):
        createKid = CreatekidScreen()
        widget.addWidget(createKid)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.adjustSize()
    def gotoCreateAgendaScreen(self):
        createCalendar = CreateAgendaScreen()
        widget.addWidget(createCalendar)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.adjustSize()
    def gotoCreateInfoScreen(self):
        infoScreen = CreateInfoScreen()
        widget.addWidget(infoScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.adjustSize()
    def gotoCreatComputoScreen(self): 
        computoScreen = CreatComputoScreen()
        widget.addWidget(computoScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.adjustSize()

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
        # hourselected = str(self.timefield.text())
        # kid = str(self.ComboPekes.currentText())
        # dateSelected = self.calendarWidget.selectedDate().toPyDate()
        # self.lblFeedback.setText(f"Programar:(Con {kid} el {dateSelected} a las {hourselected})")
        


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
            ret = QMessageBox.question(self, 'MessageBox', f"¿Estás segura de agendar una Coordinación con {description} el {dateSelected} a las {hourselected}", QMessageBox.Yes | QMessageBox.No )
            if ret == QMessageBox.Yes:  
                db = sqlite3.connect("data.db")
                cursor = db.cursor()
                query = "INSERT INTO Unusual_task (Description, Completed, Date, Hour) VALUES (?,?,?,?)"
                row = (description, "NO", dateSelected, hourselected)
                cursor.execute(query, row)
                db.commit()
                db.close()
        except Exception as e:
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
                    query = "UPDATE Task SET completed = 'YES' WHERE Nombre = '{}' AND date = DATE('{}') AND hour = '{}'".format(nombre,fecha,hora)
                else:
                    query = "UPDATE Task SET completed = 'NO' WHERE Nombre = '{}' AND date = DATE('{}') AND hour = '{}'".format(nombre,fecha, hora)
                try:
                    querySession = "INSERT INTO Schedules (nombre,sesion) VALUES ('{}','{}')".format(nombre,sesion)
                    cursor.execute(query)
        
                    cursor.execute(querySession)
                    db.commit()
                except Exception as e:
                    print(e)
        self.TaskListWidget.clear()
        self.calendarDateChanged()
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
                
                if item.checkState() == QtCore.Qt.Checked:
                    UnusualQuery = "UPDATE Unusual_Task SET completed = 'YES' WHERE Description = '{}' AND date = DATE('{}')".format(nombre,fecha)
                else:
                    UnusualQuery = "UPDATE Unusual_Task SET completed = 'NO' WHERE Description = '{}' AND date = DATE('{}')".format(nombre,fecha)
                try:
                    querySpecialSesion = "INSERT INTO Unusual_Schedules (description,sesion) VALUES ('{}','{}')".format(nombre,sesion)

                    cursor.execute(UnusualQuery)
                    cursor.execute(querySpecialSesion)
  
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
        self.comboPublic.addItem("Público")
        self.comboPublic.addItem("Privado")
    def savekidfunction(self):
        ret = QMessageBox.question(self, 'MessageBox', "¿Estás segura de guardar estos datos?", QMessageBox.Yes | QMessageBox.No )
        if ret == QMessageBox.Yes:
            nombre = self.nombrefield.text()
            progenitor1 = self.progenitor1field.text()
            tfn1 = self.tfn1field.text()
            progenirtor2 = self.progenitor2field.text()
            tfn2 = self.tfn2field.text()
            origen = self.comboPublic.currentText()
            email = self.emailfield.text()
            h_asignadas = self.asignacionfield.text()

            if len(email)==0 or len(nombre)==0 or len(progenitor1)==0 or len(tfn1)==0 or len(progenirtor2)==0 or len(tfn2)==0 or len(h_asignadas)==0: 
                self.error.setText("Por favor, rellena todos los campos")

            try:
                db = sqlite3.connect("data.db")
                cursor = db.cursor()
                query = '''
                        INSERT INTO Pekes (Nombre, Progenitor1, Tfn1, Progenitor2, Tfn2, Origen, Email, h_asignadas) VALUES (?,?,?,?,?,?,?,?)
                '''
                row = (nombre,progenitor1,tfn1,progenirtor2,tfn2,origen,email,h_asignadas)
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
        self.BtnDarAlta.clicked.connect(self.darAlta)

    def darAlta(self):
        db = sqlite3.connect("data.db")
        kid = str(self.ComboPekes.currentText())
        cursor = db.cursor()
        ret = QMessageBox.question(self, 'MessageBox', f"¿Estás segura de dar el alta a {kid}? Sus datos se eliminarán de la DB", QMessageBox.Yes | QMessageBox.No )
        if ret == QMessageBox.Yes:
            queryalta = "DELETE FROM Pekes WHERE nombre = '{}'".format(kid)
            cursor.execute(queryalta).fetchall()
            db.commit()
            db.close()
        self.PopulateComboBox()

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
        self.comboPublic.setText(PekeInfo[0][5])
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
            query =  "UPDATE PEKES SET Nombre = '{}', Progenitor1 = '{}', Tfn1 = '{}', Progenitor2 = '{}', Tfn2 = '{}', Origen = '{}', Email = '{}', h_asginadas = '{}' WHERE Nombre = '{}'".format(nombre,progenitor1,tfn1,progenirtor2,tfn2,origen,email,nombre)

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
        self.comboPublic.addItem("Público")
        self.comboPublic.addItem("Privado")


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
        self.comboPublic.setValue(PekeInfo[0][5])
        self.emailfield.setText(PekeInfo[0][6])
        self.asignacionfield.setText(PekeInfo[0][7])

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
            origen = self.comboPublic.currentText()
            email = self.emailfield.text()
            h_asignadas = self.asignacionfield.text()
        # if len(email)==0 or len(nombre)==0 or len(progenitor1)==0 or len(tfn1)==0 or len(progenirtor2)==0 or len(tfn2)==0: 
            try:
                db = sqlite3.connect("data.db")
                cursor = db.cursor()
                query =  "UPDATE PEKES SET Nombre = '{}', Progenitor1 = '{}', Tfn1 = '{}', Progenitor2 = '{}', Tfn2 = '{}', Origen = '{}', Email = '{}', h_asignadas = '{}' WHERE Nombre = '{}'".format(nombre,progenitor1,tfn1,progenirtor2,tfn2,origen,email, h_asignadas, kid)
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
        ret = QMessageBox.question(self, 'MessageBox', f"Los datos se sobreescribirán. Estás en el mes{(self.ComboMes.currentText())}. ¿Quieres continuar? ", QMessageBox.Yes | QMessageBox.No )
        if ret == QMessageBox.Yes:
                db = sqlite3.connect("data.db")
                cursor = db.cursor()
                query = "SELECT * From Pekes;"
                pekes = cursor.execute(query)
                # Create a workbook and add a worksheet.
                workbook = xlsxwriter.Workbook('Horas.xlsx')
                worksheet = workbook.add_worksheet()
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

                # print(len(Atencion_temprana_list))
                lastRowAtencionTempranalist = len(Atencion_temprana_list)
                # Setting the schema
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
                # # Seteo para que empiece con los privados
                RowPrivadoslist = lastRowAtencionTempranalist + 4
                firstPrivadosRow = 0
                firstPrivadosRow = RowPrivadoslist
                worksheet.write(RowPrivadoslist, 0, 'PRIVADOS', header_cell)
                worksheet.write(RowPrivadoslist, 1, 'Semana 1', header_cell)
                worksheet.write(RowPrivadoslist, 2, 'Semana 2', header_cell)
                worksheet.write(RowPrivadoslist, 3, 'Semana 3', header_cell)
                worksheet.write(RowPrivadoslist, 4, 'Semana 5', header_cell)
                worksheet.write(RowPrivadoslist, 5, 'Prescripción - BONO', header_cell)
                worksheet.write(RowPrivadoslist, 6, 'Realizadas', header_cell)
                worksheet.write(RowPrivadoslist, 7, 'No Realizadas', header_cell)
                worksheet.write(RowPrivadoslist, 8, 'Recuperadas', header_cell)
                for item in Privados_list:
                    RowPrivadoslist += 1
                    worksheet.write(RowPrivadoslist, col, item[0])

                # Sumatorio de los públicos
                worksheet.write_formula((lastRowAtencionTempranalist+1), 6,'=SUMA(G2:G{})'.format(lastRowAtencionTempranalist + 1), header_cell)
                worksheet.write((lastRowAtencionTempranalist + 1), 5, 'Horas/Mes', header_cell)
                worksheet.write_formula((lastRowAtencionTempranalist + 2 ), 6, '=G{}*40'.format(lastRowAtencionTempranalist+2), header_cell)
                worksheet.write((lastRowAtencionTempranalist + 2), 5, 'TOTAL', header_cell)
                total_AT_Row = 0
                total_AT_Row = lastRowAtencionTempranalist + 1

                # Sumatorio de los privados
                worksheet.write_formula((RowPrivadoslist + 1), 6,'=SUMA(G{}:G{})'.format(firstPrivadosRow + 2, RowPrivadoslist + 1), header_cell)
                worksheet.write((RowPrivadoslist + 1), 5, 'Horas/Mes Privadas', header_cell)
                worksheet.write_formula((RowPrivadoslist+2), 6, '=G{}*45'.format(RowPrivadoslist + 2), header_cell)
                worksheet.write((RowPrivadoslist + 2), 5, 'TOTAL', header_cell)

                total_privados_row = 0
                total_privados_row = RowPrivadoslist + 1

                try:
                    row = 0
                    col = 1
                    for peke in Atencion_temprana_list:
                                query_by_name = "SELECT * FROM Schedules WHERE nombre = '{}'".format(
                                    peke[0])
                                todaslascitasporname = cursor.execute(query_by_name)
                                nombre_peke = peke[0]
                                row += 1
                                col = 1
                                for cita in todaslascitasporname:
                                    nombre_cita = cita[1]
                                    month = cita[2][5] + cita[2][6]
                                    if month == (self.ComboMes.currentText()) and nombre_peke == nombre_cita:
                                        worksheet.write(row, col, cita[2])
                                        col += 1
                                worksheet.write(row, 6, col - 1)
                except Exception as e:
                        print(e)
                try:
                        row = RowPrivadoslist - len(Privados_list)
                        col = 1
                        for peke in Privados_list:
                                query_by_name = "SELECT * FROM Schedules WHERE nombre = '{}'".format(
                                    peke[0])
                                todaslascitasporname = cursor.execute(query_by_name)
                                nombre_peke = peke[0]
                                row += 1
                                col = 1
                                for cita in todaslascitasporname:
                                    nombre_cita = cita[1]
                                    month = cita[2][5] + cita[2][6]
                                    if month == (self.ComboMes.currentText()) and nombre_peke == nombre_cita:
                                        worksheet.write(row, col, (cita[2]))
                                        col += 1
                                worksheet.write(row, 6, col - 1)
                except Exception as e:
                        print(e)
                # Creo la cuenta de coordinaciones
                coordinacionesRow = 0
                coordinacionesRow = RowPrivadoslist + 4
                worksheet.write(coordinacionesRow, 0, 'COORDINACIONES', header_cell)
                try:
                    row = coordinacionesRow
                    col = 0
                    query = "SELECT * FROM Unusual_Schedules"
                    results = cursor.execute(query).fetchall()
                    for result in results:
                        month = result[2][5] + result[2][6]
                        if month == (self.ComboMes.currentText()):
                            row += 1
                            worksheet.write(row, col, result[1])
                            worksheet.write(row, col+1, 36.28)
                except Exception as e:
                    print(e)
                # # Sumatorio de coordinaciones
                worksheet.write_formula(row+1, 1, '=SUMA(B{}:B{})'.format(coordinacionesRow+1, row+1), header_cell)
                worksheet.write(row+1, 0, 'TOTAL DE COORDINACIONES', header_cell)
                total_Coordinacionesrow = 0
                total_Coordinacionesrow = row + 1

                # # Final result
                worksheet.write(3, 10, 'Total generado', header_cell)
                worksheet.write_formula(3, 11, '=G{}+G{}+B{}'.format(total_privados_row + 1, total_AT_Row + 1, total_Coordinacionesrow + 1), header_cell)
                worksheet.write(4, 10, '50%')
                worksheet.write(4, 11, '=L4/2')
                worksheet.write(5, 10, '-15%')
                worksheet.write(6, 10, 'TOTAL EUR')
                worksheet.write_formula(6, 11, '=L4-L5', header_cell)
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
Login.adjustSize()
widget = QtWidgets.QStackedWidget()
widget.addWidget(Login)
widget.setFixedHeight(715)
widget.setFixedWidth(1120)
widget.show()
widget.adjustSize()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")