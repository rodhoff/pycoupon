import os, serial
import pty, tty
from termios import *

master, slave = pty.openpty()
s_name = os.ttyname(slave)

ser = serial.Serial('COM2')

# To Write to the device
ser.write('Your text')

# To read from the device
os.read(master,1000)