# Entrada de dados
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Cálculo da área da parede
area_parede = largura * altura

# Cálculo da quantidade de tinta necessária (1 litro pinta 2m²)
litros_tinta = area_parede / 2

# Exibição dos resultados
print(f"A área da parede é de {area_parede} m²")
print(f"Você precisará de {litros_tinta:.2f} litros de tinta para pintar essa parede")
