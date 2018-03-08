'''1- Escreva um programa que armazene uma lista com o título dos conteúdos que já aprendemos.

lista =('Operações Matemática', 'Print', 'Str', 'Input', 'Int', 'If', 'Else', 'Elif', 'Float', 'Função', 'Boolean',
'In', 'Or', 'And', 'Def', 'Min', 'Max', 'Sorted', 'Break', 'Random',  'For', 'While', 'Range',  'Lista', 'Turples')

print(lista)

2- Escreva um programa que armazene uma lista com o título dos conteúdos que já aprendemos e mostre os dois últimos
itens.

lista =('Operações Matemática', 'Print', 'Str', 'Input', 'Int', 'If', 'Else', 'Elif', 'Float', 'Função', 'Boolean',
'In', 'Or', 'And', 'Def', 'Min', 'Max', 'Sorted', 'Break', 'Random',  'For', 'While', 'Range',  'Lista', 'Turples')

print(lista[23:25])

3- Escreva um programa que armazene uma lista com o título dos conteúdos que já aprendemos e adicione um item da
 aula de hoje.

 lista =['Operações Matemática', 'Print', 'Str', 'Input', 'Int', 'If', 'Else', 'Elif', 'Float', 'Função', 'Boolean',
'In', 'Or', 'And', 'Def', 'Min', 'Max', 'Sorted', 'Break', 'Random',  'For', 'While', 'Range',  'Lista', 'Turples']

lista.append('Append')
print(lista)

4- Escreva um programa que receba uma palavra  com mais de cinco letras e troque as últimas letras pela palavra gato.
EX: comida = cogato'''


'''palavra = input('Digite uma palavra: ')
qtd_letras = len(palavra)
final = qtd_letras - 4 

if qtd_letras >= 5:
	final = palavra[0:final]
	print(final + 'gato')

else:
	print('Digite uma palavra maior: ')'''

mulheres_inspiradoras = ['Ada Lovelace', 'Frida', 'Margareth Hamilton']

fatia = mulheres_inspiradoras[1:4]

print(fatia)