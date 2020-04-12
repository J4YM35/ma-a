import math

a = float(input("Qual o valor de a?: "))
b = float(input("Qual o valor de b?: "))
c = float(input("Qual o valor de c?: "))


delta = b**2 - (4*a*c)

if delta < 0:
    print("Essa equação não possui raizes reais")
else:
    if delta == 0:
        print("Esta função possui apenas uma raiz")
        raiz = (b+ math.sqrt(delta))/a
        print("A raiz dessa equação é", raiz)
    else: 
        print("Esta função possui duas raizes")
        raiz_1 = (-b + math.sqrt(delta)) / 2*a
        raiz_2 = (-b - math.sqrt(delta)) / 2*a
        print("As raizes da equação são: ", raiz_1, "e", raiz_2)