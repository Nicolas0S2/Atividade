hora = int(input('Digite o horário (hora): '))
min = int(input('Digite o horário (minutos): '))
segs = int(input('Digite o horário (segundos): '))
minSegs = min * 60
horaMin = hora * 60
horaSegs = horaMin * 60
totSegs = segs + minSegs + horaSegs
totMin = horaMin + min
print('O total de Minutos do dia de hoje é de: ', totMin)
print('O total de Segundos do dia de hoje é de: ', totSegs)
