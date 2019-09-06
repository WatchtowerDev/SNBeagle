#! /usr/bin/python
# -*- coding:utf-8 -*-

import sqlite3

def created_table():
    conn = sqlite3.connect('AWS_Sensor.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE SENSOR_VALUES
       (ID INTEGER PRIMARY KEY   AUTOINCREMENT,
       AIN0           INT    NOT NULL,
       AIN1           INT    NOT NULL,
       AIN2           INT    NOT NULL,
       AIN3           INT    NOT NULL,
       AIN4           INT    NOT NULL,
       AIN5           INT    NOT NULL,
       AIN6           INT    NOT NULL);''')
    print("database create successfully...")
    #conn.commit()
    conn.close()

def insert_values(dict_v):
    conn = sqlite3.connect('AWS_Sensor.db')
    c = conn.cursor()
    c.execute("INSERT INTO SENSOR_VALUES (AIN0,AIN1,AIN2,AIN3,AIN4,AIN5,AIN6) VALUES ('%d','%d','%d','%d','%d','%d','%d')" % tuple(dict_v))
    conn.commit()
    print("write data successfully...")
    conn.close()

def select_value():
    conn = sqlite3.connect('AWS_Sensor.db')
    c = conn.cursor()
    cursor = c.execute("SELECT * from SENSOR_VALUES")
    for row in cursor.fetchall():
        print("ID = ", row[0])
        print("AIN0 = ", row[1])
        print("AIN1 = ", row[2])
        print("AIN2 = ", row[3])
        print("AIN3 = ", row[4])
        print("AIN4 = ", row[5])
        print("AIN5 = ", row[6])
        print("AIN6 = ", row[7])
        #print("AIN6 = ", row[7], "\n")
        print("query data successfully...")
        conn.close()

def clear_value():
    conn = sqlite3.connect('AWS_Sensor.db')
    c = conn.cursor()
    cursor = c.execute("DELETE FROM SENSOR_VALUES")
    cursor = c.execute("update sqlite_sequence set seq = 0 where name = 'tablename'")
    cursor = c.execute("delete from sqlite_sequence where name = 'tablename'")
    cursor = c.execute("delete from sqlite_sequence")
    conn.commit()
    print("clean data successfully...")
    conn.close()
#created_table()
#insert_values(a)
#select_value()
#clear_value()