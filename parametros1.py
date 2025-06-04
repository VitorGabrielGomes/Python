def salario(horas: float):
    valor: float = 45.90
    valor_hora: float = valor * horas
    print(f"O valor por hora do funcionário é: {valor_hora} ")
    
horas: float = float(input("Insira as horas trabalhadas: "))

salario(horas)