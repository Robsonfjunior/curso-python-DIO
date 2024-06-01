class cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = cachorro("Zeus", "Banco e preto", False)
    print(c.nome)


#c = cachorro("cappie", "amarelo")
#c.falar()

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

criar_cachorro()
