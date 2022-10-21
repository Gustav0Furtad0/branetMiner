from excel.table import ExTable
import scraping.scraping as scraping

from excel.table import ExTable

# from control.listaCadItens import tableItens
# from control.listaParamCatalog import tableCatalog

driver = scraping.ChromeDriver()

table = ExTable();

def listaCadItens(op):
    result = driver.puxaItens()
    if op:
        table.tableItens(result)
    else:
        for i in range(len(result)):
            print(result[i])
    
def listaParamCatalog(op):
    result = driver.puxaParamCatalog()
    if op:
        table.tableItens(result)
    else:
        for i in range(len(result)):
            print(result[i])

def quit():
    driver.quitDriver(driver)