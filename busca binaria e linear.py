def bBinaria(dados,valor):
    dados.sort()
    esquerda = 0 #inicio
    direita = len(dados) - 1 #fim
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if dados[meio] == valor:
            return meio  
        elif dados[meio] > valor:
            direita = meio  
        elif dados[meio] < valor:
            esquerda = meio
        else:
            return "None" 


def bSequencial(dados,valor):
    #dados.sort()
    for j in range(len(dados)):
        if valor == dados[j]:
            return j
