#1.Importando as bibliotecas
import webbrowser #biblioteca para abrir o navegador padrão do seu PC
import pyautogui #Biblioteca para trabalhar com o mouse e teclado
import time #para dar um tempo de intervalo entre uma ação e outra
import os #fazer interação entre pastas do seu Sistema Operacional
import fnmatch #Procura um arquivo por nome ou extenssão
import shutil #Move arquivos entre pastas
#----------------------------

#2.Obtendo dados
os.chdir('C:\\Users\\Rubens\\Downloads') #definindo a pasta inicial (para onde vai seu download apos ser baixado pelo navegador

download_dir = '' #Variavel vazia
brrt_dir = 'D:\\Download\\' #Pasta vazia para destinar o arquivo apos ser baixado

webbrowser.open('https://br.leagueoflegends.com/pt-br/') #endereço de destino (de onde você quer fazer a automação
#---------------

time.sleep(6) #intervalo de tempo em SEGUNDOS para a pagina carregar


#3.Resultado---------------------------------------------------------

pyautogui.moveTo(1700, 140, duration=0.25) #movendo o mouse para as coordenadas (X e Y) em PIXEL em uma duração de 0.25 milisegundos
pyautogui.click(1700, 140, button='left', duration=0.25) #Clicando no link

time.sleep(2) #intervalo de tempo em SEGUNDOS para a pagina carregar

#4.Proxima pagina
pyautogui.moveTo(760, 480, duration=0.25) #movendo o mouse para as coordenadas (X e Y) em PIXEL em uma duração de 0.25 milisegundos
pyautogui.click(760,480, button='left', duration=0.25)#Clicando no link
pyautogui.hotkey('ctrl', 'a') #caso tenha algo no formulario ele seleciona tudo
time.sleep(1) #intervalo de tempo em SEGUNDOS para a pagina carregar
pyautogui.hotkey('del') #se tiver algo ele deleta

time.sleep(1) #intervalo de tempo em SEGUNDOS para a pagina carregar

pyautogui.typewrite('SEU NOME DE USUARIO') #Inserindo seu LOGIN

time.sleep(1) #intervalo de tempo em SEGUNDOS para a pagina carregar

pyautogui.hotkey('tab') #Aperta a tecla Tab pra ir ao proximo campo
pyautogui.hotkey('ctrl', 'a') #caso tenha algo no formulario ele seleciona tudo

time.sleep(1) #intervalo de tempo em SEGUNDOS para a pagina carregar

pyautogui.hotkey('del') #se tiver algo ele deleta

time.sleep(1) #intervalo de tempo em SEGUNDOS para a pagina carregar
pyautogui.typewrite('SUA SENHA') #Inserindo sua Senha

time.sleep(1) #intervalo de tempo em SEGUNDOS para a pagina carregar
pyautogui.hotkey('enter') #Clicando na tecla ENTER para entrar com login e senha

time.sleep(2) #intervalo de tempo em SEGUNDOS para a pagina carregar
pyautogui.moveTo(1790, 140, duration=0.25) #Move o mouse para a proxima coordenada

time.sleep(4) #intervalo de tempo em SEGUNDOS para a pagina carregar
pyautogui.moveTo(1790, 283, duration=0.25) #Move o mouse para a proxima coordenada
pyautogui.click(1790, 283, button='left', duration=0.25) #Clica em um link/Botão

time.sleep(2) #intervalo de tempo em SEGUNDOS para a pagina carregar
pyautogui.moveTo(850,700, duration=0.25) #Move o mouse para a proxima coordenada
pyautogui.click(850, 700, button='left', duration=0.25) #Clica em um link/Botão

time.sleep(2) #intervalo de tempo em SEGUNDOS para a pagina carregar
pyautogui.moveTo(405, 1010, duration=0.25) #Move o mouse para a proxima coordenada
pyautogui.click(405,1010, button='left', duration=0.25) #Clica em um link/Botão

recent_download_file_name = '' #Implementando uma variavel vazia para alocar o arquivo temporariamente

time.sleep(30) #intervalo de tempo em SEGUNDOS para a pagina carregar

#5. For para listar a pasta de destino do DOWNLOAD
for entry in os.listdir():
    if fnmatch.fnmatch(entry, "Install League of Legends br.exe"): #Se encontrar o Arquivo (lembrandod e por a extenssão
        recent_download_file_name = entry #Alocando o arquivo encontrado na variavel temporaria

#6.Condicional
if recent_download_file_name != '': #Caso a variavel esteja diferente de vazio faça:
    print('moving file...', recent_download_file_name)
    shutil.move(recent_download_file_name, brrt_dir+'lol.exe')#Movendo o arquivo da pasta atual para a pasta definida e alterando o nome do arquivo


time.sleep(30) #intervalo de tempo em SEGUNDOS para a pagina carregar

pyautogui.hotkey('alt', 'f4')#Fecha o navegador apos finalizar o processo
