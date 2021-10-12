function obterPessoasNaoMilitares() {
	$.ajax({
		url: "http://127.0.0.1:8000/exercito/pessoas/nao_militares",
		method: "GET",
		dataType: "json",
		success: adicionarPessoasAoSelect,
		error: function () {
			alert("Ocorreu um erro ao carregar as pessoas!");
		},
	});
}

function obterMilitares() {
	$.ajax({
		url: "http://127.0.0.1:8000/exercito/militares",
		method: "GET",
		dataType: "json",
	});
}

function adicionarPessoasAoSelect(pessoas) {
	pessoas.forEach((pessoa) => {
		option = `<option value=${pessoa.id}>${pessoa.nome}</option>`;
		$("#pessoa").append(option);
	});
}

function obterBatalhoes() {
	$.ajax({
		url: "http://127.0.0.1:8000/exercito/batalhoes",
		method: "GET",
		dataType: "json",
		success: adicionarBatalhoesAoSelect,
		error: function () {
			alert("Ocorreu um erro ao carregar os batalhões!");
		},
	});
}

function adicionarBatalhoesAoSelect(batalhoes) {
	batalhoes.forEach((batalhao) => {
		option = `<option value=${batalhao.id}>${batalhao.nome}</option>`;
		$("#batalhao_atual").append(option);
	});
}

function obterPatentes() {
	$.ajax({
		url: "http://127.0.0.1:8000/exercito/militares/patentes",
		method: "GET",
		dataType: "json",
		success: adicionarPatentesAoSelect,
		error: function () {
			alert("Ocorreu um erro ao carregar os patentes!");
		},
	});
}

function adicionarPatentesAoSelect(patentes) {
	patentes.forEach((patente) => {
		option = `<option value=${patente.valor}>${patente.nome}</option>`;
		$("#patente").append(option);
	});
}

obterPessoasNaoMilitares();
obterBatalhoes();
obterPatentes();

$("#form_militar").on("submit", function (event) {
	criarObjeto(
		event,
		"http://127.0.0.1:8000/exercito/militares",
		"form_militar",
		"Militar"
	);
});
