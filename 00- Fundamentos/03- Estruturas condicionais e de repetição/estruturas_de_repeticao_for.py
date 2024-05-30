# texto = input('Informe um texto: ')
texto = ""
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha
    print('Executa no final do laço')

# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")

