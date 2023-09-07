"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.
"""
soma = 0
cont = 0
for contador in range(0, 7):
    num = int(input('Digite o {} valor: '.format(contador)))
    soma = soma + num
    cont = cont + 1
print('Você informou {} numeros que soma {}'.format(cont, soma))
