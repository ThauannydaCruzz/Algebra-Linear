# 📚 Álgebra Linear - Verificação de LI e LD

[![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-blue)](https://flask.palletsprojects.com/)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)

**Álgebra Linear - Verificação de Linearidade das Matrizes (LI/LD)** é uma aplicação web desenvolvida com o propósito de verificar se uma matriz é **Linearmente Independente (LI)** ou **Linearmente Dependente (LD)**. Este projeto tem o foco em aplicar conceitos de Álgebra Linear e resolver problemas clássicos de sistemas lineares de uma forma prática e acessível.

A aplicação foi construída com **Flask**, uma framework web de Python, e utiliza a biblioteca **NumPy** para os cálculos matemáticos. A interface é simples e permite a visualização direta do resultado.

---

## 🧠 Funcionalidades

### 1. **Verificação de Linearidade**
   O sistema permite que o usuário insira as dimensões de uma matriz (número de linhas e colunas) e determina automaticamente se a matriz fornecida é **Linearmente Independente (LI)** ou **Linearmente Dependente (LD)**.

### 2. **Gerenciamento de Matriz Aleatória**
   Se o número de colunas for maior do que o número de linhas, a matriz é automaticamente considerada **LD**. Caso contrário, o sistema gera uma matriz aleatória e tenta resolver um sistema homogêneo, classificando-o com base em sua solução.

### 3. **Soluções**
   O sistema resolve o sistema linear homogêneo gerado e classifica a matriz:
   - **LI (Linearmente Independente)**: Caso exista uma solução única.
   - **LD (Linearmente Dependente)**: Caso o sistema tenha infinitas soluções.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: A linguagem de programação utilizada para implementar a lógica do projeto.
- **Flask**: Framework web em Python, usado para o backend da aplicação.
- **NumPy**: Biblioteca de álgebra linear em Python, utilizada para realizar as operações matriciais.
- **HTML5**: Linguagem de marcação usada para a construção da interface gráfica.

---

## 💡 Como Funciona?

A aplicação trabalha com o conceito de **Matrizes Lineares**. Quando o usuário informa o número de **linhas** e **colunas**, o sistema verifica a possibilidade de independência linear da matriz que será formada.

### Algoritmo

1. O usuário define o número de **linhas** e **colunas**.
2. Se o número de colunas for maior que o número de linhas, a matriz será automaticamente considerada **Linearmente Dependente (LD)**.
3. Caso contrário, o sistema gera uma matriz de **coeficientes aleatórios** utilizando a biblioteca **NumPy**.
4. Em seguida, um sistema homogêneo é gerado (com o vetor de constantes sendo preenchido por zeros).
5. A matriz gerada é resolvida com a função **np.linalg.solve()**:
   - Se houver uma **única solução**, a matriz é **Linearmente Independente (LI)**.
   - Caso o sistema não tenha solução única, ou seja, se for possível uma infinidade de soluções, a matriz é **Linearmente Dependente (LD)**.
   
### Resultados da Análise

A análise resultante pode ser:

- **LI (Linearmente Independente)**: A matriz possui uma solução única.
- **LD (Linearmente Dependente)**: A matriz possui soluções infinitas ou não tem solução.

---

## 📥 API (Interna)

### Endpoints

#### 1. **POST /verificar**
Esse endpoint realiza a verificação de linearidade de uma matriz de acordo com as dimensões informadas (linhas e colunas).

##### Parâmetros esperados:
| Parâmetro  | Tipo  | Descrição                        |
|:---------:|:-----:|:---------------------------------|
| `linhas`  | int   | Número de linhas da matriz       |
| `colunas` | int   | Número de colunas da matriz      |


## 🚀 Implementação de Exemplo

### Tela Inicial
Na interface web, o usuário pode informar os valores de **linhas** e **colunas** para a matriz.

### Exemplo de Execução:
1. Usuário escolhe **3 linhas** e **3 colunas**.
2. A aplicação gera uma matriz de **3x3** com valores aleatórios.
3. O sistema resolve o sistema linear e retorna se a matriz é **LI (Linearmente Independente)** ou **LD (Linearmente Dependente)**.

---

## 🏗️ Possíveis Melhorias
- **Interface Gráfica**: Melhoria na interface de usuário com gráficos interativos para visualização das matrizes.
- **Validação de Dados**: Adicionar validações para garantir que o usuário insira valores corretos (linhas e colunas).
- **Exibição de Resultados**: Mostrar as soluções dos sistemas lineares para mais transparência.
- **Suporte a Matrizes Grandes**: Permitir a manipulação e verificação de matrizes maiores de forma mais eficiente.

---

## 👩‍💻 Desenvolvedores
**Gabriela Akemi** e **Thauanny da Cruz**
