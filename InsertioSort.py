numeros = [5,1,4,2,8]
for i in range((len(numeros)-1)):
  for j in range((len(numeros)-1)-i):
    if numeros[j] > numeros[j+1]:
      aux = numeros[j]
      numeros[j] = numeros[j+1]
      numeros[j+1] = aux
print(numeros)