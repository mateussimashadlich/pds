function obterPessoas(){
    $.ajax({
        url: 'http://127.0.0.1:8000/exercito/pessoas',
        method: 'GET',
        dataType: 'json',
        success: listarPessoas,
        error: function(){
            alert("Ocorreu um erro ao listar as pessoas!")
        }
    })
}

function listarPessoas(pessoas){
    if (pessoas.length == 0){
        linha = `
            <tr>
                <td colspan=3>Nenhuma pessoa registrada</td>
            </tr>
        `
        $("#table-body").append(linha)
    }
    else{
        pessoas.forEach(pessoa => {
            linha = `
                <tr>
                    <td>${pessoa.nome}</td>
                    <td>${pessoa.idade}</td>
                    <td>${pessoa.peso}</td>
                    <td>${pessoa.altura}</td>
                </tr>
            `
            $("#table-body").append(linha)
        });
    }
}

window.onload = obterPessoas;
