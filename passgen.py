import string
import random
#Agrega el tamaño de la contraseña
longitud = int(input("Ingrese el tamaño de la contraseña: "))
#Los caracteres son letras, minis_mayus, digitos y puntos.
caracteres = string.ascii_letters + string.digits +string.punctuation
#En contraseña se guarda cada caracter de manera aleatorio por el rango de longitud.
contrasena = "".join(random.choice(caracteres) for i in range(longitud))
#Imprime la contraseña con la longitud.
print("La contraseña generada es: " + contrasena)

