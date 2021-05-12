from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket

nome = input("Nome da Comunidade: ")
ordem = [None,None,'A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get("https://web.archive.org/web/20141002205918/https://orkut.google.com/") #Chamando o site do Wayback Machine
sleep(5) #Aguardando carregar


aux = nome[0].upper()
if aux in ordem:
    i = ordem.index(aux)
else:
    i = 1


try:
    element_presence(By.XPATH,'/html/body/div[8]/div',30)
    index_button =driver.find_element(By.XPATH,'/html/body/div[8]/div/a[{}]'.format(i))
    index_button.click()
except Exception as e:
    print("erro")
    sleep(10)
    is_connected()

nome1 = ''
fpage = 0

while nome1 != nome:
    nome1 = ''
    element_presence(By.XPATH,'/html/body/div[5]/div/div[1]',30)
    for x in range(2,103):
        coms = driver.find_element(By.XPATH ,'/html/body/div[4]/div/div[1]/div[{}]'.format(x))
        nome1 = coms.text
        #print(nome1)
        if nome in nome1:
            print(nome1,"encontrado.")
            input("Tecle enter para continuar buscando >")
    if fpage == 0:
        next_page = driver.find_element_by_xpath("""/html/body/div[5]/div/div[1]/div[1]/div/a""").click()
        fpage = 1
    next_page = driver.find_element_by_xpath("""/html/body/div[5]/div/div[1]/div[1]/div/a[3]""").click()
    sleep(5)

print(nome1,"encontrado.")