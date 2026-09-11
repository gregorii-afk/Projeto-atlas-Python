temp = float(input('Qual temperatura você quer converter? '))
ent = input('Qual é a escala dessa temperatura? [cs/fh/k]')
esc = input('Para qual escala você quer converter? [cs/fh/k] ')
if ent == esc:
    print('O resultado é o mesmo valor. ')
elif ent == 'cs' and esc == 'fh':
    resultado = ((temp * 9/5) + 32)
    print(resultado,'Fº')
elif ent == 'fh' and esc == 'cs':
    resultado = ((temp - 32) * 5/9)
    print(resultado,'Cº')
elif ent == 'cs' and esc == 'k':
    resultado = (temp + 273.15)
    print(resultado,'Kº')
elif ent == 'k' and esc == 'cs':
    resultado = (temp - 273.15)
    print(resultado,'Cº')
elif ent == 'fh' and esc == 'k':
    resultado = ((temp - 32) * 5/9 + 273.15)
    print(resultado,'Kº')
elif ent == 'k' and esc == 'fh':
    resultado = ((temp - 273.15) * 9/5 + 32)
    print(resultado,'Fº')
else:
    print('Desculpe, essa escala é inválida. ')