produtos = {}

while True:

    print("MENU:")
    print("1. Exibir estoque atual \n 2. Adicionar um produto \n 3. Remover um produto \n 4. Atualizar a quantidade de um produto \n 5. Sair")
    
    try:
      numero = int(input("Você gostaria de: "))
    except ValueError: 
      print("Por favor, insira apenas o número.")
      break

    if numero == 1:  #Exibir estoque atual
        for chave, valor in produtos.items():
            print(chave, valor)

    elif numero == 2:  #Adicionar um produto
        item = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        produtos[item] = quantidade  
        print(f"Produto {item} adicionado com quantidade {quantidade}.")

    elif numero == 3:  #Remover um produto
        remov_produto = input("Digite o nome do produto que deseja remover:")             
        produtos.pop(remov_produto,None)  
        print(f"Produto {remov_produto} removido.")

    elif numero == 4:  #Atualizar a quantidade de um produto
        item = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a nova quantidade do produto: "))
        produtos[item] = quantidade
        print(f"Quantidade do produto {item} atualizada para {quantidade}.")  
        
    elif numero == 5:  #Sair
        print("programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")