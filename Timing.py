from datetime import datetime, timedelta
import sqlite3
import pywhatkit


 # -------------------------------------- THIS CODE CONTAINS A BUCLE FOR SEARCHING DATES

def sendWhatsapp_proge1(queryFindPeke, hour):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    pekeInfo = cursor.execute(queryFindPeke)
    print(f"{hour} Hour")
    hourDate = hour[0] + hour[1]
    hourDate = int(hourDate)
    print(f"{hourDate} HourDate")
    minDate = hour[3] + hour[4]
    minDate = int(minDate)
    minDate = minDate + 3
    print(f"{minDate} Hourmin")
    for info in pekeInfo:
        print (info)
    try:
        tfn = info[2]
        progenitor1 =info[1]
        peke = info[0]
        pywhatkit.sendwhatmsg(
        phone_no="+34{}".format(tfn), 
        message="Hola {} mañana {} tiene una cita a las {}. Si no hay ningún inconveniente, *No hace falta responder a este mensaje*".format(progenitor1, peke, hour),
        time_hour=hourDate,
        time_min=minDate, wait_time= 30, tab_close=True, close_time= 50)
        print('Sending msg')
    except Exception as e:
        print(e)

def sendWhatsapp_proge2(queryFindPeke, hour):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    pekeInfo = cursor.execute(queryFindPeke)
    print(f"{hour} Hour")
    hourDate = hour[0] + hour[1]
    hourDate = int(hourDate)
    print(f"{hourDate} HourDate")
    minDate = hour[3] + hour[4]
    minDate = int(minDate)
    minDate = minDate + 4
    print(f"{minDate} Hourmin")
    for info in pekeInfo:
        print (info)
    try:
        tfn = info[4]
        progenitor2 =info[3]
        peke = info[0]
        pywhatkit.sendwhatmsg(
        phone_no="+34{}".format(tfn), 
        message="Hola {} mañana {} tiene una cita a las {}. Si no hay ningún inconveniente, *No hace falta responder a este mensaje*".format(progenitor2, peke, hour),
        time_hour=hourDate,
        time_min=minDate, wait_time= 30, tab_close=True, close_time= 50)
        print('Sending msg')
    except Exception as e:
        print(e)
    buscar_citas_dia_siguiente()

#print(f"Fecha actual es: {fecha_actual}")
def buscar_citas_dia_siguiente():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    query = "SELECT * FROM Task WHERE completed = 'NO'"
    results = cursor.execute(query).fetchall()
    Lista_de_citas = []
    open = True
    for result in results:
        print(result)
        formatted_date= str(result[2]) + " "+ result[3]
        Lista_de_citas.append(formatted_date)
    while open == True:
        ini_time_for_now = datetime.now()
        future_date_after_1_day = ini_time_for_now + \
                            timedelta(days = 1)
        future_date_after_1_day = datetime.strftime(future_date_after_1_day, '%Y-%m-%d %H:%M')
        print(future_date_after_1_day)

        print('Not yet ...')
        if future_date_after_1_day in Lista_de_citas:
            print('Yeah')
            x = future_date_after_1_day.split()
            date = x[0]
            hour = x[1]
            #query = "SELECT * FROM Task WHERE completed = 'NO'"
            if result[2] == date and result[3] == hour:
#                    #Getting the right moment 
                # try:
                #     ini_time_for_now = datetime.now()
                #     ini_time_for_now = datetime.strftime(ini_time_for_now, '%H:%M')
                #     hourDate = ini_time_for_now[0] + ini_time_for_now[1]
                #     hourDate = int(hourDate)
                #     minDate = ini_time_for_now[3] + ini_time_for_now[4]
                #     minDate = int(minDate)
                #     minDate = minDate + 2

                #     for i in range(1, len(pekeslist)):
                #             tfn = pekeslist[i][2]
                #             progenitor1 =pekeslist[i][1]
                #             peke = pekeslist[i][0]
                #             hora = citasList[i][3]
                #             pywhatkit.sendwhatmsg(
                #             phone_no="+34{}".format(tfn), 
                #             message="Hola {} mañana {} tiene una cita a las {}. Si no hay ningún inconveniente, *No hace falta responder a este mensaje*".format(progenitor1, peke, hora),
                #             time_hour=hourDate,
                #             time_min=minDate)
                #             print('Sending msg')
                # except Exception as e:
                #     print(e)

                peke = result[0]
                print(f"El nombre es {peke}")
               # queryFindDate = "SELECT * FROM Task WHERE Nombre = ('{}') AND hour = ('{}') AND date = ('{}') ".format(peke, hour,date)
                queryFindPeke = "SELECT * FROM Pekes WHERE Nombre = ('{}')".format(peke)
                sendWhatsapp_proge1(queryFindPeke, hour)
                sendWhatsapp_proge2(queryFindPeke, hour)
                

