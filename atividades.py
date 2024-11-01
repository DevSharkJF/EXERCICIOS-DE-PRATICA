"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

print('VERIFICAÇÃO DE PAR/ÍMPAR')
numero = input('Digite um número inteiro: ')
if numero.isdigit():
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print('Você digitou um número par')
    else:
        print('Você digitou um número ímpar')

else:
    print('Você não digitou um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = int(input('Informe a hora: '))
if horario >= 0 and horario <= 11:
    print('Bom dia!')
elif horario >= 12 and horario <= 17:
    print('Boa Tarde')
elif horario >= 18 and horario <= 23:
    print('Boa Noite')
#========================================================
entrada = input('Digite a hora em números inteiros: ')
try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Informe seu nome: ')
tamanho = len(nome)
if tamanho > 1 and tamanho <= 4:
    print('Seu nome é curto')
if tamanho >= 5 and tamanho <= 6:
    print('Seu nome é normal')
if tamanho > 6:
    print('Seu nome é muito grande')
#========================================================
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
