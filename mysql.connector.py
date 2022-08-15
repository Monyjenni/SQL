# importing required libraries

import mysql.connector

  

dataBase = mysql.connector.connect(
  # the username of our sql

  host ="localhost",

  user ="root",
  #here the password is blank because it is developed for free.

  passwd =""
)
 

print(dataBase)

  
# Disconnecting from the server
dataBase.close()