# Creando la base de datos.

def createDB():
    import sqlite3
    conn = sqlite3.connect("estudiantes.db")
    conn.commit()
    conn.close()


# Creando la tabla para la base de datos.
def create_table():
    conn = sqlite3.connect("estudiantes.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE estudiantes (
            matricula integer,
            nombre text,
            apellido,
            direccion,
            telefono integer
        )"""
    )
    conn.commit()
    conn.close()


# En esta funcion se insertaran los datos de los de las personas para ser registradas en la base de datos.
def insertar_info():
    import sqlite3
    conn = sqlite3.connect("estudiantes.db")
    conn.execute("insert into estudiantes(matricula,nombre, apellido, direccion,telefono) values (?,?,?,?,?)",
                 (20185946, "Juan", "Uceta", "Res.vereda tropical, San Isidro", 8097060915))
    conn.execute("insert into estudiantes(matricula,nombre, apellido, direccion,telefono) values (?,?,?,?,?)",
                 (20195589, "Jorge", "Vasquez", "Arroyo hondo, camino chiquito #50", 8094561212))
    conn.execute("insert into estudiantes(matricula,nombre, apellido, direccion,telefono) values (?,?,?,?,?)",
                 (20205434, "Misael", "Duval", "Res. La moneda, San Isidro", 8095593409))
    conn.execute("insert into estudiantes(matricula,nombre, apellido, direccion,telefono) values (?,?,?,?,?)",
                 (20215434, "Sundel", "Diaz", "Lotes y servicio, sabana perdida", 8099874360))
    conn.execute("insert into estudiantes(matricula,nombre, apellido, direccion,telefono) values (?,?,?,?,?)",
                 (20225434, "Hansel", "Baez", "Lotes y servicios, Sabana perdida", 809873406))
    conn.commit()
    conn.close()


# Este apartado muestra el contenido de la tabla anteriormente creada
import sqlite3

conn = sqlite3.connect("estudiantes.db")
cursor = conn.execute("select matricula, nombre, apellido, direccion, telefono from estudiantes")
for fila in cursor:
    print(fila)
conn.close()


# Estas lineas de codigo son utilizadas para buscar la informacion de de las personas partiendo de la matricula.
import sqlite3

conn = sqlite3.connect("estudiantes.db")
matricula = int(input("Ingrese su matricula:"))
cursor = conn.execute("select Nombre, apellido, direccion, telefono from estudiantes where matricula=?", (matricula,))
fila = cursor.fetchone()
if fila != None:
    print(fila)
else:
    print("No esta registrada esta matricula.")
conn.close()


# Creando otra tabla para las asignaturas cursadas en este periodo.


def create_table_asig():
    import sqlite3
    conn = sqlite3.connect("estudiantes.db")
    try:
        conn.execute("""create table asignaciones (
                                  matricula integer,
                                  nombre text,
                                  materias text
                            )""")
        print("se creo la tabla asignaciones")
    except sqlite3.OperationalError:
        print("La tabla asignaciones ya existe")
    conn.commit()
    conn.close()


# insercion de info en tabla asignaciones
def info_asignaciones():
    import sqlite3
    conn = sqlite3.connect("estudiantes.db")
    conn.execute("INSERT OR IGNORE INTO asignaciones (matricula, nombre, materias) values (?,?,?)",
                 (20185946, "Juan", "Precalculo, Fundamentos de Programacion, Historia"))
    conn.execute("INSERT OR IGNORE INTO asignaciones (matricula, nombre, materias) values (?,?,?)",
                 (20195589, "Jorge", "Fundamentos de programacion, Contabilidad, Sistema Operativo III"))
    conn.execute("INSERT OR IGNORE INTO asignaciones (matricula, nombre, materias) values (?,?,?)",
                 (20205434, "Misael", "Programacion I, Etica II, Probabilidad y estadistica"))
    conn.execute("INSERT OR IGNORE INTO asignaciones (matricula, nombre, materias) values (?,?,?)",
                 (20215434, "Hansel", "programacion II, Precalculo, Etica III, Inteligencia artificial"))
    conn.execute("INSERT OR IGNORE INTO asignaciones (matricula, nombre, materias) Values (?,?,?)",
                 (20225434, "Sundel", "Desarrollo de emprendedores, Desktop Publishing avanzado, Ingles tecnico"))
    conn.commit()
    conn.close()

# Para obtener informacion general de los usuarios registrados en la tabla asignaciones.
import sqlite3
conn = sqlite3.connect("estudiantes.db")
cursor = conn.execute("select matricula, nombre, materias from asignaciones")
for line in cursor:
    print(line)

# Filtra inforamacion de usuarios partiendo de la matricula.
conn = sqlite3.connect("estudiantes.db")
matricula = int(input("Ingrese su matricula:"))
cursor = conn.execute("select nombre, materias from asignaciones where matricula=?", (matricula,))
fila = cursor.fetchone()
if fila != None:
    print(fila)
else:
    print("No esta registrada esta matricula.")
conn.close()


def actualizar_telefono():
    import sqlite3

    conn = sqlite3.connect("estudiantes.db")
    lector = conn.cursor()
    telefono_a_consultar = int(input("Digite la matricula a consultar: "))
    lector.execute("SELECT * FROM estudiantes WHERE matricula = ?", (telefono_a_consultar,))
    print(lector.fetchall())
    a = (input("¿Desea modificar el telefono del usuario?: "))
    if (a == "si"):
        nuevo_telefono = int(input("Dijite el nuevo numero de telefono: "))
        lector.execute("UPDATE estudiantes SET telefono = %s WHERE matricula = %s" %(nuevo_telefono,telefono_a_consultar))
    elif (a == "no"):
        print("No hay registro que guardar")
        conn.commit()
        conn.close()

import sqlite3

conn = sqlite3.connect("estudiantes.db")
lector2 = conn.cursor()
direccion_a_consultar = input("Digite la matricula a consultar: ")
lector2.execute("SELECT * FROM estudiantes WHERE matricula = ?",(direccion_a_consultar,))
print(lector2.fetchall())
#print("direccion")
d = input("Desea modificar direccion del usuario?: ")
if (d == "si"):
    nueva_direccion = input("Digite la nueva direccion: ")
    lector2.execute("UPDATE estudiantes SET direccion = %s WHERE matricula = %s" %(nueva_direccion,direccion_a_consultar))
elif (d == "no"):
    print("No hay registros que guardar")
conn.commit()
conn.close()




# Bloque_principal

# createDB()
# create_table()
# insertar_info()
# create_table_asig()
# info_asignaciones()
# actualizar_telefono()