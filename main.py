import controlSys

while True:
    if input("Faça login no sistema e tecle enter para continuar") == '':
        break
   
while True: 
    option = int(input (
"""\n
    --- Para fazer a extração de algum dado digite a opção correspondente na tela correspondente ---
    
    [0] Sair do sistema
    [1] Extrair mercadorias registradas na base Juiz de Fora (Tela: Cadastro de Mercadorias)
    [2] Extrair parametrizado de um catálogo selecionado (Tela: Gerenciar catálogo)
        
Rs:"""))

    match option:
        case 0:
            quit()
            break
        
        case 1:
            if input("Faca a configuracao de filtros que deseja e pressione ENTER para continuar\n") == "":
                if int(input("Se deseja passa para uma planilha digite [1] ou [0] para imprimir os itens: ")) == 1:
                    controlSys.listaCadItens(True)
                else:
                    controlSys.listaCadItens(False)

            else:
                print("Pressiona somente a tecla ENTER")
                
        case 2:
            if input("Digite ENTER para iniciar a extracao ") == "":
                if int(input("Se deseja passa para uma planilha digite [1] ou [0] para imprimir os itens: ")) == 1:
                    controlSys.listaParamCatalog(True)
                else:
                    controlSys.listaParamCatalog(False)

            else:
                print("Pressiona somente a tecla ENTER")
        
        case _:
            print ("!!! OPCAO INVALIDA !!! Tente novamente como umas das opcpes disponíveis!" )