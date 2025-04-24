// login.html - Verificação de login
if (document.getElementById("formLogin")) {
    document.getElementById("formLogin").onsubmit = function (event) {
      event.preventDefault();
      const usuario = document.getElementById("usuario").value;
      const senha = document.getElementById("senha").value;
      if (usuario === "admin" && senha === "1234") {
        window.location.href = "cadastro.html";
      } else {
        alert("Usuário ou senha incorretos.");
      }
    };
  }
  
  // cadastro.html - Salvamento e listagem de alunos
  if (document.getElementById("formAluno")) {
    document.getElementById("formAluno").onsubmit = function (event) {
      event.preventDefault();
      const aluno = {
        nome: document.getElementById("nome").value,
        nascimento: document.getElementById("nascimento").value,
        serie: document.getElementById("serie").value,
        notas: [
          parseFloat(document.getElementById("nota1").value),
          parseFloat(document.getElementById("nota2").value),
          parseFloat(document.getElementById("nota3").value),
          parseFloat(document.getElementById("nota4").value)
        ]
      };
      const lista = JSON.parse(localStorage.getItem("alunos") || "[]");
      lista.push(aluno);
      localStorage.setItem("alunos", JSON.stringify(lista));
      alert("Aluno cadastrado com sucesso!");
      document.getElementById("formAluno").reset();
    };
  }
  
  function mostrarAlunos() {
    const lista = JSON.parse(localStorage.getItem("alunos") || "[]");
    const div = document.getElementById("lista");
    div.innerHTML = "";
    lista.forEach(aluno => {
      div.innerHTML += `
        <p>
          <strong>Nome:</strong> ${aluno.nome}<br>
          <strong>Nascimento:</strong> ${aluno.nascimento}<br>
          <strong>Série:</strong> ${aluno.serie}<br>
          <strong>Notas:</strong> ${aluno.notas.join(", ")}<br>
          <hr>
        </p>`;
    });
  }
  
