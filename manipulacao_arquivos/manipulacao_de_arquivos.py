'''Este é um exemplo de manipulação de arquivos em Python dentro de uma função.'''


def soma(num1,num2): #função para calcular a soma
    soma = num1 + num2
    
    file = 'arquivo.txt'

    #ABERTURA DE ARQUIVOS

    #abertura para escrita
    arquivo_escrita = open(file, 'w') #w de write
    arquivo_escrita.write(f'O resultado da soma é: {soma}')
    arquivo_escrita.close() #fecha o arquivo após escrever

    #abertura somente para leitura
    arquivo_leitura = open(file, 'r') #r de read
    #leitura
    leitura = arquivo_leitura.read() #lê todo o conteúdo do arquivo
    print(leitura) # mostra o conteúdo lido
    arquivo_leitura.close() #fecha o arquivo após escrever

    

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma(num1,num2) #chamada da função