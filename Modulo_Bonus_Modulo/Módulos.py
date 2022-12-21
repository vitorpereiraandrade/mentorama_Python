import funcoes_clientes as fc

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
cpf = int(input("Digite seu cpf: "))

cli1 = fc.cadastra_cliente(nome, email, cpf)
fc.verifica_cadastro_ja_existente(cpf)
fc.verifica_email_valido(email)
