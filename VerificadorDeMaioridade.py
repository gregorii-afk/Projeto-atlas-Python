refazer = 'sim'
while refazer == 'sim':
    idade = int(input('Qual a sua idade?: '))
    if idade >= 18:
        print ('Você é maior de idade, está liberado.')
    else:
        print ('Você não pode entrar, é menor de 18 anos')
    refazer = input('Você quer testar outra idade? [sim/nao] ')