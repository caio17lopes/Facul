function exibirMensagem()
    {
    const mensagem = "Nunca desista dos seus sonhos, nem por causa da idade ou por achar que não tem capacidade. Esforço vale mais que talento!"
    let elemento = document.getElementById("mensagem").textContent = mensagem;
    
    if (!elemento){
        elemento = document.createElement("p");
        elemento.id = "mensagem";
        document.querySelector("button").insertAdjacentElement("afterend", elemento);
        }
    elemento.textContent = mensagem;
    }