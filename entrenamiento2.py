#función para validar ingreso de un número
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Pon solo un lo que se pide.")

#función para validar ingreso de una lista de números
def get_valid_float_list(prompt):
    while True:
        entrada = input(prompt)
        partes = entrada.split(',')
        try:
            return [float(p.strip()) for p in partes]
        except ValueError:
            print("Pon solo separados por comas.")

#determinar estado de aprobación
nota = get_valid_float("Pon una nota entre 0 y 100: ")
if 0 <= nota <= 100:
    if nota >= 60:
        print("Resultado: Aprobado")
    else:
        print("Resultado: Reprobado")
else:
    print("La nota debe estar entre 0 y 100.")

#calcular promedio de notas
notas = get_valid_float_list("Pon una lista de notas separadas por comas: ")
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")

#contar notas mayores a un valor
valor_comparacion = get_valid_float("Pon un valor para comparar las notas: ")

conteo_mayores = 0
i = 0
while i < len(notas):
    if notas[i] > valor_comparacion:
        conteo_mayores += 1
    i += 1

print(f"Número de notas mayores que {valor_comparacion}: {conteo_mayores}")

#verificar y contar calificaciones específicas
objetivo = get_valid_float("Pon una nota específica a buscar en la lista: ")

conteo_objetivo = 0
for nota in notas:
    if nota == objetivo:
        conteo_objetivo += 1
        continue
    else:
        pass  #incluido según se pide usar break o continue

print(f"La nota {objetivo} aparece {conteo_objetivo} veces en la lista.")
