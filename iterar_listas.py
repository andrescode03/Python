animales = ["gato","perro","camello"]
numeros = [10,20,30]

for animal in animales:
    print(f'ahora la variable es igual a: {animal}')
    
    #se ejecuta cada uno, primero uno y luego el otro... 

#recorriendo una lista de numeros y multiplicando cada uno por 10 
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
    
# forma correcta de recorrer ecorrer una lista ENUMERATE
for num in enumerate(numeros):
    print(num)
    
#USANDO FOR / ELSE
for numero in numeros: 
    print(f"ejecutando el ultimo bucle: {numero}")
else:
    print("el bucle termino")
    
