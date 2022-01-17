def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')

do_twice(print_spam)


def do_twice(f,g):
    f(g)
    f(g)

def print_nome(g):
    print(g)

do_twice(print_nome, 'Meu nome é Vitor')
