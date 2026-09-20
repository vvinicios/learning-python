from prompt_toolkit import prompt

### Condicionais
nome = prompt("Digite seu nome: ").lower()

if nome == "joão":
    print("Verdadeiro")
else:
    print("Falso")

