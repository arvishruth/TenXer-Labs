import serial
import time

# Open serial connection
arduino_serial = serial.Serial(port="/dev/ttyAMA0", baudrate=9600, timeout=1)

try:
    # Send characters repeatedly
    message = "TenXer"
    while True:
        for char in message:
            arduino_serial.write(char.encode())
            time.sleep(0.1)
except KeyboardInterrupt:
    # Close serial connection
    arduino_serial.close()
