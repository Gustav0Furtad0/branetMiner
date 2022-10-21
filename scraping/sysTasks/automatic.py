from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import json

with open("key.json") as file:
    key = json.load(file)

class ChromeDriver:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    
    def __init__(self):
        self.driver.get('https://juizdefora.branetlogistica.com.br/doms')
        
    def logaSistema(self, userin, passwordin):
        log = self.driver.find_elements(By.XPATH, "/html/body/div[@id='centro']/div[@id='bloco_login']/div[@class='login']/div[@id='conteudo']/form/span/div/input");
        # user = self.driver.find_element(By.ID, "j_idt19:login")
        # password = self.driver.find_element(By.ID, "j_idt19:senha") 
        log[0].send_keys(userin)
        log[1].send_keys(passwordin)
        btlogin = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/span/input")
        btlogin.click()
        sleep(5)
        self.driver.refresh()
        sleep(2)
        
nav = ChromeDriver()
nav.logaSistema(key['user'], key['password'])
    