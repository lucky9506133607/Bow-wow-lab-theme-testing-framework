import openpyxl
import mysql.connector


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