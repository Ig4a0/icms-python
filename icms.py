#Solicitar que o usuário do programa informe sua altura (em metros)
#Solicitar que o usuário do programa informe seu peso (em quilograma)

altura = float(input("Digite sua altura em metros:"))
peso = float(input("Digite seu peso em  quilogramas:"))

#Calculo de IMC

imc = peso/(altura**2)

#Exibição de resultado
print("Seu IMc é de: {:.2f}".format(imc))

#Classificação de IMC

if imc < 18.5:
    print("Você está abaixo do peso normal")
elif 18.5 <= imc < 24.9:
    print("Seu peso está na faixa de peso normal")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso")
else:
    print("Você está com obesidade")
