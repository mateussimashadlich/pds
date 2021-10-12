$("#form_batalhao").on("submit", function (event) {
	criarObjeto(
		event,
		"http://127.0.0.1:8000/exercito/batalhoes",
		"form_batalhao",
		"Batalhão"
	);
});

function obterExercitos() {
	$.ajax({
		url: "http://127.0.0.1:8000/exercito/exercitos",
		method: "GET",
		dataType: "json",
		success: adicionarExercitosAoSelect,
		error: function () {
			alert("Ocorreu um erro ao carregar os exércitos!");
		},
	});
}

function adicionarExercitosAoSelect(exercitos) {
	exercitos.forEach((exercito) => {
		$.when(obterPais(exercito.pais)).done(function (pais) {
			option = `<option value=${exercito.id}>${pais.nome} - ${exercito.lema}</option>`;
			$("#exercito").append(option);
		});
	});
}

function obterPais(id) {
	return $.ajax({
		url: "http://127.0.0.1:8000/exercito/paises/" + id,
		method: "GET",
		dataType: "json",
	});
}

function obterMilitares() {
	$.ajax({
		url: "http://127.0.0.1:8000/exercito/militares",
		method: "GET",
		dataType: "json",
		success: function (objetos) {
			adicionarMilitaresAoSelect(objetos, "comandante");
		},
		error: function () {
			alert("Ocorreu um erro ao carregar os militares!");
		},
	});
}

function adicionarMilitaresAoSelect(militares, selectId) {
	militares.forEach((militar) => {
		$.when(obterPessoa(militar.pessoa)).done(function (pessoa) {
			option = `<option value=${militar.id}>${pessoa.nome}</option>`;
			$('#'+selectId).append(option);
		})
	});
}

function obterPessoa(id) {
	return $.ajax({
		url: "http://127.0.0.1:8000/exercito/pessoas/" + id,
		method: "GET",
		dataType: "json",
	});
}

obterExercitos()
obterMilitares()
