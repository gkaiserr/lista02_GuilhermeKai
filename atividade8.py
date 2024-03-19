i = int(input("Digite sua idade:"))

if i < 16:
    print("Não eleitor")
elif i >= 16 and i <= 18 or i > 65:
    print("Eleitor facultativo")
else :
    print("Eleitor obrigatório")