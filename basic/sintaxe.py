# Esse é um comentário em Python
from click import prompt


print("Hello, World!")

### Números
x = 6
y = 3
print(f"A soma de {x} e {y} é igual a: {x + y}")
print("Somando " + str(x) + " e " + str(y) + " é igual a: " + str(x + y))
print(f"O tipo da variável x é: {type(x)}")
print(type(x))

### Operações matemáticas
a = x + y
b = x - y
c = x * y
d = x / y
e = x % y

### Stings
nome = prompt("Digite seu nome: ").lower()
sobrenome = prompt("Digite seu sobrenome: ").lower()
print(f"Olá, {nome.upper()} {sobrenome.upper()}! Bem vindo!")

### Metodos de string
nome_completo = nome + " " + sobrenome
nome_completo.count("a")
nome_completo.find("a")
nome_completo.replace("a", "o")
nome_completo.encode().decode() # Transforma a string em bytes e depois volta para string, ainda não entendi muito bem a utilidade disso, mas é bom saber que existe

telefone = prompt("Digite seu telefone: ")
telefone = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "") # Pode ser muito utilizada para limpar strings e tratativa de dados
print(f"O seu telefone é: {telefone}")

print("-".join([nome_completo]))
print(nome_completo.split(" ")) # Utilizado para separar uma string em uma lista de strings, utilizando o separador informado como parâmetro
print(nome_completo.strip("x")) # Utilizado para remover caracteres indesejados do início e do fim da string, nesse caso o "x" que não existe na string, então não vai remover nada

print(nome_completo.startswith("Vi")) # Verifica se a string começa com o caractere informado como parâmetro

print("ini" in nome_completo) # Verifica se a string está contida na string principal

print("ini" not in nome_completo) # Verifica se a string não está contida na string principal