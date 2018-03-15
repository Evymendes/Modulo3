funcionario = input('Nome do funcionario? \n')

hrtrab = int(input('Horas trabalhadas \n'))

valorhr = float(input('Valor das horas trabalhadas\n'))

salario = hrtrab * valorhr

print( 'O funcionario ' + funcionario + ' trabalhou ' + str(hrtrab) + ' horas no mês. \nA hora trabalhada vale R$ ' + str( '%.2f' % valorhr) + '. \nSeu sálario é de R$ ' + str(  '%.2f' % salario))
