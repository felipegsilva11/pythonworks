# Ler um número inteiro do usuário
numero = int(input("Digite um número inteiro para ver a sua tabuada: "))

# Mostrar a tabuada do número digitado
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
