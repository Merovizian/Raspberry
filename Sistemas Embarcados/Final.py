import bluetooth, time
end = 0;
aux = 0;
nome = 0;
y = "0";

def scan():
    aux = 0
    end = 0
    nome = 0
    print("Localizando o servidor ESP32 BT")

    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)

    number_of_devices = len(devices)

    for addr, name, device_class in devices:
        if (name == "ESP32_LED_Control"):
            end = addr
            nome = name
            aux = 1
    
    return end,nome,aux



for a in range(5):
    end,nome,aux = scan();
    if (aux == 0):  
        print(f"Controlador ESP32 não localizado!")
        time.sleep(1)
        print(f"Verifique conexão")
        time.sleep(1)
        print(f"Tentativa {a+2} de 5 ...")
        time.sleep(2)
    else:
        print(f"********************\nServidor {nome} localizado com Sucesso!!\nEndereço Mac de {nome}: {end}")
        break
    

#!/usr/bin/env python
# -*- coding: UTF-8 -*-


bd_addr = end 
  
port = 1
 
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
  

for x in range (10):
    if (y == '0'):
        y = "1"
    else:
        y = "0"
    sock.send(y)
    print(f"Comando {y} enviado com sucesso!!") 
    time.sleep(5)

sock.close()