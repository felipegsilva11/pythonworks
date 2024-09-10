num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
      [ 1 ] Converter para BINÁRIO
      [ 2 ] Converter para OCTAL
      [ 3 ] Converter para HEXADECIMAL''')
opcão = int(input('Sua opção: '))
if opcão == 1:
    print('{} converter para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif opcão == 2:
    print('{} converter para OCTAL é igual a {}'.format(num, oct(num) [2:]))
elif opcão == 3:
    print('{} converter para HEXADECIMAL é igual a {}'.format(num, hex(num) [2:]))
else:
    print('Opção inválida. Tente novamente.')