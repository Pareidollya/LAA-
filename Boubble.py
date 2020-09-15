vetor = [5,1,4,2,8,3452,76,23,56,657,123,-12345,5,5,66,4,2,23,643,234,3,0]

for j in range(len(vetor)): #primeiro laço (vezes que se repete a operação de compar e trocar (quantas vezes o vetor será vasculhado))
  
  for i in range((len(vetor)-1)-j): #inicia i do 0 pois a comparação é com o valor seguinte (i+1),- j para reduzir o numero de comparações e trocas quando o vetor ja estiver quase todo vasculhado, aumentando desempenho. 

    num = vetor[i] #numero auxiliar da posição atual (i) = 5, guarda o numero da posição para uso futuro - 1 pra nao dar fora de indice no vetor, 

    if vetor[i] > vetor[i+1]: #comparar posição atual com a proxima 
      vetor [i] = vetor[i+1]  #caso a numero da proxima posição seja maior que à atual, ele é colocado no lugar atual
      vetor[i+1] = num  #numero substituido anteriormente "sobe" uma posição utilizando o numero auxiliar guardado anteriormente

print(vetor)

