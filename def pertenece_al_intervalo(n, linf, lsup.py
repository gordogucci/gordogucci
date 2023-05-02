def pertenece_al_intervalo(n, linf, lsup):
    return linf <= n <= lsup
N = float(input("Ingrese un número: "))
linf = float(input("Ingrese un límite inferior: "))
lsup = float(input("Ingrese un límite superior: "))
if pertenece_al_intervalo(N, linf, lsup):
    print("El número pertenece al intervalo.")
else:
    print("El número no pertenece al intervalo.")
