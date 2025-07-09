def divisao(a, b):
    try:
        resultado = a / b
        print(f"Resultado da divisão: {resultado}")
    
    except ZeroDivisionError as e:
        print("Erro: Divisão por zero não é permitida.")
        
        
    except TypeError as e:
        print(f"Erro: O tipo de dado é inválido.\n Detalhes: {e}")

    
        

divisao(10, 2)  # Deve imprimir o resultado da divisão
divisao(10, 0)  # Deve imprimir mensagem de erro para divisão por zero
divisao(10, "a")  # Deve imprimir mensagem de erro para tipo inválido