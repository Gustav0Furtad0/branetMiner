from excel.table import ExTable
from time import sleep

table = None

def tableItens(op, driver):
    if op:
        result = driver.puxaItens()
        if table == None:
            print("=_=_=_=_=_=_=_= TABELA PESONALIZADA [NOVA TABELA] =_=_=_=_=_=_=_=\n\n")
            table = ExTable()
            sleep(2)
            
            table.nome = input("Nome do arquvio: ")
            
            print(result)
        
        
    else:
        result = driver.puxaItens()
        for i in range(len(result)):
            print(result[i])