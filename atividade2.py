a = int(input("Digite um número diferente de 0, para a:"))

if a == 0 :
    print("ERRO")

b = int(input("Digite um número para b:"))
c = int(input("Digite um número para c:"))



bas = b**2 - 4 * a * c

if bas > 0 :
    print("existem duas raízes reais distintas")
elif bas == 0 :
    print("existem duas raízes reais iguais")
elif bas < 0 :
    print("existem duas raízes imaginárias conjugadas")