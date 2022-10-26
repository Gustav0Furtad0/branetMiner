from ast import excepthandler
from time import sleep
from selenium.webdriver.common.by import By
import json
import scraping.scraping as scraping

with open("key.json") as file:
    key = json.load(file)
    
    
def initProcess(WEB):
    WEB.driver.maximize_window()
    #WEB.driver.get('https://juizdefora.branetlogistica.com.br/doms')
    WEB.unidade = 1
    WEB.centroCusto = 1
        
      
def logaSistema(WEB, userin = key['user'], passwordin = key['password']):
    log = WEB.driver.find_elements(By.XPATH, "/html/body/div[@id='centro']/div[@id='bloco_login']/div[@class='login']/div[@id='conteudo']/form/span/div/input");
    log[0].send_keys(userin)
    log[1].send_keys(passwordin)
    btlogin = WEB.driver.find_element(By.XPATH, "/html/body/div/div/div/div/form/span/input")
    btlogin.click()
    btentrar = WEB.driver.find_element(By.XPATH, "/html/body/div[@id='centro']/div[@id='bloco_login']/div[@class='login']/div[@id='conteudo']/form/input[@class='btn-login btn-entrar azul_primario']")
    btentrar.click()
    
    sleep(2)
    refreshPage(WEB)
    WEB.driver.get('https://juizdefora.branetlogistica.com.br/doms/manutencao/mercadoria.xhtml')


def mudaUnidade(WEB, unidade):
    
    labelU = WEB.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='topo']/div[@class='div_topo_direita']/div/div[@id='login']/form[@id='formUndiades']/div[1]/label")
    labelU.click()
    
    sleep(1)
    
    listUnidades = WEB.driver.find_elements(By.XPATH, "/html/body/div[@id='formUndiades:unidade_panel']/div[@class='ui-selectonemenu-items-wrapper']/ul[@id='formUndiades:unidade_items']/li")
    WEB.unidadeNome = listUnidades[unidade].text
    listUnidades[unidade].click()
    
    
    WEB.unidade = unidade
    
    sleep(2)


def mudaCC(WEB, cc):  
    labelCC = WEB.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='topo']/div[@class='div_topo_direita']/div/div[@id='login']/form[@id='formUndiades']/div[2]/label")
    labelCC.click()
    
    sleep(1)
    
    listCC = WEB.driver.find_elements(By.XPATH, "/html/body/div[@id='formUndiades:centroCusto_panel']/div[@class='ui-selectonemenu-items-wrapper']/ul[@id='formUndiades:centroCusto_items']/li")
    
    if (cc == len(listCC) ):
        return False
    else:
        listCC[cc].click()
        
        WEB.centroCusto = cc
        
        sleep(2)


def confirmaMud(WEB):
    WEB.driver.find_element(By.XPATH, "/html/body/div[@id='formConfirmacaoSessao']/div/form/table/tbody/tr/td[1]/button/span").click()


def refreshPage(WEB):
    WEB.driver.refresh()
    sleep(3)
    

# analisa centro de custo
def entraCat(WEB, tabela):
    try: 
        rows = WEB.driver.find_elements(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div/form/div/div/div/table/tbody/tr")
        for row in rows:
            cels = row.find_elements(By.TAG_NAME, "td")
            if cels[2].text == "CIAD - CENTRO DE DISTRIBUICAO / CIAD":
                cels[4].find_elements(By.TAG_NAME, "button")[1].click()
                sleep(4)
                result = WEB.puxaCatalogo()
                col = tabela.colunasTabela(0)+1
                print ("Coluna a inserir: ", col)
                tabela.addData(tabelaIx = 0, columns = [col], data = WEB.unidadeNome, cab = True )
                tabela.addData(tabelaIx = 0, columns = [col], data = result, condition = [1,3], dataInner = [2])
                sleep(1)
    except:
        pass

            
    
    
def navegaTodasUnidades(WEB, tabela):
    initProcess(WEB)
    input("Está no catalogo?")
    tabela.nome = "catcompleto"
    entraCat(WEB, tabela)
    #WEB.unidade
    for i in range(1, 138):
        tabela.saveArchive()
        mudaUnidade(WEB, i)
        ix = 1
        while True:
            sleep(2)
            if(mudaCC(WEB, ix) == False):
                break
            ix += 1
            confirmaMud(WEB)
            sleep(2)
            refreshPage(WEB)
            WEB.driver.get("https://juizdefora.branetlogistica.com.br/doms/processos/catalogo.xhtml")
            sleep(2)
            entraCat(WEB=WEB, tabela=tabela)
            
        sleep(2)
