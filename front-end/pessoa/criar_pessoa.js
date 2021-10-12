$("#form_pessoa").on("submit", function (event) {
	criarObjeto(
		event,
		"http://127.0.0.1:8000/exercito/pessoas",
		"form_pessoa",
		"Pessoa"
	);
});
