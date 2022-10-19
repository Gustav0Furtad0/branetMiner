import openpyxl as opx

class ExTable():
    def __init__(self):
        self.arquivo = opx.Workbook()
        self.nome = None
        self.arquivo.remove(self.arquivo.worksheets[0])
        
    def criaTabela(self, tnome):
        self.arquivo.create_sheet(tnome)
        self.arquivo.sheetnames.sort()
        
    def listaTabelas(self):
        return self.arquivo.sheetnames
    
    def tabelaAtiva(self):
        return self.arquivo.active.title
    
    def addData(self, tabelaIx, columns, data, dataInner = False, conditions = False, ):
        
        tabela = self.arquivo[self.arquivo.sheetnames[tabelaIx]]
        
        if conditions == False:
            for ix, coluna in enumerate(columns):
                for dado in range(len(data)):
                    cel = tabela.cell(row=(dado+1), column=coluna)
                    cel.value = data[dado][ix]
        
        else:
            for indicedata, coluna in enumerate(columns):
                for dado in range(len(data)):
                    if ( str(data[dado][conditions[0]]) == str(tabela.cell(row=(dado+1), column=conditions[1]).value) ):
                        cel = tabela.cell(row=(dado+1), column=coluna)
                        if dataInner == False:
                            cel.value = data[dado][indicedata]
                        else:
                            cel.value = data[dado][dataInner[indicedata]]
            
    def saveArchive(self):
        self.arquivo.save(filename=f"{self.nome}.xlsx")
