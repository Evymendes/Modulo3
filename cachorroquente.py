preço = int(input('Valor do Hot-Dog?\n'))

cliente = input('Nome do cliente?\n')

quant = int(input('Quantos Hot-Dog?\n'))

pagar = preço * quant

print('O cliente ' + cliente + ' comprou ' + str(quant) + ' cachorros quentes e vai pagar R$ ' + str('%.2f'% pagar ))