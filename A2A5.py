precoProd = float(input('Digite o preço do produto: '))
cJuros = (precoProd * 5 / 100) + precoProd
cJurosParc = cJuros / 3
duasParc = precoProd / 2
sJuros = precoProd - (precoProd * 5 / 100)
print('O produto parcelado em 3 vezes ficará com o preço da parcela de: r$' + str(cJurosParc) + ' e preço total de r$' + str(cJuros) + '.')
print('O produto parcelado em 2 vezes ficará com o preço da parcela de: r$' + str(duasParc) + ' e preço total de r$' + str(precoProd) + '.')
print('O produto á vista ficará: r$', sJuros)
