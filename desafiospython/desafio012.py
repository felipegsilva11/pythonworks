# Ler o preço do produto
preco = float(input("Digite o preço do produto: "))

# Calcular o preço com desconto de 5%
novo_preco = preco * 0.95  # 0.95 representa 95% do preço original (100% - 5% de desconto)

# Exibir o novo preço com desconto
print(f"O preço com 5% de desconto é: R$ {novo_preco:.2f}")
