from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # carrega seu index.html

@app.route('/verificar', methods=['POST'])
def verificar():
    try:
        linhas = int(request.form['linhas'])
        colunas = int(request.form['colunas'])
        
        if colunas > linhas:
            return jsonify({'mensagem': 'A sua matriz é LD (Linearmente Dependente).'})

        # Monta matriz nula
        matrizP = []
        for i in range(linhas):
            vetorAux = [0] * colunas
            matrizP.append(vetorAux)
        
        matrizP = np.array(matrizP)
        matrizAux = np.zeros((linhas, 1))
        
        try:
            solution = np.linalg.solve(matrizP, matrizAux)
            return jsonify({'mensagem': f'A matriz é LI (Linearmente Independente): {solution.tolist()}'})
        except np.linalg.LinAlgError:
            return jsonify({'mensagem': 'Matriz dos coeficientes é LD (Linearmente Dependente).'})

    except Exception as e:
        return jsonify({'mensagem': f'Erro: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
