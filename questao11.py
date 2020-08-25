num1 = int(input("Insira o número inicial do intervalo: "))
num2 = int(input("Insira o número inicial do intervalo: "))
soma = 0
while (num1<num2-1):
    num1 = num1+1
    print(num1)
    soma = num1 + soma
    
print("A soma dos intervalos é: ", soma)    