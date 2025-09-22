from flask import Flask, render_template, request, redirect, url_for 
from modelos import Livro, Estante 
app = Flask(__name__)
minha_estante = Estante()
@app.route('/') 
def pagina_inicial():
    """ Rota principal. Exibe a estante de livros. """ 
   
    livros_na_estante = minha_estante.livros 
    
    return render_template('estante.html', livros=livros_na_estante) 
    
@app.route('/adicionar', methods=['POST']) 
def adicionar_livro():  
    """ Rota que recebe os dados do formulário para adicionar um novo livro.
    """
    titulo = request.form['titulo'] 
    autor = request.form['autor'] 
    
   
    novo_livro = Livro(titulo=titulo, autor=autor)
    
    
    minha_estante.adicionar_livro(novo_livro) 
    
    
    return redirect(url_for('pagina_inicial'))

   
    if __name__ == '__main__': app.run(debug=True)