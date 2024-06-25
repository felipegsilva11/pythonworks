# Ler o salário atual do funcionário
#salario_atual = float(input("Digite o salário atual do funcionário: "))

# Calcular o novo salário com aumento de 15%
#novo_salario = salario_atual * 1.15  # Multiplicar por 1.15 para aumentar 15%

# Exibir o novo salário com aumento
#print(f"O novo salário com 15% de aumento é: R$ {novo_salario:.2f}")



salario = float(input('Qual é o salario do funcionario R$'))
novo = salario + (salario * 15 / 100)
print('um funcionario que ganhava R${:.2f}, com 15% de aumentro, passa a receber R${:.2f}'.format(salario, novo))