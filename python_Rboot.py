#! /usr/bin/python
# -*- coding:utf-8 -*-


import time
import csv
import threading
from bbio import *
from imu_demo import *
from s3update import *
from sqlite3_demo import *

row = []
vals_dict = {}
sensor_r = 10000
pins = ['AIN0','AIN1','AIN2','AIN3','AIN4','AIN5','AIN6']

def setup():
  pass

def toRolts(datas):
  reading = (4095 / datas)  - 1
  #reading = (4096 / datas)  - 1
  reading = sensor_r / reading
  return reading

# Save data to .csv file
def write_data(dict_v):
  for data in dict_v.values():
    row.append(data)
    rows = [row]
  with open('valu_datas.csv','a+') as fp:
    f_csv = csv.writer(fp)
    f_csv.writerows(rows)

def loop():
  for pin in pins:
    val = anologRead(pin)

    #Sensor Resistantce Algorithm
    #voltage = toRolts(val)
    voltage = inVolts(val)
    vals_dict[pin] = voltage
  print(vals_dict)
  # Write to .db file
  insert_values(vals_dict)

# create .db database, if database already exists, commnent next line code
#created_table()
# loop starts:
#run(setup, loop)
# execute functions in imu_demo.py, read IMU data
#go_start()
# execute functions in s3update,py, upload files to AWS
#go_main()

threads = []
threads.append(threading.Thread(target=go_start))
threads.append(threading.Thread(target=run,args=(setup,loop,)))
#threads.append(threading.Thread(target=start_hrv))

if __name__ == '__main__':
    for t in threads:
        t.start()