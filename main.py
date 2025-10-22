#New code

#Defining the functions:

def calcular_imc (peso, altura):
    imc = peso/(altura*altura)
    return imc

def analise_imc (imc):
    if imc<18.5:
        print("Classificação: Abaixo do Peso, procure ajuda médica.")
    elif imc<25 :
        print("Classificação: Peso normal, parabéns!")
    elif imc<30:
        print("Classificação: Acima do peso, atenção para sua saúde.")
    elif imc<35:
        print("Classificação: Obesidade nível um, é recomendado procurar ajuda médica.")
    elif imc<40:
        print("Classificação: Obesidade nível dois, procure um médico.")
    else:
        print("Classificação: Obesidade nível três, procure um médico imediatamente.")

#Making use of said functions

peso = float(input("Informe o seu peso atual:"))
altura = float(input("Agora informe sua altura, em metros:"))

resultado_imc = calcular_imc(peso, altura)

#Results

print("---------------------------------------------------------")
print("O resultado do IMC para estes valores é: ", resultado_imc)
print("---------------------------------------------------------")
analise_imc(resultado_imc)
print("---------------------------------------------------------")
