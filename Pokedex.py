import sqlite3, os
import pandas as pd

directory = os.path.dirname(__file__) #Obtiene la ruta donde se encuentra el archivo .py y lo guarda como string en directory
os.chdir(directory) #cd hacia el directorio donde está el archivo .py
conexion = sqlite3.connect("pokedex.sqlite")#abrimos conexión con la base de datos (se genera en el mismo directorio donde tenemos nuestro archivo .py)

def crearBase():
    try:
        conexion.execute("""
        
            create table pokemones (

                id integer primary key autoincrement,
                nombre text,
                vida integer,
                crit real
            )
        """)
        print("Se creó la tabla de artículos")

    except sqlite3.OperationalError:
        print ("La tabla ya existe")

def addPokemon(nombre, vida, crit):
    conexion.execute("insert into pokemones (nombre, vida, crit) values (?,?,?)", (nombre, vida, crit))
    conexion.commit()
    os.system("clear")
    print("\n---¡Pokémon registrado exitosamente!---")

def showPokemons():
    cursor = conexion.execute("select id, nombre, vida, crit from pokemones ")
    lista = cursor.fetchall()
    os.system("clear")
    df1 = pd.DataFrame(lista,columns= ['ID', 'NOMBRE', 'VIDA', 'CRIT'])
    print ("///////////////Base de datos Pokémon///////////////\n")
    print(df1.to_string(index=False))
    print ("\n///////////////////////////////////////////////////\n")

def searchById(id):
    cursor = conexion.execute("select id,3 nombre, vida, crit from pokemones where id = ?", (id,))
    lista = cursor.fetchall()
    os.system("clear")
    print ("///////////////Base de datos Pokémon///////////////\n")
    df1 = pd.DataFrame(lista,columns= ['ID', 'NOMBRE', 'VIDA', 'CRIT']) 
    print(df1.to_string(index=False))
    print ("\n///////////////////////////////////////////////////\n")

def deletePokemon(id):
    conexion.execute("delete from pokemones where id = ?",(id,))


while (True):
    opc = int(input("\nSeleccione una opción\n\n1) Registrar un Pokémon\n2) Eliminar un Pokémon\n3) Buscar por ID\n4) Ver la base de datos\n5) Generar base de datos\n6) Salir\n"))

    if opc == 1:
        nombre = input("\nIngresa el nombre del Pokémon: ")
        vida = input("Ingresa la vida del Pokémon: ")
        crit = input("Ingresa el crítico del Pokémon: \n")
        addPokemon(nombre, vida, crit)
    elif opc == 2:
        id = int (input("Introduce el ID: "))
        deletePokemon(id)
    elif opc == 3:
        id = int(input("Introduce el ID: "))
        searchById(id)
    elif opc == 4:
        showPokemons()
    elif opc == 5:
        crearBase()
    elif opc == 6:
        break

conexion.close()