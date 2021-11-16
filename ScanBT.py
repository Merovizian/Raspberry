#!/usr/bin/python3

# geektechstuff bluetooth

import bluetooth

def scan():
    aux = 0
    end =''
    nome = ''
    print("Localizando o servidor ESP32 BT")

    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)

    number_of_devices = len(devices)

    for addr, name, device_class in devices:
        if (name == "ESP32_LED_Control"):
            end = addr
            nome = name
            aux = 1
    
            
    if (aux != 1):
        print(f"Controlador ESP32 não localizado!\nVerifique conexão")
    return end,nome
scan()
