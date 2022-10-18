# Criar um arquivo
arquivo = open('teste.txt', 'a+')

# fecha um arquivo
arquivo.close()

# Abre um arquivo para escrita substituindo um conteúdo do arquivo existente

arquivo = open('teste.txt', 'w+')
arquivo.write('Linha1\n')
arquivo.write('Linha2\n')
arquivo.write('Linha3\n')
arquivo.close()

# Le um arquivo existente

arquivo = open('teste.txt', 'r')
print(arquivo.read())
arquivo.close()

# Outros metodos de leitura

arquivo = open('teste.txt', 'r')
print(arquivo.readline(), end='')
print(arquivo.readline(), end='')
# print(arquivo.readline(), end='')
arquivo.close()

# Outro metodo
arquivo = open('teste.txt', 'r')
print(arquivo.readlines())
arquivo.close()




