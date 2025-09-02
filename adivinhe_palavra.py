import random

palavras = ["casa","sol","livro","areia"]
palavra = random.choice(palavras)

palavra_codificada = "_" * len(palavra)
erros = 0

while "_" in palavra_codificada:
    print("Palavra:", palavra_codificada)
    letra = input("Digite uma letra: ")

    if letra in palavra:
        nova_palavra = ""
        for i in range(len(palavra)):
            if palavra[i] == letra:
                nova_palavra += letra
            else:
                nova_palavra += palavra_codificada[i]
        palavra_codificada = nova_palavra
    else:
        print("Letra incorreta!")
        erros += 1

print("Você acertou! A palavra era:", palavra)
print("Você cometeu", erros, "erro(s).")