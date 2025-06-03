pi: float = 3.14

def menu():
     print("\n--- Cálculos geométricos ---")
     print("A. Quadrado")
     print("B. Triângulo")
     print("C. Círculo")
     print("D. Rêtangulo")
     print("E. Sair")
     opcao = input("Escolha uma opção: ").upper() 
     return opcao

menu()


def quadrado():
     
     lado1: float = float (input("Insira o valor do lado um: "))
     lado2: float = float (input("Insira o valor do lado dois: "))
     area_quadrado = lado1 * lado2
     print("A área do quadrado é: ", [area_quadrado])

def triangulo():
     
     base: float = float (input("Insira o valor da base : "))
     altura: float = float (input("Insira o valor da altura: "))
     area_triangulo = (base * altura)/2
     print("A área do triângulo é: ", [area_triangulo])

def circulo():
     
     raio: float = float (input("Insira o valor do raio: "))
     area_circulo = raio**2 * pi
     print("A área do circulo é: ", [area_circulo])

def retangulo():
     
    comprimento: float = float(input("Insira o valor do comprimento: "))
    largura: float = float(input("Insira o valor da largura: "))
    area_retangulo = comprimento * largura
    print("A área do retângulo é: ", [area_retangulo])

while True:
    opcao = menu()
    if opcao == 'A':
        quadrado()
    elif opcao == 'B':
        triangulo()
    elif opcao == 'C':
        circulo()
    elif opcao == 'D':
        retangulo()
    elif opcao == 'E':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
     

     
     

     


