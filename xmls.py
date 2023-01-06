import sqlite3,xlsxwriter
def exportXLSX():
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT * From Pekes;"
        pekes = cursor.execute(query)
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('Horas.xlsx')
        worksheet = workbook.add_worksheet('01')
       
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
        # Creo la cuenta de coordinaciones
        worksheet.write(60, 0, 'COORDINACIONES', header_cell)

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
        try:
            row = 0
            col = 1
            for peke in Atencion_temprana_list:
                query_by_name = "SELECT * FROM Schedules WHERE nombre = '{}'".format(peke[0])
                todaslascitasporname = cursor.execute(query_by_name)
                nombre_peke = peke[0]
                row += 1
                col = 1
                for cita in todaslascitasporname:
                    nombre_cita = cita[1]
                    month = cita[2][5] + cita[2][6] 
                    if month == '01' and nombre_peke == nombre_cita:
                        worksheet.write(row, col, cita[2])
                        col +=1
        except Exception as e:
            print(e)    
        try:
            row = 40
            col = 1
            for peke in Privados_list:
                query_by_name = "SELECT * FROM Schedules WHERE nombre = '{}'".format(peke[0])
                todaslascitasporname = cursor.execute(query_by_name)
                nombre_peke = peke[0]
                row += 1
                col = 1
                for cita in todaslascitasporname:
                    nombre_cita = cita[1]
                    month = cita[2][5] + cita[2][6] 
                    if month == '01' and nombre_peke == nombre_cita:
                        worksheet.write(row, col, cita[2])
                        col +=1
        except Exception as e:
            print(e)
        try:
            row = 60
            col = 0
            query = "SELECT * FROM Unusual_Schedules"
            results = cursor.execute(query).fetchall()
            for result in results:
                month = result[2][5] + result[2][6] 
                if month == '01':
                    row += 1 
                    worksheet.write(row, col, result[1])
        except Exception as e:
            print(e)

        workbook.close()   
        print('editting xmlsx')

exportXLSX()