function obterExercitos() {
	$.ajax({
		url: "http://127.0.0.1:8000/exercito/exercitos",
		method: "GET",
		dataType: "json",
		success: listarExercitos,
		error: function () {
			alert("Ocorreu um erro ao listar os exércitos!");
		},
	});
}

function listarExercitos(exercitos) {
	if (exercitos.length == 0) {
		linha = `
            <tr>
                <td colspan=3>Nenhum exército registrado</td>
            </tr>
        `;
		$("#table-body").append(linha);
	} else {
		exercitos.forEach((exercito) => {
			$.when(obterPais(exercito.pais)).done(function (pais) {
				linha = `
                    <tr>
                        <td>${pais.nome}</td>
                        <td>${exercito.lema}</td>
                        <td>${exercito.ano_fundacao}</td>
                    </tr>
                `;
				$("#table-body").append(linha);
			});
		});
	}
}

function obterPais(id) {
	return $.ajax({
		url: "http://127.0.0.1:8000/exercito/paises/" + id,
		method: "GET",
		dataType: "json",
	});
}

window.onload = obterExercitos;
