function calcular(tipo, valor) {
    if(tipo === 'acao') {
        if(valor === 'c') {
            document.getElementById('resultado').value = ''
        }
        if(valor === '+' || valor ==='-' || valor === '*' || valor === '*' || valor === '/' || valor === '.') {
            var valor_campo = document.getElementById('resultado').value
            document.getElementById('resultado').value = valor_campo + valor
            //Concatenação dos valores sem precisar de criar uma variável(+=):
            // document.getElementById('resultado').value += valor
        }
        if(valor === '='){
            var valor_campo = eval(document.getElementById('resultado').value)
            document.getElementById('resultado').value = valor_campo
        }
    } else if(tipo === 'valor') {
        var valor_campo = document.getElementById('resultado').value 
        document.getElementById('resultado').value = valor_campo + valor
        //Concatenação dos valores sem precisar de criar uma variável(+=):
        // document.getElementById('resultado').value += valor
    }
}