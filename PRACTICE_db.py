# CRUD operations in mysql

import mysql.connector
import json

# connecting to db
try:
    db = mysql.connector.connect(
        host='localhost', user='root', database='sample_library')
    print("SUCCESS: Successfully connected to db")
except mysql.connector.Error as error:
    print("FAILED: An error occurred while connecting to db:\nError:", error)

# select and return records as json
try:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM BOOKS")
    # type(result)=list
    result = cursor.fetchall()
    # print as pretty json
    print("SUCCESS: records have been fetched successfully:\n",
          json.dumps(result, indent=3, sort_keys=True))
except mysql.connector.Error as error:
    print("FAILED: An error occurred while getting data:\nError message:",
          error.msg, "\nError code:", error.errno)

# update
try:
    query = "UPDATE WRITERS SET NAME = 'ASMAA' WHERE ID=1"
    cursor.execute(query)
    # commit changes
    db.commit()
    print("SUCCESS: DB is updated successfully")
except mysql.connector.Error as error:
    print("FAILED: An error occurred while updating the records:\nError message:",
          error.msg, "\nError code:", error.errno)

# insert
try:
    query = "INSERT INTO WRITERS (ID, NAME, SURNAME, BIRTHDATE) VALUES (NULL, 'Asmaa', 'Mirkhan', '1985-04-10')"
    cursor.execute(query)
    # commit changes
    db.commit()
    print("SUCCESS: record is inserted successfully")
except mysql.connector.Error as error:
    print("FAILED: An error occurred while inserting the record:\nError message:",
          error.msg, "\nError code:", error.errno)

# delete
try:
    query = "DELETE FROM WRITERS WHERE ID = 7"
    cursor.execute(query)
    # commit changes
    db.commit()
    print("SUCCESS: record is deleted successfully")
except mysql.connector.Error as error:
    print("FAILED: An error occurred while deleting the record:\nError message:",
          error.msg, "\nError code:", error.errno)
