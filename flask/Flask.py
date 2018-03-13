'''Flask é uma fremiorque para fazer mini serviço
Django
Falcon Python
''' 
'''crie duas rotas uma com todas as receitas e outra com nome da receita...'''

from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
	return 'Hello Word!!!'

@app.route("/receita")
def receita():
	return 'Receita!!!'

@app.route("/nomeReceita")
def nomeReceita():
	return 'Bolo de Coco'

if __name__ == '__main__':
	app.run(debug = True)
