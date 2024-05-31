def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 19:
        return "Plano Prata Fibra - 100Mbps"
    elif consumo <= 21:
        return "Plano Premium Fibra - 300Mbps"
    else:
        return "Consumo fora dos limites dos planos disponíveis"

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Insira o consumo médio mensal: "))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
