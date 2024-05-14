document.addEventListener("DOMContentLoaded", function() {
    // Seleciona todos os elementos <li> dentro da lista com a classe "list-group"
    var listaProcedimentos = document.querySelectorAll(".list-group li");

    // Itera sobre os elementos da lista
    listaProcedimentos.forEach(function(procedimento) {
        // Adiciona um evento de clique a cada elemento da lista
        procedimento.addEventListener("click", function() {
            // Remove a classe "selected" de todos os procedimentos
            listaProcedimentos.forEach(function(item) {
                item.classList.remove("selected");
            });
            
            // Adiciona a classe "selected" apenas ao procedimento clicado
            procedimento.classList.add("selected");

            // Recupera o nome do procedimento selecionado
            var procedimentoSelecionado = procedimento.textContent.trim();
            // Faça algo com o procedimento selecionado, como enviar para o backend para agendamento
            console.log("Procedimento selecionado:", procedimentoSelecionado);
        });
    });
});
