arquivo = open('arquivo_entrada', 'a+')
arquivo.close()

arquivo = open('arquivo_entrada', 'w+')
arquivo.write('200.135.80.9')
arquivo.write('192.168.1.1')
arquivo.write('8.35.67.74')
arquivo.write('257.32.4.5')
arquivo.write('85.345.1.2')
arquivo.write('1.2.3.4')
arquivo.write('9.8.234.5')
arquivo.write('192.168.0.256')
arquivo.close()

arquivo = open('arquivo_entrada', 'r')
print(arquivo.readlines(2))

validos = []
invalidos = []
entrada = open('arquivo_entrada', 'r')
ipsEntrada= entrada.read().split('\n')

for ip in ipsEntrada:

    if(ip in ip_v):
        validos.append(ip)

    else:
        invalidos.append(ip)



entrada.close()

saida = open('saida_ip.txt', 'w+')
saida.write('[Endereços válidos:]\n')
saida.writelines(validos)
saida.write('[Endereços inválidos:]\n')
saida.writelines(invalidos)
saida.close()
ipsEntrada= entrada.read().split('\n')
