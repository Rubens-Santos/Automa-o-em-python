#1. Importando as bibliotecas

from selenium import webdriver
import time

#-----------------------------


#2.Criando a classe
class WhatsappBot:
    def __init__(self): #Metodo construtor
        self.mensagem = "Você quer aprender Python de muitas formas? acesse: https://www.udemy.com" #Mensagem que será enviada via WhatSapp
        self.grupos = ["TESTE BOT2", "TESTE BOT WHATSAPP"] #Gupos a que deseja enviar as mensagens
        options= webdriver.ChromeOptions()
        options.add_argument('lang=pt-br') #Idioma
        self.drive = webdriver.Chrome(executable_path=r'./chromedriver.exe') #chamando o .exe do crome

    def EnviarMensagens(self): #Função para entrar no grupo, escrever a mensagem e enviar
        self.drive.maximize_window() #Maximizando a tela do navegador

        # <span dir="auto" title="Kingdom of Sevele" class="_19RFN _1ovWX _F7Vk">Kingdom of Sevele</span>
        # <div tabindex="-1" class="_1Plpp">
        # <span data-icon="send" class="">

        self.drive.get('https://web.whatsapp.com/') #Entrando no whatsapp web ---------- OBS.:use seu celular para verificar o cofigo

        time.sleep(15) #Tempo de espera para carregar o site e usar o codigo
        for grupo in self.grupos: #Loop para enviar as mensagens para a lista de grupos
            grupo = self.drive.find_element_by_xpath(f"//span[@title='{grupo}']") #Indentificando os grupos
            time.sleep(3)
            grupo.click() #Clicando para entrar no grupo
            chat_box = self.drive.find_element_by_class_name("_1Plpp") #Clicando no campo para escrever o texto
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem) #Escrevendo o Texto
            botao_enviar = self.drive.find_element_by_xpath("//span[@data-icon='send']") #Enviando a mensagem
            time.sleep(3)
            botao_enviar.click()#Enviando a mensagem
            time.sleep(4)

        self.drive.quit()#Fechando o navegador



#Chamando as funções
bot = WhatsappBot()
bot.EnviarMensagens()





