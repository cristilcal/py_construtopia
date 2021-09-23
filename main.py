# 2 - class - classes

    # 3 - definitions - definições = métodos e funções

    # Cada "def" é um metódo
def print_hi(name):
    print(f'Oi!, {name}')

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        print(f'o segundo numero não pode ser zero!')

if __name__ == '__main__':
    print_hi('Cristian')

    resultado = somar(1,2)
    print(F'O resultado da soma: {resultado}')

    resultado = subtrair(5, 2)
    print(F'O resultado da subtração: {resultado}')

    resultado = multiplicar(10, 2)
    print(F'O resultado da multiplicação: {resultado}')

    resultado = dividir(10, 5)
    print(F'O resultado da divisão: {resultado}')

     # testes unitários / Testes de UNidades

    # testes da função somar
def test_somar():
    # 1 - Configura / Prepara
    num1 = 8  # input / entrada
    num2 = 5  # input / entrada
    resultado_esperado = 13  # output / saida

    # 2 - Executa
    resultado_atual = somar(num1, num2)

        # 3 - Check / Valida
    assert resultado_atual == resultado_esperado


    # o mesmo teste só que resumido
def test_somar_compacto():
    assert somar(8, 5) == 13


