import scraping.scraping as scraping

from control.listaCadItens import tableItens
from control.listaParamCatalog import tableCatalog

driver = scraping.ChromeDriver()

def quit():
    driver.quitDriver(driver)

def listaCadItens(op):
    return tableItens(op, driver)
    
def listaParamCatalog(op):
    return tableCatalog(op, driver)