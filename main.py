from flask import Flask
app = Flask('app')

@app.route('/')
def index():
  return '<h1>Olá Mundo!</h1>'

@app.route('/unifran')
def unifra():
    return '<h2>Universidade de Franca</h2>:'
  
@app.route('/dashboard/<name>')
def dashboard (name):
 return f'Olá, {name}'
@app.route('/prod/<name>/<int:qtd>')
def prod(name, qtd):
 return f'{name} - {qtd}'
  
if __name__ =='__main__':
  app.run(host='0.0.0.0', port=8080)