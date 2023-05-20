import openpyxl
import mysql.connector



"""def getRowCount(file,sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return(sheet.max_row)

def getColumnCount(file,sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return(sheet.max_column)

def readData(file,sheetName,rownum,columnno):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.cell(row=rownum, column=columnno).value

def writeData(file,sheetName,rownum,columnno,data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    sheet.cell(row=rownum, column=columnno).value = data
    workbook.save(file)"""

def readData(db_name, tableName):
    mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port='3306',
    database=db_name,
        )

    mycursor = mydb.cursor()
    mycursor.execute('select * from '+tableName+'')
    table_data = mycursor.fetchall()

    return table_data


