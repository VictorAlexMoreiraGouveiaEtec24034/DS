lista = []

# Função de help do sistema
def Help():
    print("")
    print("0) Finaliza o programa")
    print("1) Adicionar item")
    print("2) Remover item")
    print("3) Listar item")
    print("4) Lista opções")
    print("5) Salvar lista")
    print("6) Carregar lista")
    print("")

# Chama a função assim que o programa começa
Help()

# Loop infinito até digitar 0
while True:
    # Promp para escolher a ação
    prompt = input("Digite o que deseja fazer: ")

    # Caso digite 1
    if (prompt == "1"):
        # Adiciona o elemento a lista caso não exista.
        print("")
        add = input("Adicione o item> ")
        print("")

        if (add in lista):
            print("Esse item já existe")
            print("")

        else:
            lista.append(add)
            print("Item adicionado com sucesso")
            print("")

    # Caso digite 2
    elif (prompt == "2"):
        print("")
        # Varifica se o item existe na lista e remove
        rev = input("Digite o nome do item para remover> ")
        if (rev in lista):
            lista.remove(rev)
            print("Item removido com sucesso.")
            print("")

        # Caso o item não exista, exibe um erro
        else:
            print("Erro: Não foi possivel identificar o item na lista.")
            print("")

    # Caso digite 3
    elif (prompt == "3"):
        print("")
        # Exibe cada elemento da lista
        for item in lista:
            print("- " + item)

        print("")

    # Caso digite 4
    elif (prompt == "4"):
        print("")
        # Chama a função de orientação ao usuário
        Help()

    # Caos digite 5
    elif (prompt == "5"):
        # Salva a lista dentro de um .txt
        NameFile = input("Como quer chamar o arquivo?: ")
        with open(f"{NameFile}.txt", 'w') as file:
            for item in lista:
                file.write(item + "\n")
        
        file.close()

    # Caso digite 6
    elif (prompt == "6"):
        # Carregar lista do arquivo .txt
        print("")
        FileNameLoad = input("Qual o nome do arquivo? (Digite o nome sem o .txt): ")
        arquivo = f"{FileNameLoad}.txt"  # Nome do arquivo com extensão

        # Abre o arquivo e verifica se ele foi aberto com sucesso
        file = open(arquivo, "r")
        if file:
            lista.clear()  # Limpa a lista atual antes de carregar os itens do arquivo
            for linha in file:
                lista.append(linha.strip())  # Adiciona cada item removendo quebras de linha
            file.close()  # Fecha o arquivo
            print("Lista carregada com sucesso:")
            for item in lista:
                print("- " + item)
        else:
            print("Erro: Não foi possível abrir o arquivo.")

    # Caso digite 0
    elif (prompt == "0"):
        print("")
        # Finaliza o algoritmo
        print("Fim do programa")
        break

    # Caso o usuário digitar qualquer outro número não listado
    else:
        print("Opção inválida por favor tente novamente")
        print("Digite '4' para listar as ações possiveis")