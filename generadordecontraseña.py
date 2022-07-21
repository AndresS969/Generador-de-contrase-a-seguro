import string
import random


def seguridad():
    print("generador de contraseñas segura")
    print()
    x = string.ascii_lowercase
    m = string.digits
    y = string.ascii_uppercase
    z = string.punctuation

    combinacion_contraseña = x+m+y+z
    longitud_contraseña = int(input("ingrese la longitud de la contraseña: ")) 

    password = "".join(random.sample(combinacion_contraseña,longitud_contraseña))
    print()
    print("Mi nueva contraseña es: ", password)
    

if __name__=="__main__":
    seguridad()