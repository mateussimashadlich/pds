$("#form_exercito").on("submit", function (event) {
	criarObjeto(
		event,
		"http://127.0.0.1:8000/exercito/exercitos",
		"form_exercito",
		"Exército"
	);
});

function obterPaises() {
	$.ajax({
		url: "http://127.0.0.1:8000/exercito/paises",
		method: "GET",
		dataType: "json",
		success: adicionarPaisesAoSelect,
		error: function () {
			alert("Ocorreu um erro ao carregar os países!");
		},
	});
}

function adicionarPaisesAoSelect(paises) {
	paises.forEach((pais) => {
		option = `<option value=${pais.id}>${pais.nome}</option>`;
		$("#pais").append(option);
	});
}

window.onload = obterPaises;
