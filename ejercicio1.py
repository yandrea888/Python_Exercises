calificaciones = {'moviles3': 3, 'progAvan': 4.8, 'nuevTecn': 4.3 }

resultado = calificaciones

a=tuple(calificaciones.values())
b=len(a)
suma=0
for val in a:
    suma+=val
print("promedio",suma/b)