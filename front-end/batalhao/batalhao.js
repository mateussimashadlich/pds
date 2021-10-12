function obterBatalhoes(){
    $.ajax({
        url: 'http://localhost:8000/exercito/batalhoes',
        method: 'GET',
        dataType: 'json',
        success: listarBatalhoes,
        error: function(){
            alert("Ocorreu um erro ao listar os batalhões!")
        }
    })
}

function listarBatalhoes(batalhoes){
    batalhoes.forEach(batalhao => {
        linha = `
            <tr>
                <td>${batalhao.nome}</td>
                <td>${batalhao.exercito}</td>
                <td>${batalhao.comandante}</td>
            </tr>
        `
        $("#table-body").append(linha)
    });
}

window.onload = obterBatalhoes;
