# CRIEI O INPUT PRA GERAR O ERRO

try:
    num = int(input('Digite o número 1 para contar até 10: '))
    if num == 1:
        while num < 11:
            print(num)
            num += 1
        for num in range (1,11):
            print(num)
    else:
        print(f"Vc digitou o número {num}, precisar digitar o número '1'")
except:
    print('É pra digitar o número 1')
    print('Tente novamente')
finally:
    print('Valeu !!!')



