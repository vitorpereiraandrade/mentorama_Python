setx = set(['apple', 'mango'])
sety = set(['mango', 'orange'])
setz = set(['mango'])

#A)
uniao = setx.union(sety, setz)
print(uniao)

#B)
comum = setx.intersection(sety)
print(comum)

#C)
sub = setx.issubset(sety and setz)
print(sub)


#D)
diferenca = setx.difference(sety)
print(diferenca)

