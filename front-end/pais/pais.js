function obterPaises(){
    $.ajax({
        url: 'http://127.0.0.1:8000/exercito/paises',
        method: 'GET',
        dataType: 'json',
        success: listarPaises,
        error: function(){
            alert("Ocorreu um erro ao listar os países!")
        }
    })
}

function listarPaises(paises){
    if (paises.length == 0){
        linha = `
            <tr>
                <td colspan=3>Nenhum país registrado</td>
            </tr>
        `
        $("#table-body").append(linha)
    }
    else{
        paises.forEach(pais => {
            linha = `
                <tr>
                    <td>${pais.nome}</td>
                    <td>${pais.continente}</td>
                    <td>${pais.tamanho}</td>
                </tr>
            `
            $("#table-body").append(linha)
        });
    }
}

window.onload = obterPaises;
