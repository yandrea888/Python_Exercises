frase=input("Frase:")
caracter=input("Carácter:")
nueva=""
for c in frase:
    if c==caracter:
        nueva=nueva+"*"
    else:
        nueva=nueva+c
print(nueva)