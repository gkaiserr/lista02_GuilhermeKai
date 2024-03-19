def calcular_peso_ideal(altura, sexo):
    if sexo.lower() == 'masculino':
        peso_ideal = round((72.7 * altura) - 58, 2)
    elif sexo.lower() == 'feminino':
        peso_ideal = round((62.1 * altura) - 44.7, 2)
    else:
        print("Sexo inválido. Por favor, insira 'masculino' ou 'feminino'.")
        return None
    return peso_ideal

altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (masculino/feminino): ")

peso_ideal = calcular_peso_ideal(altura, sexo)

if peso_ideal is not None:
    print("O peso ideal é:", peso_ideal)