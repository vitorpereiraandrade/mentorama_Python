num1 = float(input('Digite primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
operacao = float(input('Digite a operacao desejada 1(adiacao), 2(subtracao), 3(divisao), 4(multiplicacao): '))
if operacao == 1:
    print(num1 + num2)
elif operacao == 2:
    print(num1 - num2)
elif operacao == 3:
    print(num1 / num2)
elif operacao == 4:
    print(num1 * num2)
else:
    print('Digitar o numero de 1 a 4')
