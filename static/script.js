document.addEventListener('DOMContentLoaded', () => {
    const formDimensoes = document.getElementById('form-dimensoes');
    const formMatriz = document.getElementById('form-matriz');
    const matrizInputs = document.getElementById('matriz-inputs');
    const resultadoDiv = document.getElementById('resultado');

    formDimensoes.addEventListener('submit', (e) => {
        e.preventDefault();
        const linhas = parseInt(document.getElementById('linhas').value);
        const colunas = parseInt(document.getElementById('colunas').value);

        matrizInputs.innerHTML = '';
        for (let i = 0; i < linhas; i++) {
            const rowDiv = document.createElement('div');
            for (let j = 0; j < colunas; j++) {
                const input = document.createElement('input');
                input.type = 'number';
                input.name = `valor_${i}_${j}`;
                input.required = true;
                input.style.width = '60px';
                input.style.margin = '2px';
                rowDiv.appendChild(input);
            }
            matrizInputs.appendChild(rowDiv);
        }

        const linhasInput = document.createElement('input');
        linhasInput.type = 'hidden';
        linhasInput.name = 'linhas';
        linhasInput.value = linhas;

        const colunasInput = document.createElement('input');
        colunasInput.type = 'hidden';
        colunasInput.name = 'colunas';
        colunasInput.value = colunas;

        formMatriz.appendChild(linhasInput);
        formMatriz.appendChild(colunasInput);

        formMatriz.style.display = 'block';
    });

    formMatriz.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(formMatriz);

        const response = await fetch('/verificar', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        resultadoDiv.textContent = data.mensagem;
    });
});
