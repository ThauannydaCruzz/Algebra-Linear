from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

def escalonamento_com_explicacao(matriz):
    explicacao = ""
    matriz = matriz.astype(float)
    linhas, colunas = matriz.shape
    explicacao += "Matriz aumentada (A | 0) inicial:\n"
    explicacao += str(matriz) + "\n\n"

    for i in range(min(linhas, colunas - 1)):
        if np.isclose(matriz[i][i], 0):
            for k in range(i + 1, linhas):
                if not np.isclose(matriz[k][i], 0):
                    matriz[[i, k]] = matriz[[k, i]]
                    explicacao += f"Troca L{i+1} com L{k+1} para obter pivô não nulo:\n"
                    explicacao += str(matriz) + "\n\n"
                    break
        for k in range(i + 1, linhas):
            if not np.isclose(matriz[i][i], 0):
                fator = matriz[k][i] / matriz[i][i]
                matriz[k] -= fator * matriz[i]
                explicacao += (
                    f"Eliminação abaixo do pivô na coluna {i+1}:\n"
                    f"L{k+1} ← L{k+1} - ({fator:.2f})·L{i+1}\n"
                    + str(matriz) + "\n\n"
                )
    return matriz, explicacao

def calcular_posto(matriz):
    return sum(not np.allclose(linha[:-1], 0) for linha in matriz)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    try:
        linhas = int(request.form['linhas'])
        colunas = int(request.form['colunas'])

        matriz = []
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                valor = float(request.form.get(f'valor_{i}_{j}', '0'))
                linha.append(valor)
            matriz.append(linha)

        matriz = np.array(matriz)

        if colunas > linhas:
            return jsonify({'mensagem': 'Mais colunas do que linhas ⇒ Matriz é LD (Linearmente Dependente).'})

        vetor_nulo = np.zeros((linhas, 1))
        matriz_estendida = np.hstack((matriz, vetor_nulo))

        matriz_escalonada, explicacao = escalonamento_com_explicacao(matriz_estendida.copy())
        posto = calcular_posto(matriz_escalonada)

        explicacao += f"Posto da matriz dos coeficientes (A): {posto}\n"
        explicacao += f"Número de variáveis: {colunas}\n\n"

        if posto == colunas:
            resultado = "A matriz é LI (Linearmente Independente) ⇒ única solução trivial x = 0."
        else:
            resultado = "A matriz é LD (Linearmente Dependente) ⇒ sistema com infinitas soluções."

        return jsonify({'mensagem': resultado, 'explicacao': explicacao})

    except Exception as e:
        return jsonify({'mensagem': f'Erro: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
