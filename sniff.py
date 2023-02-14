import serial
import time

# Open serial connection
ser = serial.Serial("/dev/ttyUSB0", baudrate=9600)

# Read data from Arduino
while True:
    read_text = ser.read()
    print(read_text)
    