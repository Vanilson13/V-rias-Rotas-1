from flask import Flask
app = Flask('app')

@app.route('/')
def index():
  return '<h1>Olá Mundo!</h1>'

@app.route('/unifran')
def unifra():
    return '<h2>Universidade de Franca</h2>:'

@app.route('/dashboard/Eduardo')
def eduardo():
    return '<h3>Olá, Eduardo</h3>'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
