from excel.table import ExTable
import scraping.scraping as scraping

from excel.table import ExTable

driver = scraping.ChromeDriver()

table = ExTable()
catCompleto = ExTable()

def listaCadItens(op):
    result = driver.puxaItens()
    if op:
        table.tableItens(dataTable=result)
    else:
        for i in range(len(result)):
            print(result[i])
    
def listaParamCatalog(op):
    result = driver.puxaCatalogo()
    if op:
        table.tableItens(result)
    else:
        for i in range(len(result)):
            print(result[i])

def quit():
    del table
    driver.quitDriver(driver) 
    
def geraCatCompleto():
    
    driver.loginSistema()
    
    input("entra catalogo")
    
    result = driver.puxaItens()

    catCompleto.addData( tabelaIx = 0, columns = [1,2,3], data = result)
    
    driver.geraCatalogoCompleto(catCompleto)
    
geraCatCompleto()