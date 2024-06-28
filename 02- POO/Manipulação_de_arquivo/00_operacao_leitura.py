arquivo = open("E:/Cursos/T.I/Python DIO/02- POO/Manipulação_de_arquivo/lorem.txt", "r")


print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# tip
# while len(linha := arquivo.readline()):
#     print(linha)
arquivo.close()
