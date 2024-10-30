"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'shark'
acertos = ''
tentativas = 0

while True:
    letra = input('Informe uma letra: ')
    tentativas += 1

    if len(letra) > 1:
        print('Apenas uma letra por vez!')
        continue
    
    if letra in palavra_secreta:
        acertos += letra
    else:
        print('Letra incorreta, tente novamente')
    
    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in acertos:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print('Palavra Formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ DESCOBRIU A PALAVRA SECRETA!')
        print('TENTATIVAS: ', tentativas)
        print('A PALAVRA SECRETA ERA: ', palavra_secreta)
        break
