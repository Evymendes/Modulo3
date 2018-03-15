'''Crie um programa que receba a idade de uma pessoa 
e verifique se ela pode votar

entrada: 21 dalianny
saida: dalianny tem 21 anos e pode votar'''

nome = input(' Qual o seu nome? ')
idade = int(input(' Sua idade? '))

if idade > 18:
	print(nome + ' tem ' + str(idade) + ' anos é obrigado a votar ')

elif idade >= 16:
	print(nome + ' tem ' + str(idade) + ' vota se quiser ')

else:
	print(nome + ' tem ' + str(idade) + ' não pode votar')