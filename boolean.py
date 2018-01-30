# Exercicio boolean idade:
idade = int(input())

if idade > 18: 
	print('É Maior')
else:
	print('É Menor')











# Exercicio boolean:
if 10 > 5: 
	print('verdadeiro')
else:
	print('não é não')











# Crie um proclama que receba a idade de uma pessoa e verifique se ela pode voltar com a idade

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade >= 18:
	print(nome + ' tem ' + str(idade) + ' anos e pode voltar')
else:
	print(nome + ' tem ' + str(idade) + ' anos e não pode voltar')










# Exercicio se pode voltar a partir do ano que nasceu:
nome = input('Digite seu nome: ')
ano = int(input('Digite o ano em que você nasceu: '))

if ano <= 2000:
	print(nome + ' tem ' + str(ano) + ' anos e é obrigatório voltar')
elif ano <= 2002:
	print(nome + ' tem ' + str(ano) + ' anos e não é obrigatório voltar')
else:
	print(nome + ' tem ' + str(ano) + ' anos e não pode voltar')










# Exercicio se é impar ou par e negativo ou positivo:
numero = int(input('Digite um número: '))

if numero < 0 and numero % -2 ==  -1:
	print(str(numero) + ' NEGATIVO IMPAR ')
elif numero < 0 and numero % -2 == 0:
	print(str(numero) + ' NEGATIVO PAR ')
elif numero > 0 and numero % 2 ==  1:
	print(str(numero) + ' POSITIVO IMPAR')
elif numero > 0 and numero % 2 ==  0:
	print(str(numero) + ' POSITIVO PAR')
elif numero == 0:
	print(str(numero) + ' NULL')








# Exercicio do ano bissexto:
ano = int(input('Digite um ano: '))

if ano % 4 == 0:
 print('Esse ano é um ano bissexto')
else:
	print('Esse ano não é bissexto')
