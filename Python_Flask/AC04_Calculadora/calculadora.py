from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main_page():
    return "verifique a URL /calc e /resultado"

@app.route("/calc")
def exibe_calculadora():
    html = '''
    <form action="/resultado">
    a <input type="number" name="a" id="a"> <br>
    b <input type="number" name="b" id="b"> <br>
    multiplicação: <input type="radio" name="ope" value="mult" required> <br>
    divisão: <input type="radio" name="ope" value="div"> <br>
    soma: <input type="radio" name="ope" value="soma"> <br>
    subtracao: <input type="radio" name="ope" value="sub">
    <button type="submit">calcular</button>
    </form>

    Implemente as operacoes! Teste com o arquivo runtests_calculadora.py
    '''
    return html

@app.route("/resultado")
def resultado():
    if 'a' in request.args and 'b' in request.args and 'ope' in request.args:
        a = int(request.args['a'])
        b = int(request.args['b'])
        ope = request.args['ope']
        if ope == 'soma':
            resultado = a + b
        elif ope == 'mult':
            resultado = a * b
        elif ope == 'sub':
            resultado = a - b
        elif ope == 'div':
            if b == 0:
                resultado = 'Erro divisão por Zero'
            else:
                resultado = a / b
            
    return str(resultado)


app.run(debug=True)