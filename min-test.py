from escpos import SerialConnection
from escpos.impl.epson import GenericESCPOS

conn = SerialConnection.create('COM5:9600,8,1,N')
printer = GenericESCPOS(conn)
printer.init()
printer.text('----> Printer Test')