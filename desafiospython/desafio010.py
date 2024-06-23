# Ler quantos reais a pessoa tem na carteira
dinheiro_em_reais = float(input("Digite quantos reais você tem na carteira: "))

# Definir a taxa de câmbio
taxa_de_cambio = 3.27  # US$1,00 = R$3,27

# Calcular quantos dólares ela pode comprar
dolares_possiveis = dinheiro_em_reais / taxa_de_cambio

# Exibir o resultado
print(f"Com R$ {dinheiro_em_reais:.2f} você pode comprar aproximadamente US$ {dolares_possiveis:.2f}")
