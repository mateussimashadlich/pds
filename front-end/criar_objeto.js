function criarObjeto(event, url, formId, nomeModelo) {
	event.preventDefault();
	$.ajax({
		url: url,
		method: "POST",
		data: $("#" + formId).serialize(),
		dataType: "json",
		success: function () {
			document.getElementById(formId).reset();
			alert(`${nomeModelo} cadastrado com sucesso!`);
		},
		error: function () {
			alert("Ocorreu um erro ao enviar o formulário!");
		},
	});
}