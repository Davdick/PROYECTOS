from tkinter import *
from tkinter import messagebox
import sqlite3


#-------------------------FUNCIONES-----------------------------------------
    

#---------------------------------------------------------------------------

def conexionBBDD():
    
    miConexion=sqlite3.connect("BDPrototipo")

    miCursor=miConexion.cursor()
    
    try:

        miCursor.execute('''
            CREATE TABLE bdDatos(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            mi1 VARCHAR(50),
            mi2 VARCHAR(50),
            mi3 VARCHAR(50),
            mi4 VARCHAR(50))
            ''')

        messagebox.showinfo("BBDD", "BBDD Creada con exito")
    
    except:

        messagebox.showwarning("ATENCION", "LA BBDD YA EXISTE")
def limpiarCampos():
    miId3.set("")
    mi11.set("")
    mi22.set("")
    mi33.set("")
    mi44.set("")
        

def crear():
    miConexion=sqlite3.connect("BDPrototipo")

    miCursor=miConexion.cursor()

    datos=mi11.get(),mi22.get(),mi33.get(),mi44.get() 
    miCursor.execute("INSERT INTO bdDatos VALUES(NULL,?,?,?,?)", (datos))
    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado con exito")
def leer():

    miConexion=sqlite3.connect("BDPrototipo3")

    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM bdDatos WHERE ID=" + miId3.get())

    elUsuario=miCursor.fetchall()

    for usuario in elUsuario:

        miId3.set(usuario[0])
        mi11.set(usuario[1])
        mi22.set(usuario[2])
        mi33.set(usuario[3])
        mi44.set(usuario[4])
               
    miConexion.commit()
def actualizar():
    miConexion=sqlite3.connect("BDPrototipo")
    
    miCursor=miConexion.cursor()
    datos=mi11.get(),mi22.get(), mi33.get(), mi44.get()
    miCursor.execute("UPDATE bdDatos SET mi11=?, mi22=?,mi33=?,mi44=?" + 
        "WHERE ID=" + miId3.get(), (datos))


    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro Actualizado con exito")
def eliminar():
    
    miConexion=sqlite3.connect("BDPrototipo")

    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM bdDatos WHERE ID=" + miId3.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro borrado con exito")

see=Tk()
see.title("Amigos")
see.config(bg="DarkSeaGreen2")

miId3=StringVar()
mi11=StringVar()
mi22=StringVar()
mi33=StringVar()
mi44=StringVar()
barraMenu=Menu(see)
see.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos", command=limpiarCampos)

crudMenu=Menu (barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

#ayudaMenu=Menu(barraMenu, tearoff=0)
#ayudaMenu.add_command(label="Licencia")
#ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="Crud", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda")
 

#-----------------------------------------------------------------------------
#------------------------------LABEL frame1---------------------------------------------
usuarioLabel=Label(see, text="Añadir Personas de confianza:")
usuarioLabel.grid(row=0, column=2, sticky="e", padx=10, pady=10)

passLabel=Label(see, text="Nombre:")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(see, text="Apellidos:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(see, text="Telefono:")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(see, text="Correo electronico:")
passLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(see, text="ID:")
passLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)


#----------------------------ENTRY Frame1---------------------------------------------

cuadroNombre=Entry(see, textvariable=mi11)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

cuadroPass=Entry(see, textvariable=mi22)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)

cuadro1=Entry(see, textvariable=mi33)
cuadro1.grid(row=3, column=1, padx=10, pady=10)

cuadro2=Entry(see, textvariable=mi44)
cuadro2.grid(row=4, column=1, padx=10, pady=10)


cuadro4=Entry(see, textvariable=miId3)
cuadro4.grid(row=5, column=1, padx=10, pady=10)

#------------------------BOTONES Frame1--------------------------------------------

#botonEntrar=Button(see, text="Entrar", command=crear)
#botonEntrar.grid(row=3, column=1, sticky="e", padx=20, pady=20)


botonCrear=Button(see, text="Agregar", command=crear)
botonCrear.grid(row=7, column=2, sticky="e", padx=10, pady=10)

botonLeer=Button(see, text="Buscar", command=leer)
botonLeer.grid(row=7, column=3, sticky="e", padx=10, pady=10)

botonActualizar=Button(see, text="Actualizar", command=actualizar)
botonActualizar.grid(row=7, column=4, sticky="e", padx=10, pady=10)

botonBorrar=Button(see, text="Borrar", command=eliminar)
botonBorrar.grid(row=7, column=5, sticky="e", padx=10, pady=10)

#------------------------------------LABEL FRAME 2-----------------------------------


#-----------------------------------BOTONES FRAME 2----------------------------------



see.mainloop()
