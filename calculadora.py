refazer = 'sim'
while refazer == 'sim':
    n1 = int (input ('qual é o primeiro número?' ))
    n2 = int (input ('qual é o segundo número?' ))
    operação = input ('qual operação você deseja usar?')
    if operação == 'soma':
        print('O resultado da soma é' ,n1 + n2,)
    elif operação == 'subtração':
        print ('O resultado da subtração é' ,n1 - n2,)
    elif operação == 'multiplicação':
        print ('O resultado da multiplicação é' ,n1 * n2,)
    elif operação == 'divisão':
        if n2 == 0:
            print('indefinido')
        else:
            print ('O resultado da divisão é' ,n1 / n2,)
    else:
        print ('essa operação não existe, tente: soma, subtração, multiplicação ou divisão')
    refazer = input ('Deseja fazer outra conta? [sim/nao]')

