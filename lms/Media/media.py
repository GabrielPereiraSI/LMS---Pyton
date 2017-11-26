# escreva uma função que recebe uma lista de números
# e retorna a média dos números dessa lista
# [1, 2, 3] => 2
# [5, 5, 4, 4] => 9

# crie um novo módulo para testar a função que 
# calcula a média

def calcula_media(lista):
    soma = sum(lista)    
    t = len(lista)
    return soma / t