buscar_citas_dia_siguiente() 









# Using current time
# ini_time_for_now = datetime.now()

# future_date_after_1_day = ini_time_for_now + \
#                         timedelta(days = 1)
 

# future_date_after_1_day = datetime.strftime(future_date_after_1_day, '%Y-%m-%d %H:%M')


# def sendWhatsapp(queryFindPeke, hour):
#     db = sqlite3.connect("data.db")
#     cursor = db.cursor()
#     pekeInfo = cursor.execute(queryFindPeke)
#     print(f"{hour} Hour")
#     hourDate = hour[0] + hour[1]
#     hourDate = int(hourDate)
#     print(f"{hourDate} HourDate")
#     minDate = hour[3] + hour[4]
#     minDate = int(minDate)
#     minDate = minDate + 1
#     print(f"{minDate} Hourmin")
#     for info in pekeInfo:
#         print (info)
#     try:
#         tfn = info[2]
#         progenitor1 =info[1]
#         pywhatkit.sendwhatmsg(
#         phone_no="+34{}".format(tfn), 
#         message="Hola {} esto una prueba  con variables dinámicas y te ha tocado ser conejillo".format(progenitor1),
#         time_hour=hourDate,
#         time_min=minDate)
#         print('Sending msg')
#     except Exception as e:
#         print(e)
#     buscar_citas_dia_siguiente()

#print(f"Fecha actual es: {fecha_actual}")
# def buscar_citas_dia_siguiente():
#     ini_time_for_now = datetime.now()
#     future_date_after_1_day = ini_time_for_now + \
#                              timedelta(days = 1)
#     future_date_after_1_day = datetime.strftime(future_date_after_1_day, '%Y-%m-%d')
#     db = sqlite3.connect("data.db")
#     cursor = db.cursor()
#     query = "SELECT * FROM Task WHERE completed = 'NO' AND date = ?"
#     row = (future_date_after_1_day,)
#     results = cursor.execute(query, row).fetchall()
#     pekeslist = []
#     citasList = []
#     for result in results:
#         citasList.append(result)
#         queryFindPeke = "SELECT * FROM Pekes WHERE Nombre = ('{}')".format(result[0])
#         citados = cursor.execute(queryFindPeke)
#         for peke in citados:
#             pekeslist.append(peke)
    
    # print(f"{pekeslist} Son la pekelist")
    # print(f"{citasList} Son las citasList")

    # print(f"{citasList[0][3]} Hora de la primera cita")
    # print(f"{pekeslist[0][1]} Nombre del primer  peke")
#     try:
#         #Getting the right moment 
#         ini_time_for_now = datetime.now()
#         ini_time_for_now = datetime.strftime(ini_time_for_now, '%H:%M')
#         hourDate = ini_time_for_now[0] + ini_time_for_now[1]
#         hourDate = int(hourDate)
#         minDate = ini_time_for_now[3] + ini_time_for_now[4]
#         minDate = int(minDate)
#         minDate = minDate + 2
   

#         for i in range(1, len(pekeslist)):
#             tfn = pekeslist[i][2]
#             progenitor1 =pekeslist[i][1]
#             peke = pekeslist[i][0]
#             hora = citasList[i][3]
#             pywhatkit.sendwhatmsg(
#             phone_no="+34{}".format(tfn), 
#             message="Hola {} mañana {} tiene una cita a las {}. Si no hay ningún inconveniente, *No hace falta responder a este mensaje*".format(progenitor1, peke, hora),
#             time_hour=hourDate,
#             time_min=minDate)
#             print('Sending msg')
#     except Exception as e:
#         print(e)

  
# buscar_citas_dia_siguiente()
# import time 
# import pywhatkit
# import pyautogui
# from pynput.keyboard import Key, Controller

