# crenado una funcion simple
#  def saludar():
#      print("hola andres, cómo estas?")

# ejecutando la funcion simple
# saludar()

# creando una funcion que tenga parametros

def saludar(nombre, sexo):
    sexo = sexo.lower()     
    if sexo == "mujer":
        adjetivo = "hermosa"
    elif sexo == "hombre":
        adjetivo = "crack"
    else:
        adjetivo = "amigo/a"

    print(f"Hola {nombre}, {adjetivo}, ¿cómo estás?")

saludar("Andres", "hombre")

#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
    
#desempaquetando la funciòn
password,primer_numero = crear_contraseña_random(981)
#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El nùmero utilizado para crearla fue: {primer_numero}")







 


