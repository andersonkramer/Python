#Exercício 07 Comando FOR
for i in range(5):
    print(i)
#Comando While e Break com contagem de tempo
import time
contador = 0
while contador < 10:
    print('agora não ainda é {}'.format(contador))
    contador = contador + 1
    if contador == 7:
        break
    time.sleep(contador)
print('agora sim finalizou a contagem com {}'.format(contador))

#exercicio calculando o fatorial de um numero

import time
numero = int(input('Digite um número'))
resultado = 1
while numero > 1:
    resultado = resultado * numero
    print('O Resultado Parcial é {}'.format(resultado))
    numero = numero - 1
    time.sleep(1)
print('Resultado total é {}'.format(resultado))
