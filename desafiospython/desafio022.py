nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))