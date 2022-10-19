from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

def catalogo(WEB):
    lista = []
    
    select = Select(WEB.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/form[@id='cadastro_itens']/div/div/div/div[1]/select"))
    select.select_by_value('500')
    
    sleep(3)
    
    navigator = WEB.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div/span/form/div/div/div/div[1]/span[2]")
    navigator = navigator.find_elements(By.TAG_NAME, 'a')
    
    for i in range(len(navigator)):
        if i != 0:
            navigator[i].click();
            sleep(3)
            
        rows = WEB.driver.find_elements(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/form/div/div/div/div/table/tbody/tr")
        
        for row in rows:
            cels = row.find_elements(By.TAG_NAME, 'td')
            lista.append([cels[0].text, cels[1].text, cels[4].text])
            
        navigator = WEB.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div/span/form/div/div/div/div[1]/span[2]")
        navigator = navigator.find_elements(By.TAG_NAME, 'a')
        
    return lista
