dic = {}

def insere_dic(nome,n1, n2):
    dic[nome] = [n1, n2]

def media(nome):
    n1 = dic[nome][0]
    n2 = dic[nome][1]
    return (n1 + n2) / 2
'''
nome = input('Nome: ')
dic = {}
while nome != '':
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    dic[nome] = [n1, n2]
    nome = input('Nome: ')'''
#print(media('Fernando'))

