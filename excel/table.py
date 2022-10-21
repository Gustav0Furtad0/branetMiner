import openpyxl as opx
from time import sleep

def strtoArray()

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
    
    def addData(self, tabelaIx, columns, data, dataInner = False, conditions = False):
        
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
        
    
    def tableItens(self, dataTable):
        print(f"=_=_=_=_=_=_=_= TABELA PESONALIZADA {self.nome} =_=_=_=_=_=_=_=\n\n")
        data = dataTable
        while True:
            optext = f"""\n
                    --- Para fazer a manipulacao de arquivos escolha uma opcao abaixo ---
                    Lista de tabelas: 
                    """
                    
            for i, tbl in enumerate(self.tabelaAtiva()):
                optext += f"\n{i} - {tbl}"
                
            optext +=f"""
                    \n
                    [0] Voltar para extracao de dados
                    [1] Mudar nome do arquivo
                    [2] Criar tabela em {self.nome}.xlsx
                    [3] Listar areas de trabalho existentes
                    [4] Adicionar dados a uma tabela simples
                    [5] Adicionar dados condicionais a uma tabela
                    [6] Salvar Arquivo
                        
                    Rs:"""
            option = int(input(optext))
            
            match option:
                case 0:
                    return
                
                case 1:
                    self.nome = input("\nNome do arquvio: ")
                    
                case 2:
                    self.criaTabela(input("\nNome da Tabela: "))
                    
                case 3:
                    print(self.listaTabelas())
                    
                case 4:
                    
                    tabelaIX = input("\nEscolha a tabela a ter dados inseridos: ")
                    self.avisoTabela(dataTable[0])
                    columns = lambda colunas = input("Digite as colunas onde quer inserir na ordem dos dados (',' entre elas): ") : colunas.replace(" ", "").split(",")

                    for col in columns:
                        columns[col] = int(col)
                    
                    self.addData( tabelaIx = tabelaIX, columns = columns, data = data)
                    
                case 5:
                    tabelaIX = input("\nEscolha a tabela a ter dados inseridos: ")
                    
                    columns = lambda colunas = input("Digite as colunas onde quer inserir na ordem dos dados (',' entre elas): ") : colunas.replace(" ", "").split(",")
                    
                    for col in columns:
                        columns[col] = int(col)
                        
                    conditions = input("['dados extraido indice', 'coluna indice'] analisar dado e coluna (',' entre elas): ")
                    for col in conditions:
                        columns[col] = int(col)
                    
                    self.addData( tabelaIx = tabelaIX, columns = columns, data = data, conditions = False, dataInner = False)
            
                case 6:
                    self.saveArchive()
        
    def avisoTabela(data):
        avisodata = ""
        
        for i, dado in enumerate(data[1]):
            avisodata += f"{i+1} - {dado}, "
            
        print(f"""Vale lembra que as colunas de dados são: {avisodata}""")
