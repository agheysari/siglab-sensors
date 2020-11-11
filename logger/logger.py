import serial
import time
from datetime import datetime
import csv

# #Read interval [sec]
interval = 3

# #Serial ports
port_ardu = "COM3"
# port_bath = "COM1"

# #Start serial connection
ser_ardu = serial.Serial(port_ardu, 9600)
# ser_bath = serial.Serial(port_bath, 9600)

start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    time.sleep(0.001)
    
    if elapsed_time > interval:
        ser_ardu.write("r".encode())
        # str(int(elapsed_time))
        read_ardu = ser_ardu.readline().decode('utf-8').strip()
        print("Time: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time))  + " | " + "Temperature: " + read_ardu + " degC ")
        with open('export.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time)), read_ardu])
        start_time = time.time()
        continue