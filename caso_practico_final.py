'''Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione
una lista de tareas pendientes.'''

class Tarea: # clase principal
    
    #atributos de la clase (con valores por defecto)
    lista_tareas = [] #crear lista una vacía
    num_tareas = 0
    nombre = ""
    estado = "Pendiente"
    
    # constructor
    def __init__(self, nombre ="", estado = "Pendiente"):
        self.nombre = nombre
        self.estado = estado

    #decorador con las instrucciones cómo mostrar la lista de tareas    
    @classmethod
    def listar_todas_tareas(cls):
        if not cls.lista_tareas: # si no hay tareas guerdadas
            return "No hay tareas.\n"
        resultado = ""
        for i, tarea in enumerate(cls.lista_tareas, 1): # para enumerar las tareas dentro de la lista
            resultado += f"{i}. Tarea: {tarea.nombre} | Estado: {tarea.estado}\n" #el formato en qué se mostrará la lista
        return resultado

# opción del menú por defecto    
opcion = 0
#bucle while para crear un menú para la aplicación. se va a mostrar después de ejecutar cada opción, hasta que el usuario pulse 5 para salir
while (opcion!=5):
    opcion=input("Elige una opción:\n1. Añadir tarea.\n2. Mostrar las tareas.\n3. Marcar la tarea como completada.\n"
                 + "4. Eliminar tarea.\n5. Salir.\n")
    
    # añadir tareas
    if opcion == "1":
        # bucle while para poder añadir varias tareas a la vez. no hay límite en el número de tareas
        while True:
            nombre=input("Escribe una tarea. Si quieres volver al menú principal, escribe 'stop'.\n")
            if nombre.lower() == "stop": #convertir la palabra en minúsculas por si los usuarios la escriben con mayúscula(s)
                print("Volvemos al menú principal.\n")
                break
            else:
                #al crear una tarea, se marca como pendiente
                tarea = Tarea(nombre)
                Tarea.lista_tareas.append(tarea) #para añadir tarea en la lista
                Tarea.num_tareas += 1 #se incrementa el número de tareas
                print("Tarea guardada.\n")
   
    #mostrar la lista con todas las tareas
    elif opcion == "2":
        print("-----Mis tareas:-----\n" + Tarea.listar_todas_tareas()) #se llama el decorador

    #marcar la tarea como completada
    elif opcion == "3":   
        print("-----Mis tareas:-----\n" + Tarea.listar_todas_tareas()) #mostrar las tareas, llamando al decorador
        
        # para elegir la tarea
        while True:
            texto=input("\n¿Has completado alguna? Escribe 'sí' o 'no'\n")
                        
            if texto.lower() == "sí" or texto.lower() == "si": #por si los usuarios escriben sin tildes
                while True:    
                    num_tarea=input("Escribe el número de la tarea que quieres marcar como completada.\n")
                    try: #comprobar si el número de la tarea está dentro de la lista
                        #se utiliza -1 para llegar al número de la tarea en la lista, ya que en el programa el índice empieza por 0, 
                        #pero los usuarios van a poner los números empezando por 1
                        num_tarea = int(num_tarea) - 1
                        #si el número introducido es mayor que 0, pero menor que el tamaño de la lista
                        if (0 <= num_tarea < len(Tarea.lista_tareas)): 
                            Tarea.lista_tareas[num_tarea].estado = "Completada" #cambiar el estado a la tarea seleccionada
                            print("Tarea " + Tarea.lista_tareas[num_tarea].nombre + " está completada") #confirmación
                            break
                        else:
                            print("Introduce un número de tarea que existe.")
                    except ValueError:
                        print("Introduce la opción válida.")    
                break #salir del bucle while interno
                    
            #si el usuario pulsa "no"
            elif texto.lower() == "no":
                print("Volvemos al menú principal.\n")
                break
            else: # el usuario puede volver a introducir el número, sin tener que volver al menú
                print("Introduce la opción válida.")

    # eliminar la(s) tarea(s)       
    elif opcion == "4":
        #si la lista está vacía
        if not Tarea.lista_tareas:
            print("No hay tareas. Volvemos al menú principal.\n")
            continue
        # bucle para poder borrar las tareas sin volver al menú después de cada eliminación
        while True:
            print("¿Qué número de tarea quieres eliminar? Si NO QUIERES BORRAR NADA y deseas volver al menú, pulsa '0'\n")
            print("-----Mis tareas:-----\n" + Tarea.listar_todas_tareas()) #mostrar la lista para ver las tareas con los números
            
            # para introducir el número de tarea
            num_tarea=input("Escribe el número aqui:  ")

            # si pulsar 0, el usuario va a salir al menú principal
            if num_tarea == '0':
                print("Volvemos al menú principal.\n")
                break

            try: #comprobar si el número de la tarea está dentro de la lista (como en la opcion 3)    
                num_tarea = int(num_tarea)-1
                
                #se pide otro número si el número introducido no corresponde con los números de la lista
                if not (0 <= num_tarea < len(Tarea.lista_tareas)):
                    print("Introduce un número de tarea que existe.")
                    continue # para quedar dentro del bucle
                
                #si la tarea está completada, se eliminará sin pasos adicionales
                if (0 <= num_tarea < len(Tarea.lista_tareas)) and (Tarea.lista_tareas[num_tarea].estado == "Completada"):
                        #confirmación
                        print ("La tarea " + Tarea.lista_tareas[num_tarea].nombre + " ha sido eliminada.\n")
                        Tarea.lista_tareas.pop(num_tarea) # eliminar el número correspondiente
                        Tarea.num_tareas -= 1 #disminuir el número de tareas en la lista
                        continue

                #pasos adicionales si la tarea está pendiente   
                if (0 <= num_tarea < len(Tarea.lista_tareas)) and (Tarea.lista_tareas[num_tarea].estado == "Pendiente"):
                        texto=input("La tarea " + Tarea.lista_tareas[num_tarea].nombre + " no está completada."
                                    + "¿Quieres eliminarla de todos modos? (Escribe 'sí' o 'no')   ")
                        
                        #hay que confirmar su borrado
                        if texto.lower() in ["sí", "si"]:
                            print ("La tarea " + Tarea.lista_tareas[num_tarea].nombre + " ha sido eliminada.\n")
                            Tarea.lista_tareas.pop(num_tarea)
                            Tarea.num_tareas -= 1
                            continue
                        elif texto.lower()=="no":
                            print("Puedes elegir otra tarea para eliminar.\n")
                            continue #para no salir del bucle
                        else: 
                            print("Opción no válida. Introduce otro número.\n")
                            continue #para no salir del bucle
            
            # excepción en le caso de introducir palabras o números que no corresponden    
            except ValueError:
                print("Introduce un número de tarea que existe o vuelve al menú principal para ver la lista.")
                continue
    
    #salir del programa 
    elif opcion == "5":
        print("Salimos del programa.\n")
        break

    # en el caso si la opción introducida no está en el menú    
    else:
        print("Introduce una opción válida.\n")