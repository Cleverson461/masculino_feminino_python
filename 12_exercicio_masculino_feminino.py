#Receba F para feminino e M para masculino e exiba o sexo da pessoa.

sexo = input("Digite o sexo da pessoa: ")
#sexo = sexo.upper()

if sexo == "F" or sexo == "Feminino" or sexo == "feminino" or sexo == "FEMININO" or sexo == "f":
    print("Sexo Feminino")
elif sexo == "M" or sexo == "Masculino" or sexo == "masculino" or sexo == "MASCULINO" or sexo == "m":
    print("Sexo Masculino")
else:
    print('Valor inválido.')