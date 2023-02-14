import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
for port, desc, hwid in ports:
    print("Port:", port)
    print("Description:", desc)
    print("Hardware ID:", hwid)
    print("")
