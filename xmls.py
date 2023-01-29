import sqlite3,xlsxwriter
def exportXLSX():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    query = "SELECT * From Pekes;"
    pekes = cursor.execute(query)
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Horas.xlsx')
    worksheet = workbook.add_worksheet('01')
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


    #print(len(Atencion_temprana_list))
    lastRowAtencionTempranalist = len(Atencion_temprana_list)
    # Setting the schema
    header_cell = workbook.add_format(
        {'bold': True, 'font_color': 'white', 'bg_color': 'rgb(214, 234, 248)'})
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
    worksheet.write_formula((lastRowAtencionTempranalist+1), 6,'=SUMA(G2:G{})'.format(lastRowAtencionTempranalist +1), header_cell)
    worksheet.write((lastRowAtencionTempranalist +1), 5, 'Horas/Mes', header_cell)
    worksheet.write_formula((lastRowAtencionTempranalist +2 ), 6, '=G{}*40'.format(lastRowAtencionTempranalist+2), header_cell)
    worksheet.write((lastRowAtencionTempranalist + 2), 5, 'TOTAL', header_cell)
    total_AT_Row = 0
    total_AT_Row = lastRowAtencionTempranalist +1
   
    # Sumatorio de los privados
    worksheet.write_formula((RowPrivadoslist + 1), 6,'=SUMA(G{}:G{})'.format(firstPrivadosRow + 2, RowPrivadoslist +1), header_cell)
    worksheet.write((RowPrivadoslist +1), 5, 'Horas/Mes Privadas', header_cell)
    worksheet.write_formula((RowPrivadoslist+2), 6, '=G{}*45'.format(RowPrivadoslist +2), header_cell)
    worksheet.write((RowPrivadoslist + 2), 5, 'TOTAL', header_cell)

    total_privados_row = 0
    total_privados_row = RowPrivadoslist +1

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
                        if month == ('01') and nombre_peke == nombre_cita:
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
                    print(row)
                    col = 1
                    for cita in todaslascitasporname:
                        nombre_cita = cita[1]
                        month = cita[2][5] + cita[2][6]
                        if month == ('01') and nombre_peke == nombre_cita:
                            worksheet.write(row, col, (cita[2]))
                            col += 1
                    worksheet.write(row, 6, col - 1)
    except Exception as e:
                print(e)
        # Creo la cuenta de coordinaciones
    coordinacionesRow = 0
    coordinacionesRow = RowPrivadoslist +4
    worksheet.write(coordinacionesRow, 0, 'COORDINACIONES', header_cell)
    try:
        row = coordinacionesRow
        col = 0
        query = "SELECT * FROM Unusual_Schedules"
        results = cursor.execute(query).fetchall()
        for result in results:
            month = result[2][5] + result[2][6]
            if month == ('01'):
                row += 1
                worksheet.write(row, col, result[1])
                worksheet.write(row, col+1, 36.28)
    except Exception as e:
        print(e)
    # # Sumatorio de coordinaciones
    worksheet.write_formula(row+1, 1, '=SUMA(B{}:B{})'.format(coordinacionesRow+1, row+1), header_cell)
    worksheet.write(row+1, 0,'TOTAL DE COORDINACIONES', header_cell)
    total_Coordinacionesrow = 0
    total_Coordinacionesrow = row +1


    # # Final result
    worksheet.write(3, 10, 'Total generado', header_cell)
    worksheet.write_formula(3, 11, '=G{}+G{}+B{}'.format(total_privados_row +1, total_AT_Row +1, total_Coordinacionesrow +1), header_cell)
    worksheet.write(4, 10, '50%')
    worksheet.write(4, 11, '=L4/2')
    worksheet.write(5, 10, '-15%')
    worksheet.write(6, 10, 'TOTAL EUR')
    worksheet.write_formula(6, 11, '=L4-L5', header_cell)


    workbook.close()
exportXLSX()
print('editting xmlsx')
