uni = int(input("Digite 1 caso sua Universidade for a PUCPR, caso for UNICAMP digite 2:"))
if uni > 2 :
    print("ERRO")
    exit()
n1 = float(input("Digite a primeira nota do Bimestre:"))
n2 = float(input("Digite a segunda nota do Bimestre:"))
m = (n1 + n2/2)
if uni == 1:
    if m >= 7:
        print("Situação do Estudante:")
        print("Aprovado")
    elif m >= 4:
        print("Situação do Estudante:")
        print("Em Exame")
    elif m < 4:
        print("Situação do Estudante:")
        print("Reprovado")
elif uni == 2:
    if m >= 5:
        print("Situação do Estudante:")
        print("Aprovado")
    else :
        print("Situação do Estudante:")
        print("Reprovado")