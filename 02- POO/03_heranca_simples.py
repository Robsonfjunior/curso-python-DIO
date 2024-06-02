class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa  
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self): 
        return self.cor


class motocicleta(veiculo):
    pass


class carro(veiculo):
    pass


class caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def estado_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = motocicleta("preta", "ABC-1234", 2)
carro = carro("branco", "ABC-1234", 4)
caminhao = caminhao("roxo","GFD-8712", 8, True)

print(moto)
print(carro)
print(caminhao)
