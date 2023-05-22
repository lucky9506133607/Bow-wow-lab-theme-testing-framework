import openpyxl
import mysql.connector

import mysql.connector


def readData(db_name, query, params):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port='3306',
        database=db_name,
    )

    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute(query, params)
    table_data = mycursor.fetchall()

    return table_data
