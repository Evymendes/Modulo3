# Mostre uma sequência de números de 1 a 10.
for numero in range(1,11):
	print(numero)

# Mostre um programa que imprima todos os números pares 1 a 1000.
for par in range(1,1000,2):
	print('Número Par: ' + str(par))

# Mostre um programa para listar todos os números ímpares 1 a 1000.
for par in range(1,1000,3):
	print('Número Par: ' + str(par))

''' Maria tem que tomar remedio em 15 em 15 minutos escreva um programa 
que mostre todos os horários em que Maria precisa tomar o remério num periodo de 1 dia.'''

dia = 365

for dia in range(0,60,15):
	print(dia)