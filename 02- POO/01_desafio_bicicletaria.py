class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("Plim plim")

    def parar(self):
        print("Parando bicicleta....")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrunmmmm...")

    def trocar_marcha(nro_marcha):
        print("Marcha alterada.")

    def __str__(self):
        return f"bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor{self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = bicicleta("verde", "monark", 2000, 189)
bicicleta.buzinar(b2)
print(b2)
