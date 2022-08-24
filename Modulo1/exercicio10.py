valor_divida = float(input('Qual o valor da divida: '))
juros_mensal = float(input('Qual a porcentagem do juros mensal: '))
quantidade_parcela = float(input('Qual a quantidade de parcelas financiamento: '))

juros_total = quantidade_parcela * juros_mensal
print(f'O juros total é {juros_total:.2f}%')

contador1 = juros_total / 100

juros_divida = valor_divida * contador1

valor_total_divida = juros_divida + valor_divida
print(f'O valor total da divida é de R${valor_total_divida:.2f}')

parcela = valor_total_divida / quantidade_parcela
print(f'O valor da parcela mensal com juros é de R$ {parcela:.2f}')
