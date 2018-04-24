#!/usr/bin/env python

import os
import sys
import glob
from time import sleep
import datetime
from numpy import *

os.system('modprobe w1-gpio')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')
device_file=[0,1,2,3,4,5,6]

try:
    for i in [0,len(device_folder)-1]:
	device_file[i] = device_folder[i] + '/w1_slave'
except:
    print('0 0')
    sys.exit()

def read_temp_raw(i):
    f = open(device_file[i], 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(i):
    lines = read_temp_raw(i)
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw(i)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

try:
#    while True:
     todaydetail  =    datetime.datetime.today()
     print todaydetail.strftime('%Y/%m/%d %H:%M:%S'),
     for i in [0,len(device_folder)-1]:
       	print(device_folder[i].replace(base_dir,'')+' '+str(read_temp(i))+' deg '),
#       	sleep(1)
     print('')

except KeyboardInterrupt:
    pass
except:
     print('0 0')
