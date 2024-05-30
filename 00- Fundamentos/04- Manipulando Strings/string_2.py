nome = "Junior"
idade = "30"
profissão = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Junior", "idade": 30}

print("Nome: %s Idade: %s" % (nome, idade))

print("Nome: {} Idade: {}" .format(nome, idade))

print("Nome: {1} Idade: {0}" .format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(idade, nome))

print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}" .format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade}" .format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo}")
