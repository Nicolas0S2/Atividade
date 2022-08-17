altura = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro: '))
areaCilindro = 2 * 3.14 * raio * (raio + altura)
quantidadeLatas = (areaCilindro / 3) / 5
custo = quantidadeLatas * 50
print(areaCilindro)
print('A quantidade de latas necessárias é de: ', quantidadeLatas)
print('O custo será de: ', custo)
