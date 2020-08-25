nome = str(input("Informe seu nome: "))
while len(nome)<3:
    nome = str(input("Informe seu nome: "))

idade = int(input("Informe sua idade: "))
while (idade<0)or(idade>150):
    idade = int(input("Informe sua idade: "))

salario = float(input("Informe seu salário: "))
while salario<0:
    salario = float(input("Informe seu salário: "))

sexo = str(input("Informe seu sexo: "))
while (sexo!="F")and(sexo!="f")and(sexo!="M")and(sexo!="m"):
    sexo = str(input("Informe seu sexo: "))

estadocivil = str(input("Informe seu Estado Civíl: "))
while (estadocivil != "S")and(estadocivil != "s")and(estadocivil != "C")and(estadocivil != "c")and(estadocivil != "V")and(estadocivil != "v")and(estadocivil != "D")and(estadocivil != "d"):
    estadocivil = str(input("Informe seu Estado Civíl: "))

print("Dados corretos e salvos")