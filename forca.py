import os
palavra = 'Carambola'
palavra_escondida = []

for letra in palavra:
    palavra_escondida.append('*')

acerto = 0

while acerto < len(palavra):
    os.system('clear')

    print(palavra_escondida)
    print('Quantidade de letras da palavra:', len(palavra))

    letra_escondida = input("Digite uma letra:")

    for indice, letra in enumerate(palavra):
        if letra_escondida == letra:
            palavra_escondida[indice] = letra_escondida
            acerto += 1

    print("\n")

    print('Parabéns! Você acertou a palavra')