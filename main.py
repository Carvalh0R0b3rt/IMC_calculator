#New code

peso = float(input("Informe o seu peso atual:"))
altura = float(input("Agora informe sua altura, em metros:"))

def calcular_imc (peso, altura):
    imc = peso/(altura*altura)
    return imc

resultado_imc = calcular_imc(peso, altura)
print("O resultado do IMC para estes valores é: ", resultado_imc)