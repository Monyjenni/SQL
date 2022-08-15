# importing required libraries

import mysql.connector

  

dataBase = mysql.connector.connect(

  host ="localhost",

  user ="root",

  passwd =""
  
  database= "hdsd"
)
 
# preparing a cursor object

cursorObject = dataBase.cursor()
 
# creating database

cursorObject.execute("CREATE DATABASE hdsd")
studentRecord = """ Create table student
                    name
                """
cursorObject.excute(studentRecord)

dataBase.close()
                