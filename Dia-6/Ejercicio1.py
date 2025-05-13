# ##########################
# #### Clase Día 6 - Diccionarios en Python ####
# ##########################

# Un diccionario es una colección de elementos con claves únicas asociadas a valores.
miPrimerDiccionario = {
    "nombre": "Pedro",
    "apellido": "Gómez",
    "edad": 25
}

print(miPrimerDiccionario)
print(type(miPrimerDiccionario))

# Acceder a un valor por su clave
print(miPrimerDiccionario["nombre"])
print(type(miPrimerDiccionario["nombre"]))

# Modificar un valor
miPrimerDiccionario["nombre"] = "Pedro"
nombre = miPrimerDiccionario["nombre"]
apellido = miPrimerDiccionario["apellido"]
print(nombre + " " + apellido)

# Agregar una nueva clave
miPrimerDiccionario["ciudadNacimiento"] = "Monteria"
print(miPrimerDiccionario)

# Modificar la clave agregada
miPrimerDiccionario["ciudadNacimiento"] = "Bucaramanga"
print(miPrimerDiccionario)

# Lista de personas (lista de diccionarios)
listaPersonas = [miPrimerDiccionario]
listaPersonas.append({
    "nombre": "Corpus",
    "apellido": "Bejarano",
    "edad": 27
})

# Mostrar la lista y elementos
print(listaPersonas)
print(listaPersonas[1])
print(type(listaPersonas[1]))
print(listaPersonas[0]["edad"])

# Recorrer la lista de personas
for i, persona in enumerate(listaPersonas):
    print("#################")
    print(f"#### Persona #{i + 1} ####")
    print("#################")
    print("Nombre:", persona["nombre"])
    print("Apellido:", persona["apellido"])
    print("Edad:", persona["edad"])

# Diccionario con listas (más robusto)
diccionarioRobusto1 = {
    "id": 1,
    "nombre": "Pedro",
    "apellido": "Gómez",
    "edad": 25,
    "telefonos": [
        {"codigo": 57, "numero": 3023019865, "tipo": "trabajo"},
        {"codigo": 1, "numero": 3983054625, "tipo": "personal"}
    ]
}

diccionarioRobusto2 = {
    "id": 2,
    "nombre": "Corpus",
    "apellido": "Bejarano",
    "edad": 27,
    "telefonos": [
        {"codigo": 58, "numero": 2323057565, "tipo": "trabajo"},
        {"codigo": 22, "numero": 6857493658, "tipo": "personal"}
    ]
}

listaRobusta = [diccionarioRobusto1, diccionarioRobusto2]

# Mostrar número de trabajo del primer contacto
for telefono in listaRobusta[0]["telefonos"]:
    if telefono['tipo'] == "trabajo":
        print(telefono['numero'])

# Mostrar otro número específico
numeroPrimeraPersona = listaRobusta[0]["telefonos"][1]['numero']
tipoNumeroPP = listaRobusta[0]["telefonos"][1]['tipo']
print(str(numeroPrimeraPersona) + " " + tipoNumeroPP)

# Menú CRUD
booleanito = True
while booleanito:
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")

    opcionUsuario = input("Ingrese una opción (número): ")
    print("")

    if(opcionUsuario==1):
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        nuevaPersona = {}
        nuevaPersona["id"] = int(input("Ingrese ID: "))
        nuevaPersona["nombre"] = input("Ingrese nombre: ")
        nuevaPersona["apellido"] = input("Ingrese apellido: ")
        nuevaPersona["edad"] = int(input("Ingrese edad: "))
        nuevaPersona["telefonos"] = []

        cantidadTelefonos = int(input("¿Cuántos teléfonos quiere agregar?: "))
        for i in range(cantidadTelefonos):
            telefono = {}
            print("Teléfono #", i+1)
            telefono["codigo"] = int(input("Código de país: "))
            telefono["numero"] = int(input("Número: "))
            telefono["tipo"] = input("Tipo (personal o trabajo): ")
            nuevaPersona["telefonos"].append(telefono)

        listaRobusta.append(nuevaPersona)
        print("Persona agregada exitosamente.")

    elif (opcionUsuario==2):
        for i, persona in enumerate(listaRobusta):
            print("#################")
            print(f"#### Persona #{i + 1} ####")
            print("#################")
            print("ID:", persona["id"])
            print("Nombre:", persona["nombre"])
            print("Apellido:", persona["apellido"])
            print("Edad:", persona["edad"])

            for j, telefono in enumerate(persona["telefonos"]):
                print("---------------------------")
                print(f"Teléfono #{j + 1}:")
                print("#### - Código:", telefono["codigo"])
                print("#### - Número:", telefono["numero"])
                tipo_desc = "Personal" if telefono["tipo"] == "personal" else "Trabajo"
                print(f"#### - Tipo: Es su número de {tipo_desc}")
                print("---------------------------")
                
    elif(opcionUsuario==3):
        print("#################")
        print("#### Buscar Persona ####")
        print("#################")
        buscarID = int(input("Ingrese el ID de la persona: "))
        encontrado = False
        for i in range(len(listaRobusta)):
            if(listaRobusta[i]["id"] == buscarID):
                print("ID:", listaRobusta[i]["id"])
                print("Nombre:", listaRobusta[i]["nombre"])
                print("Apellido:", listaRobusta[i]["apellido"])
                print("Edad:", listaRobusta[i]["edad"])
                for j in range(len(listaRobusta[i]["telefonos"])):
                    print("Teléfono #", j+1)
                    print("Código:", listaRobusta[i]["telefonos"][j]["codigo"])
                    print("Número:", listaRobusta[i]["telefonos"][j]["numero"])
                    print("Tipo:", listaRobusta[i]["telefonos"][j]["tipo"])
                encontrado = True
        if(encontrado == False):
            print("No se encontró una persona con ese ID.")


    elif(opcionUsuario==4):
        print("#################")
        print("#### Actualizar Persona ####")
        print("#################")
        idActualizar = int(input("Ingrese el ID de la persona a actualizar: "))
        for i in range(len(listaRobusta)):
            if(listaRobusta[i]["id"] == idActualizar):
                nuevoNombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
                nuevoApellido = input("Nuevo apellido (dejar vacío para no cambiar): ")
                nuevaEdad = input("Nueva edad (dejar vacío para no cambiar): ")

                if(nuevoNombre != ""):
                    listaRobusta[i]["nombre"] = nuevoNombre
                if(nuevoApellido != ""):
                    listaRobusta[i]["apellido"] = nuevoApellido
                if(nuevaEdad != ""):
                    listaRobusta[i]["edad"] = int(nuevaEdad)

                print("Persona actualizada.")
                break
        else:
            print("No se encontró una persona con ese ID.")

    elif(opcionUsuario==5):
        print("#################")
        print("#### Eliminar Persona ####")
        print("#################")
        idEliminar = int(input("Ingrese el ID de la persona a eliminar: "))
        for i in range(len(listaRobusta)):
            if(listaRobusta[i]["id"] == idEliminar):
                del listaRobusta[i]
                print("Persona eliminada.")
                break

    elif (opcionUsuario==6):
        print("Chaousssss")
        booleanito = False

    else:
        print("No es una opción válida.")
