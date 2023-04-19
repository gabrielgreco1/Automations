import pyautogui
import keyboard
import csv
import subprocess
import sys
import time
from time import sleep
import datetime


log_file = open("C:\Automacao\AutomacoesPITON\INU_CTE_CLICK\log.txt", "w")
sys.stdout = log_file
pyautogui.FAILSAFE = False

def print_with_timestamp(*args, **kwargs):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(timestamp, *args, **kwargs, file=log_file)

login = "gabriel.greco"
password = "Jardim5Secret!@#"
modulo = "05" # Módulo Faturamento
rotina = "Nf-e Sefaz"

# Abrir o aplicativo
subprocess.Popen('C:\\Users\\Administrator\\Desktop\\smartclient_x64\\smartclient.exe')

if keyboard.press("esc"):
    sys.exit()

print("Abrindo Protheus...")

# Validacao que sera utilizada
while not pyautogui.pixelMatchesColor(858,750, (0, 0, 255)): 
    time.sleep(2)
print_with_timestamp("Execução Ok")

pyautogui.moveTo(974,627)
pyautogui.click(974,627)
pyautogui.moveTo(1000, 729, duration=1.5)
pyautogui.click(1000, 729)

# Aguardar o aplicativo carregar
time.sleep(7.5)


print_with_timestamp("Logando...")

# Clicar no login e logar
pyautogui.moveTo(904,545)
pyautogui.write(login)
pyautogui.press("tab")
pyautogui.write(password)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")  

time.sleep(5)

# Espera o software carregar e seleciona a rotina

for i in range(4):
    pyautogui.press("tab")
time.sleep(0.5)

# Seleciona o módulo 
pyautogui.write("13")
pyautogui.press("tab")
pyautogui.write("05")
pyautogui.press("tab")
pyautogui.write(modulo)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(4)

# Seleciona a rotina
pyautogui.moveTo(74,550, duration=1)
pyautogui.click(74,550)
pyautogui.write(rotina)
pyautogui.moveTo(219,551, duration=2)
pyautogui.click(219,551)

while not pyautogui.pixelMatchesColor(1669,796, (6,69,85)):
    time.sleep(3)
print_with_timestamp("Login realizado - Selecionando rotina...")

# Confirmar empresa
pyautogui.moveTo(1114,797)
pyautogui.click(1114,797)

time.sleep(5)
while not pyautogui.pixelMatchesColor(1157,378, (90,107,156)):
    time.sleep(2)
print_with_timestamp("Execucao ok! - Iniciando rotina")

# Continuar pra rotina
pyautogui.moveTo(1130,774, duration=1)
pyautogui.click(1130,774)

# Zerar série
pyautogui.moveTo(959,528, duration=2)
pyautogui.click(959,528)
pyautogui.write("000")

pyautogui.moveTo(1133,778, duration=2)
pyautogui.click(1133,778)

while not pyautogui.pixelMatchesColor(1879,341, (28,157,189)):
    time.sleep(2)
print_with_timestamp("Execucao ok! - Rodando a rotina")

#METODO with open para arquivos csv (leitura)?
with open('C:\Automacao\AutomacoesPITON\INU_CTE_CLICK\INUTILIZACAO.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in arquivo:
        while not pyautogui.pixelMatchesColor(48,467, (255,255,255)):
            time.sleep(2)
        Inicial = linha.split(';')[0]
        Final = linha.split(';')[1]
        Numero = linha.split(';')[2]
        print_with_timestamp("Começando Inutilização do período: ", Inicial, " até ", Final)
        pyautogui.click(508,230, duration=3)   # Outras acoes
        pyautogui.click(488,535, duration=1)  # Inutilizacao
        pyautogui.click(1330,880, duration=5)  # Avançar
        pyautogui.click(849,455, duration=1)  # Numero
        pyautogui.write(Numero)
        #pyautogui.click(849,510, duration=2)  # Inicial
        pyautogui.write(Inicial)
        #pyautogui.click(849,555, duration=2)  # Final
        pyautogui.write(Final)
        pyautogui.press(['shift','left'])
        pyautogui.click(1310, 870) # Avançar /2
        pyautogui.click(1235,778, duration=1.5)
        pyautogui.click(1079,774, duration=1.5)
        pyautogui.click(1321,876, duration=1.5)
    print_with_timestamp("Processo finalizado!")
    log_file.close()
    arquivo.close()
