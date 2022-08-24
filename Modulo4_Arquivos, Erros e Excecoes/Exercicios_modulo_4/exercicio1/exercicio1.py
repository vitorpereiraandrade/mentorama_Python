ip_entrada = open('ip_entrada.txt', 'a+')
ip_entrada.close()

ip_entrada = open('ip_entrada.txt', 'w+')
ip_entrada.write('200.135.80.9\n')
ip_entrada.write('192.168.1.1\n')
ip_entrada.write('8.35.67.74\n')
ip_entrada.write('257.32.4.5\n')
ip_entrada.write('85.345.1.2\n')
ip_entrada.write('1.2.3.4\n')
ip_entrada.write('9.8.234.5\n')
ip_entrada.write('192.168.0.256\n')
ip_entrada.close()

# ACHEI ESSA FUNÇÃO NA INTERNET PARA IPS VALIDOS E INVALIDOS
def ip_valido(ip_string):
    partes = ip_string.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        parte_integer = int(parte)
        if parte_integer < 0 or parte_integer > 255:
            return False
    return True

ip_entrada = open('ip_entrada.txt', 'r')
lista_ips = ip_entrada.read().split('\n')

validos = []
invalidos = []

for ip in lista_ips:
    if ip_valido(ip) == True:
        validos.append(ip)
    else:
        invalidos.append(ip)

arquivo_relatorio = open('arquivo_de_saida.txt', 'wt')
arquivo_relatorio.write('[Endereços válidos]\n')

for valido in validos:
    arquivo_relatorio.write(valido+'\n')

arquivo_relatorio.write('\n[Endereços inválidos]\n')
for invalido in invalidos:
    arquivo_relatorio.write(invalido+'\n')

arquivo_relatorio.close()

arquivo_relatorio = open('arquivo_de_saida.txt', 'r')
print(arquivo_relatorio.read())
arquivo_relatorio.close()




