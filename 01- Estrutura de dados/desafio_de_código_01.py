def lista():
    equipamentos = []

    for i in range(3):
        equipamento = input(f"Qual o equipamento {i+1}: ")
        equipamentos.append(equipamento)

    return equipamentos


equipamentos = lista()

print("Lista de Equipamentos:")
for equipamento in equipamentos:
    print(f"- {equipamento}")