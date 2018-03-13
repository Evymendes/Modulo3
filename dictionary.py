'''
sammy = {
	'username': 'sammy-shark', 
	'online': true, 
	'followers': 987
}

1- Escreva um dicionário sobre o perfil de um usuário do Gitbub.
2- Adicione novos campos a esse dicionários
3- Exiba esse dicionário mostrando cada chave e valor.

'''

username = {
	'username': 'Evelyn', 
	'repositorios': '19', 
	'followers': '1'
}

print('username')


username = {
	'username': 'Evelyn', 
	'repositorios': '19', 
	'followers': '1'
}

username ['following'] = '1'

print(username)

username = {
	'username': 'Evelyn', 
	'repositorios': '19', 
	'followers': '1'
}

del username['repositorios']

print(username)

for key in username:
	print(key + ':\t' + username[key])