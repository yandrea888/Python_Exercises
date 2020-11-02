calificaciones = {'Moviles3': 3.5, 'ProgAvan': 4.8, 'NuevTecn': 4 }

#resultado = calificaciones

a=tuple(calificaciones.values())
b=len(a)
suma=0
for val in a:
    suma+=val

maximo = max(calificaciones.keys(), key=lambda k: calificaciones[k])
minimo = min(calificaciones.keys(), key=lambda k: calificaciones[k])

print("El promedio es:",suma/b) 
print("La materia con mejor promedio:", maximo, calificaciones[maximo])
print("La materia con menor promedio:", minimo, calificaciones[minimo])