# keyboard = Controller()

# def send_whatsapp_message(msg: str):
#     try:
#         pywhatkit.sendwhatmsg_instantly(
#             phone_no="<phone-number>", 
#             message=msg,
#             tab_close=True
#         )

#         time.sleep(10)
#         pyautogui.click()
#         time.sleep(2)
#         keyboard.press(Key.enter)
#         keyboard.release(Key.enter)
#         print("Message sent!")
#     except Exception as e:
#         print(str(e))

    # try:
    #     for i in range(1,len(pekeslist)):
    #         for j in range(1,len(citasList)):
    #             tfn = pekeslist[i][2]
    #             progenitor1 =pekeslist[i][1]
    #             pekeName = pekeslist[i][0]
    #             hora = citasList[j][3]
    #             pywhatkit.sendwhatmsg(
    #             phone_no="+34{}".format(tfn), 
    #             message="Hola {} mañana {} tiene una cita a las {}. Si no hay ningún inconveniente, *No hace falta responder a este mensaje*".format(progenitor1, pekeName, hora),
    #             time_hour=19,
    #             time_min=26)
    #     print('Sending msg')
    # except Exception as e:
    #     print(e)


   

 # -------------------------------------- THIS CODE CONTAINS A BUCLE FOR SEARCHING DATES

 # def sendWhatsapp(queryFindPeke, hour):
#     db = sqlite3.connect("data.db")
#     cursor = db.cursor()
#     pekeInfo = cursor.execute(queryFindPeke)
#     print(f"{hour} Hour")
#     hourDate = hour[0] + hour[1]
#     hourDate = int(hourDate)
#     print(f"{hourDate} HourDate")
#     minDate = hour[3] + hour[4]
#     minDate = int(minDate)
#     minDate = minDate + 1
#     print(f"{minDate} Hourmin")
#     for info in pekeInfo:
#         print (info)
#     try:
#         tfn = info[2]
#         progenitor1 =info[1]
#         pywhatkit.sendwhatmsg(
#         phone_no="+34{}".format(tfn), 
#         message="Hola {} esto una prueba  con variables dinámicas y te ha tocado ser conejillo".format(progenitor1),
#         time_hour=hourDate,
#         time_min=minDate)
#         print('Sending msg')
#     except Exception as e:
#         print(e)
#     buscar_citas_dia_siguiente()

# #print(f"Fecha actual es: {fecha_actual}")
# def buscar_citas_dia_siguiente():
#     db = sqlite3.connect("data.db")
#     cursor = db.cursor()
#     query = "SELECT * FROM Task WHERE completed = 'NO'"
#     results = cursor.execute(query).fetchall()
#     Lista_de_citas = []
#     for result in results:
#         print(result)
#         formatted_date= str(result[2]) + " "+ result[3]
#         Lista_de_citas.append(formatted_date)
#     while True:
#         ini_time_for_now = datetime.now()
#         future_date_after_1_day = ini_time_for_now + \
#                             timedelta(days = 1)
#         future_date_after_1_day = datetime.strftime(future_date_after_1_day, '%Y-%m-%d %H:%M')
#         print(future_date_after_1_day)
#         print('Not yet ...')
#         if future_date_after_1_day in Lista_de_citas:
#             print('Yeah')
#             x = future_date_after_1_day.split()
#             date = x[0]
#             hour = x[1]
#             #query = "SELECT * FROM Task WHERE completed = 'NO'"
#             if result[2] == date and result[3] == hour:
#                 peke = result[0]
#                 print(f"El nombre es {peke}")
#                # queryFindDate = "SELECT * FROM Task WHERE Nombre = ('{}') AND hour = ('{}') AND date = ('{}') ".format(peke, hour,date)
#                 queryFindPeke = "SELECT * FROM Pekes WHERE Nombre = ('{}')".format(peke)
#                 sendWhatsapp(queryFindPeke, hour)
#                 break

# buscar_citas_dia_siguiente()  