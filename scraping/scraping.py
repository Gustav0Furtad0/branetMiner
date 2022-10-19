from selenium import webdriver
from scraping.sysTasks.puxaCatalog import catalogo
from scraping.sysTasks.puxaItens import itens

class ChromeDriver:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    
    def __init__(self):
        self.driver.get('https://juizdefora.branetlogistica.com.br/doms')
    
    def puxaItens(self):
        result = itens(self)
        return result
    
    def puxaCatalogo(self):
        result = catalogo(self)
        return result
    
    def quitDriver(self):
        self.driver.quit()