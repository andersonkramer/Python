fruta = 'Limao'
fruta2 = 'Abacate'
type(fruta)

#Imprimir variáveis %s = String %d = Decimal %f = Float
print('Suco de %s com %s é o meu favorito' %fruta, %fruta2)

#Outro método
print('Suco de {} é o meu favorito'.format(fruta))

#Com mais variaveis
print('Suco de {0} com {1} é o meu favorito'.format(fruta, fruta2))

#Formatacao com números diminuindo as casas decimais
conta = 17/3
print('O Resultado da conta é {:.2f}'.format(conta))

