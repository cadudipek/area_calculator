print('==================')
print('Calculadora de área')
print('==================')

# menu
print('1) Quadrado')
print('2) Retângulo')
print('3) Triângulo')
print('4) Círculo')
print('5) Sair')

# input do seletor
selector = int(input('Selecione o formato: '))

# Quadrado
if selector == 1:
    side = int(input('Qual o tamanho do lado do quadrado? '))
    area = side ** 2
    print(f'A área é {area}')

# Retângulo
elif selector == 2:
    length = int(input('Qual o comprimento? '))
    width = int(input('Qual a largura? '))
    area = length * width
    print(f'A área é {area}')

# Triângulo
elif selector == 3:
    height = int(input('Qual a altura? '))
    base = int(input('Qual a base do triângulo? '))
    area = (height * base) / 2
    print(f'A área é {area}')

# Círculo
elif selector == 4:
    pi = 3.14
    radius = int(input('Qual o raio do círculo? '))
    area = pi * (radius ** 2)
    print(f'A área é {area}')

# Sair
else:
    print('O programa será encerrado')
