"""Considerações iniciais:
1. as aspas triplas (\""") são usadas pra documentar o código, neste caso to usando pra descrevê-lo;
2. as cerquilas (#) são usadas pra comentar o código, neste caso também usei pra descrever o código"""

"""1 Importar o módulo math pra poder calcular raiz"""
import math

"""2 Usar os inputs pra obter os coeficientes da função"""
a = input("Insira o valor de a:")
b = input("Insira o valor de b:")
c = input("Insira o valor de c:")

""""3 Como os imput retornam strings, devemos converter para int ou float pra poder fazer as comparações e cálculos. Neste caso vou usar float para permitir que o ususário coloque números quebrados. Ex: 1.5"""
a = float(a)
b = float(b)
c = float(c)

"""4 calculamos o delta da fórmula de Báskara"""
delta = b ** 2 - (4 * a * c)

if delta < 0:  # Se delta é menor que 0 ele entra aqui
    """4a Esta função não possui raizer reais"""
    print("Esta função não possui raizer reais")

else:  # Se delta não é menor que zero ele entra aqui

    if delta == 0:
        """4b Esta função possui apenas uma raiz"""
        print('Esta função possui apenas uma raiz')
        """Calcula a raiz"""
        raiz = (b + math.sqrt(delta)) / a

        print('A raiz da função é:', raiz)  # Imprime a raiz

    if delta > 0:
        """esta função possui 2 raizes"""
        print('esta função possui 2 raizes')

        """Calcula as raizes"""
        raiz_1 = (b + math.sqrt(delta)) / a
        raiz_2 = (b - math.sqrt(delta)) / a

        """Curiosidade: usei o barra n aqui pra quebrar a linha no print"""
        print('As raizes são:\nraiz 1:', raiz_1, '\nraiz 2:', raiz_2)
