const form_criar_calendario = document.getElementById("form_criar_calendario");
const nome_calendario = document.getElementById("nome_calendario");
const descricao_calendario = document.getElementById("descricao_calendario");
const erro_nome = document.getElementById("erro_nome");
const erro_descricao = document.getElementById("erro_descricao");
const mensagem_sucesso = document.getElementById("mensagem_sucesso");

form_criar_calendario.addEventListener("submit", function (evento) {
    evento.preventDefault();

    limpar_erros();

    const nome = nome_calendario.value.trim();
    const descricao = descricao_calendario.value.trim();
    let formulario_valido = true;

    if (nome.length < 3) {
        erro_nome.textContent = "Informe um nome com pelo menos 3 caracteres.";
        nome_calendario.classList.add("campo_invalido");
        formulario_valido = false;
    }

    if (descricao.length < 5) {
        erro_descricao.textContent = "Informe uma descrição com pelo menos 5 caracteres.";
        descricao_calendario.classList.add("campo_invalido");
        formulario_valido = false;
    }

    if (!formulario_valido) {
        return;
    }

    mensagem_sucesso.textContent = "Calendário criado com sucesso!";
    mensagem_sucesso.style.display = "block";

    form_criar_calendario.reset();

});

function limpar_erros() {
    erro_nome.textContent = "";
    erro_descricao.textContent = "";

    nome_calendario.classList.remove("campo_invalido");
    descricao_calendario.classList.remove("campo_invalido");

    mensagem_sucesso.style.display = "none";
}

function cancelar_criacao() {
    window.history.back();
}