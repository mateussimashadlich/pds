function obterMilitares() {
	$.ajax({
		url: "http://127.0.0.1:8000/exercito/militares",
		method: "GET",
		dataType: "json",
		success: listarMilitares,
		error: function () {
			alert("Ocorreu um erro ao listar os militares!");
		},
	});
}

function listarMilitares(militares) {
	if (militares.length == 0) {
		linha = `
            <tr>
                <td colspan=3>Nenhum militar registrado</td>
            </tr>
        `;
		$("#table-body").append(linha);
	} else {
		militares.forEach((militar) => {
			var batalhao_atual;
			if (militar.batalhao_atual == undefined) {
				batalhao_atual = "N/A";
			} else {
				$.when(obterBatalhao(militar.batalhao_atual)).done(function (
					batalhao
				) {
					batalhao_atual = batalhao.nome;
				});
			}
			$.when(obterPessoa(militar.pessoa)).done(function (pessoa) {
				linha = `
                    <tr>
                        <td>${pessoa.nome}</td>
                        <td>${pessoa.idade} anos</td>
                        <td>${pessoa.peso}kg</td>
                        <td>${pessoa.altura}cm</td>
                        <td>${militar.patente}</td>
                        <td>${batalhao_atual}</td>
                        <td>${militar.ano_ingresso}</td>
                    </tr>
                `;
				$("#table-body").append(linha);
			});
		});
	}
}

function obterPessoa(id) {
	return $.ajax({
		url: "http://127.0.0.1:8000/exercito/pessoas/" + id,
		method: "GET",
		dataType: "json",
	});
}

function obterBatalhao(id) {
	return $.ajax({
		url: "http://127.0.0.1:8000/exercito/batalhoes/" + id,
		method: "GET",
		dataType: "json",
	});
}

window.onload = obterMilitares;
