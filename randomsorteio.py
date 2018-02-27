import random

sorteio = random.randint(1,30)
tentativas = 0

while tentativas < 3 :
	tente = int(input('Digite um número de 1 à 30: '))
	print(sorteio)
	tentativas = tentativas + 1

	if tente == sorteio:
		print('Você acertou na ' + str(tentativas) + ' tentativa!')
		break

else:
	print('Não foi desta vez... O número sorteado foi: ' + str(sorteio))


