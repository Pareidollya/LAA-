vetor = [5,1,4,2,8,3452,76,23,56,657,123,-12345,5,5,66,4,2,23,643,234,3,0]

for j in range(len(vetor)): 
  
  for i in range((len(vetor)-1)-j):  todo vasculhado, aumentando desempenho. 

    num = vetor[i] 

    if vetor[i] > vetor[i+1]:
      vetor [i] = vetor[i+1] 
      vetor[i+1] = num 

print(vetor)

