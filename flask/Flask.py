'''Flask é uma fremiorque para fazer mini serviço
Django
Falcon Python
main = arquivo principal 
def = função
crie duas rotas uma com todas as receitas e outra com nome da receita...'''

from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
	return 'Hello Word!!!'

@app.route("/receita/")
def receita():
	return '° Bolo de Coco'

@app.route("/receita/<bolodecoco>")
def Receita(bolodecoco):
	return '<h1>Bolo de Coco</h1> <h2>INGREDIENTES</h2> <h3>MASSA: </h3><br> 2 xícaras (chá) de açúcar <br> 2 xícaras (chá) de farinha de trigo <br> 4 ovos <br> 1 xícara (chá) leite <br> 2 colheres (sopa) coco ralado <br> 1 colher (sopa) fermento em pó <br> 2 colheres (sopa) margarina sem sal  <br> <h3>CALDA:</h3>  <br> 1 lata de leite condensado <br> 1 vidro (200ml) leite de coco <br> 1 xícara de coco ralado<h2>MODO DE PREPARO</h2> <h3>MASSA:</h3> <br> Bata no liquidificador os ovos, o leite, a margarina, o açúcar e o coco <br> Coloque o trigo em uma vasilha, despeje a massa batida e misture até que fique homogêneo <br> Adicione o coco e misture <br> Por último, acrescente o fermento <br> Coloque em forma untada e enfarinhada <br> Asse em forno médio, preaquecido, por cerca de 40 minutos, ou até dourar <br> <h3>COBERTURA:</h3> <br> Misture tudo (não precisa levar ao fogo), coloque sobre o bolo ainda quente e polvilhe coco ralado <br> Leve para gelar! %s!' % bolodecoco 

@app.route("/")
def index():
	return "ERRO <BR> Digite / e qualquer coisa depois do 5000 ", 404

@app.route("/<nome>")
def certo(nome):
	return "{}".format(nome), 200

if __name__ == '__main__':
	app.run(debug = True)
