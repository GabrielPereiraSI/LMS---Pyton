semana = 'segunda','terça','quarta','quinta','sexta'

fds = ('sábado','domingo')

dia1, dia2, dia3, dia4, dia5 = semana

estudar = ('domingo',)
semana = list(semana)
# errada
semana[0] = 'segunda-feira'
#errado
del semana[3]
print(semana[1])
print(fds[0])
print(estudar[0])
lista = [1,2,3]
tupla = tuple(lista)
print(tupla)

tupla = (0, [1,2])
tupla[1][0] = 5
print(tupla)