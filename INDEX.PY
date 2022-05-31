def separar(lista): 
   for i in lista:
     if i%2==0:
       pares.append(i)
     else:         
       impares.append(i)
lista = [6,5,2,1,7] 
lista.sort()
pares = []
impares = []
separar(lista)
print(pares)
print(impares)