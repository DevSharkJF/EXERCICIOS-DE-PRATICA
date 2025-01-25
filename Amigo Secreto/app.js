//O principal objetivo deste desafio é fortalecer suas habilidades em lógica de programação. Aqui você deverá desenvolver a lógica para resolver o problema.
let amigos = [];

function listarAmigos() {
    const listaAmigos = document.getElementById('listaAmigos');
    listaAmigos.innerHTML = '';
    amigos.forEach((amigo, index) => {
        const li = document.createElement('li');
        li.textContent = amigo;
        listaAmigos.appendChild(li);
    });
}

function adicionarAmigo() {
    const input = document.getElementById('amigo');
    const nome_amigo = input.value.trim();
    if (nome_amigo) {
        amigos.push(nome_amigo);
        input.value = '';
        listarAmigos();
    }
}

function sortearAmigo() {
    if (amigos.length === 0) {
        alert('Adicione pelo menos um amigo para sortear');
        return;
    }
    const indice = Math.floor(Math.random() * amigos.length);
    const sorteado = amigos[indice];
    const resultado = document.getElementById('resultado');
    limparLista();
    resultado.innerHTML = `<li>O amigo sorteado foi:</li> <br> <li>${sorteado.toUpperCase()}</li>`;
    
}

function limparLista(){
    amigos = [];
    document.getElementById('listaAmigos').innerHTML = '';
    document.getElementById('resultado').innerHTML = '';
}