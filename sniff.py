import serial
while True:
 ser=serial.Serial("/dev/ttyAMA0",baudrate=9600)
 readText = ser.readline()
 print(readText)
