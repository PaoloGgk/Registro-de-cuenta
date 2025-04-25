# Creemos la cuenta, pidamos datos del usuario
print("Bienvenido a la creación de cuentas")
print("Por favor, completa los siguientes datos para crear tu cuenta")
print("Recuerda que debes tener al menos 12 años para crear una cuenta")
print("El nombre solo puede contener letras y no puede estar vacío")
print("El usuario debe tener entre 4 y 12 caracteres, comenzar con una letra y no contener espacios")
print("La contraseña debe tener al menos 8 caracteres y contener al menos una letra y un número")
print("Si no cumples con alguno de estos requisitos, no podrás crear la cuenta")

#Datos del usuario                                

Nombre = input("¿Cuál es tu nombre? ")
Edad = int(input("¿Cuál es tu edad? "))
Usuario = input("¿Cuál será tu usuario? ")
Contraseña = input("¿Cuál será tu contraseña? ")

#Requisitos para crear la cuenta

#Nombre

if len(Nombre) == 0 or not Nombre.isalpha():
    print("El nombre solo puede contener letras y no puede estar vacio")

#Edad
    
if (Edad) < 12:
    print("Debes tener al menos 12 años para crear una cuenta")
    
#Usuario
    
if len(Usuario) < 4 or len(Usuario) > 12:
    print("El usuario debe tener entre 4 y 12 caracteres")

elif not Usuario[0].isalpha():
    print("El usuario debe comenzar con una letra")
    
elif " " in Usuario:
    print("El usuario no puede contener espacios")
    
#Contraseña
    
if len(Contraseña) < 8:
    print("La contraseña debe tener al menos 8 caracteres")
    
elif not any(char.isdigit() for char in Contraseña):
    print("La contraseña debe contener al menos un número")
    
#Cuenta creada
  
else :
    print("¡Felicidades! Tu cuenta ha sido creada exitosamente")
    print("Nombre:", Nombre)
    print("Edad:", Edad)
    print("Usuario:", Usuario)
    print("Contraseña:", Contraseña)
    
