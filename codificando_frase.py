frase = input("Digite uma frase:")
modificada = ""

for letra in frase:
  if letra == " ":
    modificada += "-"
  elif letra == "a":
    modificada += "@"
  else:
    modificada += letra

print("Frase modificada", modificada)