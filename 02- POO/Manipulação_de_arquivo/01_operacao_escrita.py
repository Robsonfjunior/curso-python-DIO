arquivo = open(
    "E:/Cursos/T.I/Python DIO/02- POO/Manipulação_de_arquivo/teste.txt", "w"
    )
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])

arquivo.close()
