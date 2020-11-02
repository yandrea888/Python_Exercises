#definimos una lista vacia
lista=[]
#disponemos un ciclo de 10 vueltas
for x in range(10):
    valor=int(input("Ingrese un valor positivo:"))
    if valor > 0:
        lista.append(valor)
    else:
        print("El valor debe ser positivo")

#imprimimos la lista    
print(lista)

a=list(lista)
b=len(a)
suma=0
for val in a:
    suma+=val

nMax = max(lista)
nMin = min(lista)

print("El valor de la suma es:",suma)
print("El promedio es:",suma/b)
print("El valor máximo ingresado:", nMax)
print("El valor mínimo ingresado:", nMin)

