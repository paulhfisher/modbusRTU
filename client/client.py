# libraries
from pymodbus.client import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.transaction import ModbusRtuFramer
from pymodbus.constants import Defaults as ModbusDefaults

import logging
import time
# FORMAT = ('%(message)-15s')
# logging.basicConfig(format=FORMAT)
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

# declaration of client and connexion

reading = 0
client = ModbusSerialClient(method='rtu', port = '/dev/ttyCLIENT', stopbits=1, bytesize=8, parity='N', baudrate=9600)

connexion = client.connect()
print(client)
print("\033[92m-------------------client connected----------------------\033[0m")
# log.debug("client started")

def responseReceived(response):
    print("connected")
#     log.debug("server has send data")


while True:
    
    if connexion == True:
        print(" enter ID to get protocole ID \n enter IO to get the number of I/0 of the card \n enter PROBE what type is sond is the card")
        question = input("------ Witch information do you want to read ----------\n")
        # toSend = input("enter a string to write in holding register : ") # enter message to send
        # toSendCoils = input("enter a integer to write in coils: ")  # enter message to send

        if question == "ID":
            sending = client.write_registers(0,10,0x01)  # write to address 49849 of holding register
            test = client.read_holding_registers(0,1,0x01)
        elif question == "I/O":
            sending = client.write_register(1, 20,0x01)  # write to address 49849 of holding register
            test = client.read_holding_registers(1,1,0X01,callback=responseReceived)
            values = test.registers
            print(values)        
        elif question == "PROBE":
            sending = client.write_register(2, 2,0x01)  # write to address 49849 of holding register
            test = client.read_holding_registers(2,1,0X01,callback=responseReceived)
            print(test)
        else :
            print("you have not entered a good value")

        # print(test.decode())
        # client.write_coils(15, toSendCoils.encode('ascii'),0x01) #write  to address 15 coil register
    else:
        print("client not started")