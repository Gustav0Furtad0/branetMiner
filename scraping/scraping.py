from selenium import webdriver
from scraping.sysTasks.puxaCatalog import catalogo
from scraping.sysTasks.puxaItens import itens
import scraping.sysTasks.automatic as automatic
from selenium.webdriver.common.by import By

class ChromeDriver:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    unidade = None # unidade que o sistema está logado
    unidadeNome = None
    centroCusto = None # centro de custo que está acessado na unidade
    
    def __init__(self):
        self.driver.get('https://juizdefora.branetlogistica.com.br/doms')
    
    def puxaItens(self):
        result = itens(self)
        return result
    
    def puxaCatalogo(self):
        result = catalogo(self)
        return result
    
    def geraCatalogoCompleto(self, tabela):
        automatic.navegaTodasUnidades(self, tabela)
        
    def loginSistema(self):
        automatic.logaSistema(WEB = self)
    
    def quitDriver(self):
        self.driver.quit()