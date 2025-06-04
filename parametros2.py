#Função com parametros
def euro(valor: float):
    conversao_euro: float = valor/6.42
    print(f"O valor em Euro é: {conversao_euro}")
    
def dolar(valor: float):
    conversao_dolar: float = valor/5.64
    print(f"valor em Dólar é: {conversao_dolar}")

#Função sem parametros
def libra():
    valor: float = float(input("Insira um valor: "))
    conversao_libra: float = valor/7.63
    print(f"O valor em Libra é: {conversao_libra}")

valor: float = float(input("Informe um valor: R$ "))
euro(valor)
dolar(valor)

