#
# Matt Schultz
# 2-18-2019
# First try with python code to take regular data from 34970a datalogger.
# Set your options here in the code (to keep it as simiple as possible). 
# Import the csv file into "Excel" or "Calc" to graph and manipulate data. 
#

import visa
import time

delay = 1 # Number of seconds between scans
loops = 5 # Number of times to do the loop
myfile = open('mydata.csv','a') # mydata.csv will be the output file name


rm = visa.ResourceManager()
daq = rm.open_resource('ASRL/dev/ttyUSB0::INSTR') #Change this to USB0 or 1 or 2... as needed


myfile.write(daq.query("SYST:DATE?")) # puts date stamp in the output file from the logger
myfile.write(daq.query("SYST:TIME?")) # puts time stamp in the output file from the logger

print(daq.query("*IDN?"))  # Show logger information in the terminal

print('Scan list includes...')
#Choose some or none of the following scan lists:

#daq.write("CONF:VOLT:DC 10,0.001,(@101:110)") # Proven works, try first.
daq.write("CONF:TEMP THER,10000,1,0.01,(@111:116)")# Proven works, include daq.write("UNIT:...)
daq.write("UNIT:TEMP F,(@111:116)")
#daq.write("CONF:RES AUTO,DEF,(@111:116)") # Proven works.
#daq.write("CONF:VOLT:DC 10,0.001,(@101:110)") # Change and make your own
#daq.write("CONF:VOLT:DC 10,0.001,(@101:110)") # Change and make your own
#


print(daq.query("ROUT:SCAN?")) # show scan list in the terminal
print(daq.query("UNIT:TEMP?")) # shows temp units in the terminal (F,C,or K) if needed.
print('Delay between scans is', delay, 'seconds') 


for i in range(loops):
    myfile.write(daq.query("READ?")) #Sends line of data to csv file
    time.sleep(delay) #seconds to sleep between scans
    print('Scanned',i+1,'of', loops) # Countdown on terminal, if you ^C out the previous data should still be in the file.

myfile.close()
print ('Finished with scans')

#END

