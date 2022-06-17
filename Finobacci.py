n1 = 1
n2 = 0
soma = 0
f = 0
print('Sequência de Finobacci!')
l = int(input('Digite um numero maior que 0 e veja seu correspondente na sucessão de Finobacci!\n'))

for f in range(0,l):

    soma = n1 + n2
    n2 = n1
    n1 = soma
    print('Sequência de Finobacci {}'.format(soma))