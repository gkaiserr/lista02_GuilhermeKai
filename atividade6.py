P = []
I = []


def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        P.append(numero)
    else:
        I.append(numero)


numero = int(input("Digite um número (digite 0 para encerrar): "))


while numero != 0:
    verificar_par_ou_impar(numero)
    numero = int(input("Digite um número (digite 0 para encerrar): "))


print("Valores pares (P):", P)
print("Valores ímpares (I):", I)