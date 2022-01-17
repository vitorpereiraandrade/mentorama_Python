class A:
    a = 1  # atributo publico
    _b = 2  # Atributo privado a class A   - no privado vc coloca _ na frente


class B(A):                       # A classe 'B' herda os parametros da classe 'A'
    _c = 3  # Atributo privado a B

    def __init__(self):
        print(self.a)
        print(self._c)


a = A
print(a.a)  # imprime 1

b = B
print(b._b)  # Era para dar erro mas nao deu **************** ( Erro, pois _b é privado a classe A).
print(b._c)  # Era para dar erro, mas nao deu ***********( Erro, _c é um atributo privado, somente chamado pela classe)


