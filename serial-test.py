import serial

ser = serial.Serial('COM2', 115200)
if not ser.isOpen():
    ser.open()
print('com2 is open', ser.isOpen())


# ser.write('\x1b\x40'); # esc @ (init)
# ser.write('\x0a'); #line feed
# ser.write('\x0a'); #line feed
ser.write(str.encode('Hello World')); #text
#ser.write('Hello World'); #text
#ser.write('Hello World'); #text
#ser.write('Hello World'); #text
#ser.write('Hello World'); #text
#ser.write('\x0a'); #line feed
#ser.write('\x1d\x56\x42\x03'); #cut the paper