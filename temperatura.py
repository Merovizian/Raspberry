from time import time, sleep
from datetime import date,datetime
from gpiozero import CPUTemperature

cpu = CPUTemperature()
temp = (cpu.temperature)

data_atual = str(date.today())
time_atual = time()
texto = list()

horario = datetime.now().strftime("%H:%M:%S")



def arquivoExiste(nome):
    '''
    Verifica se um arquivo já existe, se não o cria.
    :param nome: arquivo
    :return:1 - Se o arquivo já existe e 0 - se não existe
    '''
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return 0
    else:
        return 1

arquivo = data_atual
if arquivoExiste(arquivo) == 0:
    a = open(arquivo, 'wt+')
    print(f"Arquivo {arquivo} criado com sucesso!")
else:
    a = open(arquivo, 'a')
    print(f"Arquivo {arquivo} já existente")


a.writelines(f"{data_atual}\n")
a.writelines(f"   Time  - Temperatura\n")

while True:
    try:
        if(time() - time_atual >= 100 ):
            cpu = CPUTemperature()
            temp = (cpu.temperature)
            horario = datetime.now().strftime("%H:%M:%S")
            a.writelines(f" {horario}    {temp}\n")
            time_atual = time()
            
           
    except:
        a.writelines(f"\n\n")
        a.close()
        print(f"Arquivo {arquivo} gravado com sucesso!")
        break;


    
