#!/usr/bin/env python
# -*- coding: UTF-8 -*-
  
import bluetooth
import time
from random import randint
y = "0";
bd_addr = "94:B9:7E:E4:40:72" #j'ai mis l'add mac du raspberry que j'ai pris avec la la ligne de commande (bluetoothctl)
  
port = 1
 
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
  
#rnd = randint(1,3)
#toSend = "profil:%d" % rnd
for x in range (10):
    if (y == '0'):
        y = "1"
    else:
        y = "0"
    sock.send(y)
    print(f"enviando comando {y}") 
    #data = sock.recv(1024)
    time.sleep(5)

sock.close()
