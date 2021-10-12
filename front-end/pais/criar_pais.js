function obterContinentes() {
	$.ajax({
		url: "http://127.0.0.1:8000/exercito/paises/continentes",
		method: "GET",
		dataType: "json",
		success: adicionarContinentesAoSelect,
		error: function () {
			alert("Ocorreu um erro ao carregar os continentes!");
		},
	});
}

function adicionarContinentesAoSelect(continentes) {
	continentes.forEach((continente) => {
		option = `<option value=${continente.valor}>${continente.nome}</option>`;
		$("#continente").append(option);
	});
}

window.onload = obterContinentes;

$("#form_pais").on("submit", function (event) {
	criarObjeto(
		event,
		"http://127.0.0.1:8000/exercito/paises",
		"form_pais",
		"País"
	);
});
