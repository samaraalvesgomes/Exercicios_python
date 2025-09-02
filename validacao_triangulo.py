print("Classificando um Triângulo!")

while True:

    try:
        a = float(input("Digite o lado A: "))
        b = float(input("Digite o lado B: "))
        c = float(input("Digite o lado C: "))
    except ValueError:
        print("Por favor, insira apenas números.")
        continue

    if a + b > c and a + c > b and b + c > a: 
        print("É um triângulo válido!")
        if a == b == c:  #Todos os lados iguais
            print("É um triângulo equilátero.")
        elif a == b or a == c or b == c: #Dois lados iguais
            print("É um triângulo isósceles.")  
        else:   #Todos os lados diferentes
            print("É um triângulo escaleno.")
    else: 
        print("Não forma um triângulo.")
    
    resposta = input(("Deseja continuar? (s/n):"))

    if resposta == "s"or resposta == "S":
        continue
    else:
        print("Programa encerrado.")
        break