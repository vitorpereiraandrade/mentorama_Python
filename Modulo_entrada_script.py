# Modulo Entrada

def valida_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v = int(input(mensagem))
            if v >= minimo and v <= maximo:
                return v
            else:
                print(f'Digite um valor entre {minimo} e {maximo}')
        except:
            print('Voce deve digitar um numero inteiro')
