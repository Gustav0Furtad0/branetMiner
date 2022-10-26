from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def itens(WEB):
    lista = []

    select = Select(WEB.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form[@id='lista']/div/div[1]/select"))
    select.select_by_value('500')
    sleep(3)
    WEB.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form[@id='lista']/div/div/table/thead/tr/th[2]").click()
    sleep(3)
    navigator = WEB.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form[@id='lista']/div/div[1]/span[2]")
    navigator = navigator.find_elements(By.TAG_NAME, 'a')
    
    for i in range(len(navigator)):
        if i != 0:
            navigator[i].click();
            sleep(3)
            
        rows= WEB.driver.find_elements(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form[@id='lista']/div/div/table/tbody/tr")
        for ix, row in enumerate(rows):
            if ((ix+1) % 500) == 0:
                print("Extraindo item ", (i+1)*500)
            cels = row.find_elements(By.TAG_NAME, 'td')
            lista.append([cels[1].text, cels[2].text, cels[5].text])

        navigator = WEB.driver.find_element(By.XPATH, "/html/body/div[@id='div_principal']/div[@id='div_principal']/div[@id='conteudo_template']/span[@id='conteudo']/div[@id='panelPesquisa']/div[@id='panelPesquisa_content']/form[@id='lista']/div/div[1]/span[2]")
        navigator = navigator.find_elements(By.TAG_NAME, 'a')

    return lista
