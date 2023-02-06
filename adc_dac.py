import time
from Adafruit_ADS1x15 import ADS1115
from Adafruit_MCP4725 import MCP4725

adc=Adafruit_ADS1x15.ADS1X15()
dac = Adafruit_MCP4725.MCP4725(address=0x60)

x=float(input("Enter applicable voltage, 0 to 4 volts \n"));
x=int(x*4096/5)
dac.set_voltage(x)

GAIN=1

values= [0]*4

values[0] = adc.read_adc(0, gain=GAIN)
val= int('| {0:>6} |' .format(*values).replace('|', ''))
volt= (val/2**15)*4.096
print("dac reading =", val)
print(volt, 'volts')
