nome = input(' Seu nome? \n')
ano = int(input('Seu ano de nascimento?\n'))

if ano < 2000:
	print('Você é obrigado a votar')

elif ano <= 2002:
	print('Vota se quiser')

else:
	print('Você não pode votar')