import bluetooth, time

def scan():
    '''
    REALIZA A PROCURA POR UM DISPOSITIVO BT, NESTE CASO ESPECIFICO O BT DE NOME "ESP32_LED_Control"
    RETORNA:
    0 - SE NÃO ACHAR NENHUM DISPOSITIVO COM ESP32.
    endereço MAC do DISPOSITIVO BLUETOOTH ESP32.
    '''
    
    print("Localizando o servidor ESP32 BT")  #Essa linha poderá ser apagada depois do programa estar pleno.

    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)

    number_of_devices = len(devices)

    for addr, name, device_class in devices:
        if (name == "ESP32_LED_Control"):
           # nome = name   
           #  aux = 1
            return addr
        else:
            return 0
        
def envio(bd_addr, y):
    '''
    REALIZA O ENVIO DE UMA INFORMAÇÃO POR BLUETOOTH.
    ENTRADAS:
    bd_addr - é o endereço MAC do dispositivo BLUETOOTH ao qual a informação será enviada.
    y - é a informação em que deverá ser enviada ao dispositivo BLUETOOTH.
    IMPORTANTE: A INFORMAÇÃO DEVERÁ SER SOMENTE UM CHAR DE DOIS VALORES "0" e "1" ONDE:
    "0" - Carro permitido.
    "1" - Carro impedido.

    '''
    
    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-
    
    port = 1
    
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bd_addr, port))
 
    sock.send(y)
    print(f"Comando {y} enviado com sucesso!!") #Essa linha poderá ser apagada depois do programa estar pleno.
    time.sleep(5)
    sock.close()


    
rede = scan()
print(rede) #Essa linha poderá ser apagada depois do programa estar pleno.
y = "0" #Essa linha poderá ser apagada depois do programa estar pleno.
for x in range (10): #ESTE FOR DEVERA SER APAGADO QUANOD O SITEMA ESTIVER OPERANTE.
    if (y == '0'):
        y = "1"
    else:
        y = "0"
    print(y)
    envio(rede,y)
    time.sleep(10);
