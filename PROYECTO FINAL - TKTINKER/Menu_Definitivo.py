from tkinter import *
import os
import COMPLEJIDAD_2
import COMPLEJIDAD_3
import TERMINALES

#Cosas menu
def ventana_inicio():
    global ventana_principal
    botones_color = "DarkGrey"
    ventana_principal = Tk()
    ventana_principal.geometry("300x320")
    ventana_principal.resizable(0,0)
    ventana_principal.title("ITESO AERONAUTICS")
    Label(text="Charles de Gaulle Simulacion de Ruta", bg="royalblue3", width="300", height="2",
          font=("Calibri", 13), fg="white").pack()
    miFrame= Frame()
    miFrame.place(x=60, y=60)
    miFrame.config(width="175", height="120")
    miFrame.config(bg="white")
    miFrame.config(relief="ridge")
    miFrame.config(bd=5)
    miImage= PhotoImage(file="Logo_Aeropuerto.png")
    Label(miFrame, image=miImage).place(x=0,y=0)
    Label(text="").pack()
    Button(text="Acceder", height="2", width="25", bg=botones_color, command=login).place(x=55, y=195)
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="25", bg=botones_color, command=registro).place(x=55, y=245)
    Label(text="").pack()
    ventana_principal.mainloop()
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar()
    clave = StringVar()
    Label(ventana_registro, text="Introduzca datos").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario)
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*')
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1,
           command=registro_usuario).pack()
def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("ITESO AERONAUTICS")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
    global verifica_usuario
    global verifica_clave
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
    global entrada_login_usuario
    global entrada_login_clave
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show='*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command=verifica_login).pack()
def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END)
    entrada_login_clave.delete(0, END)
    lista_archivos = os.listdir()
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r")
        verifica = archivo1.read().splitlines()
        if clave1 in verifica:
            seleccionar_dificultad()
        else:
            no_clave()
    else:
        no_usuario()
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack()
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack()
def borrar_no_clave():
    ventana_no_clave.destroy()
def borrar_no_usuario():
    ventana_no_usuario.destroy()
def registro_usuario():
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
    file = open(usuario_info, "w")
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
#Cosas seleccion dificultad
def seleccionar_dificultad():
    global ventana_seleccionar_dificultad
    ventana_seleccionar_dificultad = Toplevel(ventana_login)
    ventana_seleccionar_dificultad.title("ITESO AERONAUTICS")
    ventana_seleccionar_dificultad.geometry("300x320")
    Label(ventana_seleccionar_dificultad, text="Selecciona una dificultad",  bg="royalblue3", width="300", height="2",
          font=("Calibri", 13), fg="white").pack()
    complejidad1 = Button(ventana_seleccionar_dificultad, text= "Complejidad 1", height= 2, width= 25, bg= "darkgrey", command=complejidad1_ventana)
    complejidad1.place(x=57,y=100)
    complejidad2 = Button(ventana_seleccionar_dificultad, text= "Complejidad 2", height= 2, width= 25, bg= "darkgrey", command= complejidad2_ventana)
    complejidad2.place(x=57,y=160)
    complejidad3 = Button(ventana_seleccionar_dificultad, text= "Complejidad 3", height= 2, width= 25, bg= "darkgrey", command=complejidad3_ventana)
    complejidad3.place(x=57,y=220)
#Complejidad1
def complejidad1_ventana():
    global ventana_complejidad1
    ventana_complejidad1 = Toplevel(ventana_seleccionar_dificultad)
    ventana_complejidad1.title("ITESO AERONAUTICS")
    ventana_complejidad1.geometry("300x340")
    Label(ventana_complejidad1, text= "De donde vienes?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_complejidad1, text="JFK - New York", height= 1,width= 20, bg= "darkgrey",command=tipovuelo_newyork).pack(())
    Button(ventana_complejidad1, text="LYC - Londres", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_londres).pack(())
    Button(ventana_complejidad1, text="BCN - Barcelona", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_barcelona).pack(())
    Button(ventana_complejidad1, text="FCO - Roma", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_roma).pack(())
    Button(ventana_complejidad1, text="YUL - Montreal", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_montreal).pack(())
    Button(ventana_complejidad1, text="AMS - Ámsterdam", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_amsterdam).pack(())
    Button(ventana_complejidad1, text="DXB - Dubái", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_dubai).pack(())
    Button(ventana_complejidad1, text="FRA - Fránkfurt", height= 1,width= 20, bg= "darkgrey", command=tipovuelo_frankfurt).pack(())
    Button(ventana_complejidad1, text="SVO - Moscú", height= 1,width= 20, bg= "darkgrey", command=tipovuelo_moscu).pack(())
    Button(ventana_complejidad1, text="IST - Estambul", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_estambul).pack(())
def tipovuelo_newyork():
    global ventana_tipovuelo_newyork
    ventana_tipovuelo_newyork = Toplevel(ventana_complejidad1)
    ventana_tipovuelo_newyork.title("ITESO AERONAUTICS")
    ventana_tipovuelo_newyork.geometry("300x250")
    Label(ventana_tipovuelo_newyork, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_newyork,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_carganorte_complejidad1_newyork).place(x=72,y=80)
    Button(ventana_tipovuelo_newyork, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad1_newyork).place(x=72,y=150)
def tipovuelo_londres():
    global ventana_tipovuelo_londres
    ventana_tipovuelo_londres = Toplevel(ventana_complejidad1)
    ventana_tipovuelo_londres.title("ITESO AERONAUTICS")
    ventana_tipovuelo_londres.geometry("300x250")
    Label(ventana_tipovuelo_londres, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_londres,text="Carga",height=2,width= 20, bg= "darkgrey", command=instrucciones_carganorte_complejidad1_londres).place(x=72,y=80)
    Button(ventana_tipovuelo_londres, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad1_londres).place(x=72,y=150)
def tipovuelo_barcelona():
    global ventana_tipovuelo_barcelona
    ventana_tipovuelo_barcelona = Toplevel(ventana_complejidad1)
    ventana_tipovuelo_barcelona.title("ITESO AERONAUTICS")
    ventana_tipovuelo_barcelona.geometry("300x250")
    Label(ventana_tipovuelo_barcelona, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_barcelona,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad1_barcelona).place(x=72,y=80)
    Button(ventana_tipovuelo_barcelona, text="Pasajeros",height= 2,width= 20, bg= "darkgrey",command= instrucciones_pasajerossur_complejidad1_barcelona).place(x=72,y=150)
def tipovuelo_roma():
    global ventana_tipovuelo_roma
    ventana_tipovuelo_roma = Toplevel(ventana_complejidad1)
    ventana_tipovuelo_roma.title("ITESO AERONAUTICS")
    ventana_tipovuelo_roma.geometry("300x250")
    Label(ventana_tipovuelo_roma, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_roma,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad1_roma).place(x=72,y=80)
    Button(ventana_tipovuelo_roma, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command=instrucciones_pasajerossur_complejidad1_roma).place(x=72,y=150)
def tipovuelo_montreal():
    global ventana_tipovuelo_montreal
    ventana_tipovuelo_montreal = Toplevel(ventana_complejidad1)
    ventana_tipovuelo_montreal.title("ITESO AERONAUTICS")
    ventana_tipovuelo_montreal.geometry("300x250")
    Label(ventana_tipovuelo_montreal, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_montreal,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_carganorte_complejidad1_montreal).place(x=72,y=80)
    Button(ventana_tipovuelo_montreal, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad1_montreal).place(x=72,y=150)
def tipovuelo_amsterdam():
    global ventana_tipovuelo_amsterdam
    ventana_tipovuelo_amsterdam = Toplevel(ventana_complejidad1)
    ventana_tipovuelo_amsterdam.title("ITESO AERONAUTICS")
    ventana_tipovuelo_amsterdam.geometry("300x250")
    Label(ventana_tipovuelo_amsterdam, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_amsterdam,text="Carga",height=2,width= 20, bg= "darkgrey", command=instrucciones_carganorte_complejidad1_paisesbajos).place(x=72,y=80)
    Button(ventana_tipovuelo_amsterdam, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad1_paisesbajos).place(x=72,y=150)
def tipovuelo_dubai():
    global ventana_tipovuelo_dubai
    ventana_tipovuelo_dubai = Toplevel(ventana_complejidad1)
    ventana_tipovuelo_dubai.title("ITESO AERONAUTICS")
    ventana_tipovuelo_dubai.geometry("300x250")
    Label(ventana_tipovuelo_dubai, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_dubai,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad1_dubai).place(x=72,y=80)
    Button(ventana_tipovuelo_dubai, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command=instrucciones_pasajerossur_complejidad1_dubai).place(x=72,y=150)
def tipovuelo_frankfurt():
    global ventana_tipovuelo_frankfurt
    ventana_tipovuelo_frankfurt = Toplevel(ventana_complejidad1)
    ventana_tipovuelo_frankfurt.title("ITESO AERONAUTICS")
    ventana_tipovuelo_frankfurt.geometry("300x250")
    Label(ventana_tipovuelo_frankfurt, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_frankfurt,text="Carga",height=2,width= 20, bg= "darkgrey",command= instrucciones_carganorte_complejidad1_frankfurt).place(x=72,y=80)
    Button(ventana_tipovuelo_frankfurt, text="Pasajeros",height= 2,width= 20, bg= "darkgrey",command=instrucciones_pasajerosnorte_complejidad1_frankfurt).place(x=72,y=150)
def tipovuelo_moscu():
    global ventana_tipovuelo_moscu
    ventana_tipovuelo_moscu = Toplevel(ventana_complejidad1)
    ventana_tipovuelo_moscu.title("ITESO AERONAUTICS")
    ventana_tipovuelo_moscu.geometry("300x250")
    Label(ventana_tipovuelo_moscu, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_moscu,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_carganorte_complejidad1_moscu).place(x=72,y=80)
    Button(ventana_tipovuelo_moscu, text="Pasajeros",height= 2,width= 20, bg= "darkgrey",command= instrucciones_pasajerosnorte_complejidad1_moscu).place(x=72,y=150)
def tipovuelo_estambul():
    global ventana_tipovuelo_estambul
    ventana_tipovuelo_estambul = Toplevel(ventana_complejidad1)
    ventana_tipovuelo_estambul.title("ITESO AERONAUTICS")
    ventana_tipovuelo_estambul.geometry("300x250")
    Label(ventana_tipovuelo_estambul, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_estambul,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad1_estambul).place(x=72,y=80)
    Button(ventana_tipovuelo_estambul, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerossur_complejidad1_estambul).place(x=72,y=150)
def instrucciones_pasajerosnorte_complejidad1_newyork():
    global ventana_instrucciones_pasajerosnorte_complejidad1_newyork
    ventana_instrucciones_pasajerosnorte_complejidad1_newyork = Toplevel(ventana_tipovuelo_newyork)
    ventana_instrucciones_pasajerosnorte_complejidad1_newyork.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad1_newyork.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_newyork, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINÚE POR LA PISTA Z3 HASTA K3 Y AGUARDE INDICACIONES"
    pista_at = "CRUCE LA PISTA 09R Y CONTINÚE POR K3 HASTA D Y ESPERE"
    pista_d = "GIRE A LA IZQUIERDA EN LA PISTA D Y CONTINÚE HASTA LA ROTONDA"
    rotonda = "GIRE POR IZQUIERDA POR BD11 HASTA BD12"
    in_term = "TOME LA RUTA 8 SOBRE LA PISTA B"
    puerta = "ESPERE EN EL EDIFICIO W Y ESPERE A SER REMOLCADO HASTAS LA PUERTA W5"
    esperar = "DESPUES DE ESTO UNICAMENTE ESPERE A SER REMOLCADO"
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_newyork, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_newyork, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_newyork, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_newyork, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_newyork, text=pista_d,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_newyork, text=rotonda ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_newyork, text=in_term ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_newyork, text=puerta ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_newyork, text=esperar ,font= ("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad1_newyork():
    global ventana_instrucciones_carganorte_complejidad1_newyork
    ventana_instrucciones_carganorte_complejidad1_newyork = Toplevel(ventana_tipovuelo_newyork)
    ventana_instrucciones_carganorte_complejidad1_newyork.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad1_newyork.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad1_newyork, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA Z1 HASTA K1 Y AGUARDE INDICACIONES"
    pista_at = "GIRE A LA DERECHA EN LA PISTA 09R Y CONTINÚE HASTA TOMAR Y1"
    pista_bd = "CONTINÚE DERECHO POR BD HACIA M Y AGUARDE EN LA INTERSECCION"
    pista_m = "GIRE POR DERECHA Y SIGA POR M HASTA LA BIFURCACIÓN"
    hangar = "GIRE A LA IZQUIERDA EN EN22 HACIA EM3 RUMBO AL PRIMER COMPLEJO DE HANGARES Y CONTINÚE POR LA PISTA"
    final = "SIGA DERECHO HASTA EL HANGAR NÚMERO 4 CON SALIDA EN EN41"
    Label(ventana_instrucciones_carganorte_complejidad1_newyork, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_newyork, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_newyork, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_newyork, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_newyork, text=pista_bd,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_newyork, text=pista_m ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_newyork, text=hangar ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_newyork, text=final ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad1_londres():
    global ventana_instrucciones_pasajerosnorte_complejidad1_londres
    ventana_instrucciones_pasajerosnorte_complejidad1_londres = Toplevel(ventana_tipovuelo_londres)
    ventana_instrucciones_pasajerosnorte_complejidad1_londres.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad1_londres.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_londres, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINÚE POR LA PISTA Z3 HASTA K3 Y AGUARDE INDICACIONES"
    pista_at = "CRUCE LA PISTA 09R Y CONTINÚE POR K3 HASTA D Y ESPERE"
    pista_d = "GIRE A LA IZQUIERDA EN LA PISTA D Y CONTINÚE HASTA LA ROTONDA"
    rotonda = "GIRE POR IZQUIERDA POR BD11 HASTA BD12"
    in_term = "TOME LA RUTA 8 SOBRE LA PISTA B"
    puerta = "ESPERE EN EL EDIFICIO W Y ESPERE A SER REMOLCADO HASTAS LA PUERTA W5"
    esperar = "DESPUES DE ESTO UNICAMENTE ESPERE A SER REMOLCADO"
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_londres, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_londres, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_londres, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_londres, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_londres, text=pista_d,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_londres, text=rotonda ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_londres, text=in_term ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_londres, text=puerta ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_londres, text=esperar ,font= ("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad1_londres():
    global ventana_instrucciones_carganorte_complejidad1_londres
    ventana_instrucciones_carganorte_complejidad1_londres = Toplevel(ventana_tipovuelo_londres)
    ventana_instrucciones_carganorte_complejidad1_londres.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad1_londres.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad1_londres, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA Z1 HASTA K1 Y AGUARDE INDICACIONES"
    pista_at = "GIRE A LA DERECHA EN LA PISTA 09R Y CONTINÚE HASTA TOMAR Y1"
    pista_bd = "CONTINÚE DERECHO POR BD HACIA M Y AGUARDE EN LA INTERSECCION"
    pista_m = "GIRE POR DERECHA Y SIGA POR M HASTA LA BIFURCACIÓN"
    hangar = "GIRE A LA IZQUIERDA EN EN22 HACIA EM3 RUMBO AL PRIMER COMPLEJO DE HANGARES Y CONTINÚE POR LA PISTA"
    final = "SIGA DERECHO HASTA EL HANGAR NÚMERO 4 CON SALIDA EN EN41"
    Label(ventana_instrucciones_carganorte_complejidad1_londres, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_londres, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_londres, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_londres, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_londres, text=pista_bd,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_londres, text=pista_m ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_londres, text=hangar ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_londres, text=final ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad1_barcelona():
    global ventana_instrucciones_pasajerosur_complejidad1_barcelona
    ventana_instrucciones_pasajerosur_complejidad1_barcelona = Toplevel(ventana_tipovuelo_barcelona)
    ventana_instrucciones_pasajerosur_complejidad1_barcelona.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad1_barcelona.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad1_barcelona, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 26L"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA V2 HASTA J Y AGUARDE INDICACIONES"
    taxiway_2 = "CRUCE J Y SIGA DERECHO POR S3 Y ESPERE"
    pista_at = "CRUCE LA PISTA 08L Y CONTINÚE POR S3 HASTA T Y ESPERE"
    pista_d = "CRUCE T Y AGUARDE EN RT3"
    rotonda = "SIGA DERECHO, CRUZANDO POR R HASTA RP1 Y ATIENDA"
    in_term = "GIRE A SU IZQUIERDA POR P Y AGUARDE A 15 METROS DE LA PUERTA A1"
    puerta = "ESPERE A SER REMOLCADO HASTA LA PUERTA A1"
    Label(ventana_instrucciones_pasajerosur_complejidad1_barcelona, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_barcelona, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_barcelona, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_barcelona, text=taxiway_2 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_barcelona, text=pista_at,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_barcelona, text=pista_d ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_barcelona, text=rotonda ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_barcelona, text=in_term ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_barcelona, text=puerta ,font= ("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad1_barcelona():
    global ventana_instrucciones_carganorte_complejidad1_barcelona
    ventana_instrucciones_carganorte_complejidad1_barcelona =  Toplevel(ventana_tipovuelo_barcelona)
    ventana_instrucciones_carganorte_complejidad1_barcelona.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad1_barcelona.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad1_barcelona, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 26L"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA V3 HASTA J Y AGUARDE INDICACIONES"
    taxiway_2 = "GIRE A LA IZQUIERDA EN J HASTA S1 Y DETÉNGASE EN 08L"
    pista_at = "CRUCE LA PISTA 08L Y CONTINÚE POR S1 HASTA C Y ESPERE"
    pista_c = "DÉ VUELTA A LA IZQUIERDA EN C HASTA UC3"
    complejo = "INGRESE AL COMPLEJO GIRANDO A LA DERECHA EN U"
    hangar = "DÉ UNA VUELTA A LA DERECHA Y SIGA DERECHO HASTA M13"
    puerta = "ESPERE A SER REMOLCADO HASTA E; HANGAR M13"
    Label(ventana_instrucciones_carganorte_complejidad1_barcelona, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_barcelona, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_barcelona, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_barcelona, text=taxiway_2 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_barcelona, text=pista_at,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_barcelona, text=pista_c ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_barcelona, text=complejo,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_barcelona, text=hangar ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_barcelona, text=puerta ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad1_roma():
    global ventana_instrucciones_pasajerosur_complejidad1_roma
    ventana_instrucciones_pasajerosur_complejidad1_roma = Toplevel(ventana_tipovuelo_roma)
    ventana_instrucciones_pasajerosur_complejidad1_roma.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad1_roma.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad1_roma, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 26L"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA V2 HASTA J Y AGUARDE INDICACIONES"
    taxiway_2 = "CRUCE J Y SIGA DERECHO POR S3 Y ESPERE"
    pista_at = "CRUCE LA PISTA 08L Y CONTINÚE POR S3 HASTA T Y ESPERE"
    pista_d = "CRUCE T Y AGUARDE EN RT3"
    rotonda = "SIGA DERECHO, CRUZANDO POR R HASTA RP1 Y ATIENDA"
    in_term = "GIRE A SU IZQUIERDA POR P Y AGUARDE A 15 METROS DE LA PUERTA A1"
    puerta = "ESPERE A SER REMOLCADO HASTA LA PUERTA A1"
    Label(ventana_instrucciones_pasajerosur_complejidad1_roma, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_roma, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_roma, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_roma, text=taxiway_2 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_roma, text=pista_at,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_roma, text=pista_d ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_roma, text=rotonda ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_roma, text=in_term ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_roma, text=puerta ,font= ("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad1_roma():
    global ventana_instrucciones_carganorte_complejidad1_roma
    ventana_instrucciones_carganorte_complejidad1_roma =  Toplevel(ventana_tipovuelo_roma)
    ventana_instrucciones_carganorte_complejidad1_roma.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad1_roma.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad1_roma, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 26L"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA V3 HASTA J Y AGUARDE INDICACIONES"
    taxiway_2 = "GIRE A LA IZQUIERDA EN J HASTA S1 Y DETÉNGASE EN 08L"
    pista_at = "CRUCE LA PISTA 08L Y CONTINÚE POR S1 HASTA C Y ESPERE"
    pista_c = "DÉ VUELTA A LA IZQUIERDA EN C HASTA UC3"
    complejo = "INGRESE AL COMPLEJO GIRANDO A LA DERECHA EN U"
    hangar = "DÉ UNA VUELTA A LA DERECHA Y SIGA DERECHO HASTA M13"
    puerta = "ESPERE A SER REMOLCADO HASTA E; HANGAR M13"
    Label(ventana_instrucciones_carganorte_complejidad1_roma, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_roma, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_roma, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_roma, text=taxiway_2 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_roma, text=pista_at,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_roma, text=pista_c ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_roma, text=complejo,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_roma, text=hangar ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_roma, text=puerta ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad1_montreal():
    global ventana_instrucciones_pasajerosnorte_complejidad1_montreal
    ventana_instrucciones_pasajerosnorte_complejidad1_montreal = Toplevel(ventana_tipovuelo_montreal)
    ventana_instrucciones_pasajerosnorte_complejidad1_montreal.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad1_montreal.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_montreal, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINÚE POR LA PISTA Z3 HASTA K3 Y AGUARDE INDICACIONES"
    pista_at = "CRUCE LA PISTA 09R Y CONTINÚE POR K3 HASTA D Y ESPERE"
    pista_d = "GIRE A LA IZQUIERDA EN LA PISTA D Y CONTINÚE HASTA LA ROTONDA"
    rotonda = "GIRE POR IZQUIERDA POR BD11 HASTA BD12"
    in_term = "TOME LA RUTA 8 SOBRE LA PISTA B"
    puerta = "ESPERE EN EL EDIFICIO W Y ESPERE A SER REMOLCADO HASTAS LA PUERTA W5"
    esperar = "DESPUES DE ESTO UNICAMENTE ESPERE A SER REMOLCADO"
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_montreal, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_montreal, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_montreal, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_montreal, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_montreal, text=pista_d,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_montreal, text=rotonda ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_montreal, text=in_term ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_montreal, text=puerta ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_montreal, text=esperar ,font= ("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad1_montreal():
    global ventana_instrucciones_carganorte_complejidad1_montreal
    ventana_instrucciones_carganorte_complejidad1_montreal = Toplevel(ventana_tipovuelo_montreal)
    ventana_instrucciones_carganorte_complejidad1_montreal.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad1_montreal.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad1_montreal, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA Z1 HASTA K1 Y AGUARDE INDICACIONES"
    pista_at = "GIRE A LA DERECHA EN LA PISTA 09R Y CONTINÚE HASTA TOMAR Y1"
    pista_bd = "CONTINÚE DERECHO POR BD HACIA M Y AGUARDE EN LA INTERSECCION"
    pista_m = "GIRE POR DERECHA Y SIGA POR M HASTA LA BIFURCACIÓN"
    hangar = "GIRE A LA IZQUIERDA EN EN22 HACIA EM3 RUMBO AL PRIMER COMPLEJO DE HANGARES Y CONTINÚE POR LA PISTA"
    final = "SIGA DERECHO HASTA EL HANGAR NÚMERO 4 CON SALIDA EN EN41"
    Label(ventana_instrucciones_carganorte_complejidad1_montreal, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_montreal, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_montreal, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_montreal, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_montreal, text=pista_bd,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_montreal, text=pista_m ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_montreal, text=hangar ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_montreal, text=final ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad1_paisesbajos():
    global ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos
    ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos = Toplevel(ventana_tipovuelo_amsterdam)
    ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINÚE POR LA PISTA Z3 HASTA K3 Y AGUARDE INDICACIONES"
    pista_at = "CRUCE LA PISTA 09R Y CONTINÚE POR K3 HASTA D Y ESPERE"
    pista_d = "GIRE A LA IZQUIERDA EN LA PISTA D Y CONTINÚE HASTA LA ROTONDA"
    rotonda = "GIRE POR IZQUIERDA POR BD11 HASTA BD12"
    in_term = "TOME LA RUTA 8 SOBRE LA PISTA B"
    puerta = "ESPERE EN EL EDIFICIO W Y ESPERE A SER REMOLCADO HASTAS LA PUERTA W5"
    esperar = "DESPUES DE ESTO UNICAMENTE ESPERE A SER REMOLCADO"
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos, text=pista_d,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos, text=rotonda ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos, text=in_term ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos, text=puerta ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_paisesbajos, text=esperar ,font= ("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad1_paisesbajos():
    global ventana_instrucciones_carganorte_complejidad1_paisesbajos
    ventana_instrucciones_carganorte_complejidad1_paisesbajos = Toplevel(ventana_tipovuelo_amsterdam)
    ventana_instrucciones_carganorte_complejidad1_paisesbajos.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad1_paisesbajos.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad1_paisesbajos, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA Z1 HASTA K1 Y AGUARDE INDICACIONES"
    pista_at = "GIRE A LA DERECHA EN LA PISTA 09R Y CONTINÚE HASTA TOMAR Y1"
    pista_bd = "CONTINÚE DERECHO POR BD HACIA M Y AGUARDE EN LA INTERSECCION"
    pista_m = "GIRE POR DERECHA Y SIGA POR M HASTA LA BIFURCACIÓN"
    hangar = "GIRE A LA IZQUIERDA EN EN22 HACIA EM3 RUMBO AL PRIMER COMPLEJO DE HANGARES Y CONTINÚE POR LA PISTA"
    final = "SIGA DERECHO HASTA EL HANGAR NÚMERO 4 CON SALIDA EN EN41"
    Label(ventana_instrucciones_carganorte_complejidad1_paisesbajos, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_paisesbajos, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_paisesbajos, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_paisesbajos, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_paisesbajos, text=pista_bd,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_paisesbajos, text=pista_m ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_paisesbajos, text=hangar ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_paisesbajos, text=final ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad1_dubai():
    global ventana_instrucciones_pasajerosur_complejidad1_dubai
    ventana_instrucciones_pasajerosur_complejidad1_dubai = Toplevel(ventana_tipovuelo_dubai)
    ventana_instrucciones_pasajerosur_complejidad1_dubai.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad1_dubai.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad1_dubai, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 26L"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA V2 HASTA J Y AGUARDE INDICACIONES"
    taxiway_2 = "CRUCE J Y SIGA DERECHO POR S3 Y ESPERE"
    pista_at = "CRUCE LA PISTA 08L Y CONTINÚE POR S3 HASTA T Y ESPERE"
    pista_d = "CRUCE T Y AGUARDE EN RT3"
    rotonda = "SIGA DERECHO, CRUZANDO POR R HASTA RP1 Y ATIENDA"
    in_term = "GIRE A SU IZQUIERDA POR P Y AGUARDE A 15 METROS DE LA PUERTA A1"
    puerta = "ESPERE A SER REMOLCADO HASTA LA PUERTA A1"
    Label(ventana_instrucciones_pasajerosur_complejidad1_dubai, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_dubai, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_dubai, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_dubai, text=taxiway_2 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_dubai, text=pista_at,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_dubai, text=pista_d ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_dubai, text=rotonda ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_dubai, text=in_term ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_dubai, text=puerta ,font= ("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad1_dubai():
    global ventana_instrucciones_carganorte_complejidad1_dubai
    ventana_instrucciones_carganorte_complejidad1_dubai =  Toplevel(ventana_tipovuelo_dubai)
    ventana_instrucciones_carganorte_complejidad1_dubai.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad1_dubai.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad1_dubai, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 26L"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA V3 HASTA J Y AGUARDE INDICACIONES"
    taxiway_2 = "GIRE A LA IZQUIERDA EN J HASTA S1 Y DETÉNGASE EN 08L"
    pista_at = "CRUCE LA PISTA 08L Y CONTINÚE POR S1 HASTA C Y ESPERE"
    pista_c = "DÉ VUELTA A LA IZQUIERDA EN C HASTA UC3"
    complejo = "INGRESE AL COMPLEJO GIRANDO A LA DERECHA EN U"
    hangar = "DÉ UNA VUELTA A LA DERECHA Y SIGA DERECHO HASTA M13"
    puerta = "ESPERE A SER REMOLCADO HASTA E; HANGAR M13"
    Label(ventana_instrucciones_carganorte_complejidad1_dubai, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_dubai, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_dubai, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_dubai, text=taxiway_2 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_dubai, text=pista_at,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_dubai, text=pista_c ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_dubai, text=complejo,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_dubai, text=hangar ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_dubai, text=puerta ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad1_frankfurt():
    global ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt
    ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt = Toplevel(ventana_tipovuelo_frankfurt)
    ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINÚE POR LA PISTA Z3 HASTA K3 Y AGUARDE INDICACIONES"
    pista_at = "CRUCE LA PISTA 09R Y CONTINÚE POR K3 HASTA D Y ESPERE"
    pista_d = "GIRE A LA IZQUIERDA EN LA PISTA D Y CONTINÚE HASTA LA ROTONDA"
    rotonda = "GIRE POR IZQUIERDA POR BD11 HASTA BD12"
    in_term = "TOME LA RUTA 8 SOBRE LA PISTA B"
    puerta = "ESPERE EN EL EDIFICIO W Y ESPERE A SER REMOLCADO HASTAS LA PUERTA W5"
    esperar = "DESPUES DE ESTO UNICAMENTE ESPERE A SER REMOLCADO"
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt, text=pista_d,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt, text=rotonda ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt, text=in_term ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt, text=puerta ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_frankfurt, text=esperar ,font= ("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad1_frankfurt():
    global ventana_instrucciones_carganorte_complejidad1_frankfurt
    ventana_instrucciones_carganorte_complejidad1_frankfurt = Toplevel(ventana_tipovuelo_frankfurt)
    ventana_instrucciones_carganorte_complejidad1_frankfurt.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad1_frankfurt.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad1_frankfurt, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA Z1 HASTA K1 Y AGUARDE INDICACIONES"
    pista_at = "GIRE A LA DERECHA EN LA PISTA 09R Y CONTINÚE HASTA TOMAR Y1"
    pista_bd = "CONTINÚE DERECHO POR BD HACIA M Y AGUARDE EN LA INTERSECCION"
    pista_m = "GIRE POR DERECHA Y SIGA POR M HASTA LA BIFURCACIÓN"
    hangar = "GIRE A LA IZQUIERDA EN EN22 HACIA EM3 RUMBO AL PRIMER COMPLEJO DE HANGARES Y CONTINÚE POR LA PISTA"
    final = "SIGA DERECHO HASTA EL HANGAR NÚMERO 4 CON SALIDA EN EN41"
    Label(ventana_instrucciones_carganorte_complejidad1_frankfurt, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_frankfurt, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_frankfurt, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_frankfurt, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_frankfurt, text=pista_bd,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_frankfurt, text=pista_m ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_frankfurt, text=hangar ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_frankfurt, text=final ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad1_moscu():
    global ventana_instrucciones_pasajerosnorte_complejidad1_moscu
    ventana_instrucciones_pasajerosnorte_complejidad1_moscu = Toplevel(ventana_tipovuelo_moscu)
    ventana_instrucciones_pasajerosnorte_complejidad1_moscu.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad1_moscu.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_moscu, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINÚE POR LA PISTA Z3 HASTA K3 Y AGUARDE INDICACIONES"
    pista_at = "CRUCE LA PISTA 09R Y CONTINÚE POR K3 HASTA D Y ESPERE"
    pista_d = "GIRE A LA IZQUIERDA EN LA PISTA D Y CONTINÚE HASTA LA ROTONDA"
    rotonda = "GIRE POR IZQUIERDA POR BD11 HASTA BD12"
    in_term = "TOME LA RUTA 8 SOBRE LA PISTA B"
    puerta = "ESPERE EN EL EDIFICIO W Y ESPERE A SER REMOLCADO HASTAS LA PUERTA W5"
    esperar = "DESPUES DE ESTO UNICAMENTE ESPERE A SER REMOLCADO"
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_moscu, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_moscu, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_moscu, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_moscu, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_moscu, text=pista_d,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_moscu, text=rotonda ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_moscu, text=in_term ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_moscu, text=puerta ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad1_moscu, text=esperar ,font= ("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad1_moscu():
    global ventana_instrucciones_carganorte_complejidad1_moscu
    ventana_instrucciones_carganorte_complejidad1_moscu = Toplevel(ventana_tipovuelo_moscu)
    ventana_instrucciones_carganorte_complejidad1_moscu.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad1_moscu.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad1_moscu, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 27R"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA Z1 HASTA K1 Y AGUARDE INDICACIONES"
    pista_at = "GIRE A LA DERECHA EN LA PISTA 09R Y CONTINÚE HASTA TOMAR Y1"
    pista_bd = "CONTINÚE DERECHO POR BD HACIA M Y AGUARDE EN LA INTERSECCION"
    pista_m = "GIRE POR DERECHA Y SIGA POR M HASTA LA BIFURCACIÓN"
    hangar = "GIRE A LA IZQUIERDA EN EN22 HACIA EM3 RUMBO AL PRIMER COMPLEJO DE HANGARES Y CONTINÚE POR LA PISTA"
    final = "SIGA DERECHO HASTA EL HANGAR NÚMERO 4 CON SALIDA EN EN41"
    Label(ventana_instrucciones_carganorte_complejidad1_moscu, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_moscu, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_moscu, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_moscu, text=pista_at ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_moscu, text=pista_bd,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_moscu, text=pista_m ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_moscu, text=hangar ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_moscu, text=final ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad1_estambul():
    global ventana_instrucciones_pasajerosur_complejidad1_estambul
    ventana_instrucciones_pasajerosur_complejidad1_estambul = Toplevel(ventana_tipovuelo_estambul)
    ventana_instrucciones_pasajerosur_complejidad1_estambul.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad1_estambul.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad1_estambul, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 26L"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA V2 HASTA J Y AGUARDE INDICACIONES"
    taxiway_2 = "CRUCE J Y SIGA DERECHO POR S3 Y ESPERE"
    pista_at = "CRUCE LA PISTA 08L Y CONTINÚE POR S3 HASTA T Y ESPERE"
    pista_d = "CRUCE T Y AGUARDE EN RT3"
    rotonda = "SIGA DERECHO, CRUZANDO POR R HASTA RP1 Y ATIENDA"
    in_term = "GIRE A SU IZQUIERDA POR P Y AGUARDE A 15 METROS DE LA PUERTA A1"
    puerta = "ESPERE A SER REMOLCADO HASTA LA PUERTA A1"
    Label(ventana_instrucciones_pasajerosur_complejidad1_estambul, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_estambul, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_estambul, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_estambul, text=taxiway_2 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_estambul, text=pista_at,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_estambul, text=pista_d ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_estambul, text=rotonda ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_estambul, text=in_term ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad1_estambul, text=puerta ,font= ("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad1_estambul():
    global ventana_instrucciones_carganorte_complejidad1_estambul
    ventana_instrucciones_carganorte_complejidad1_estambul =  Toplevel(ventana_tipovuelo_estambul)
    ventana_instrucciones_carganorte_complejidad1_estambul.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad1_estambul.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad1_estambul, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    aterrizaje = "ATERRICE EN LA PISTA 26L"
    vel = "REDUZCA SU VELOCIDAD A 4 NUDOS Y AGUARDE INDICACIONES"
    taxiway_1 = "CONTINUE POR LA PISTA V3 HASTA J Y AGUARDE INDICACIONES"
    taxiway_2 = "GIRE A LA IZQUIERDA EN J HASTA S1 Y DETÉNGASE EN 08L"
    pista_at = "CRUCE LA PISTA 08L Y CONTINÚE POR S1 HASTA C Y ESPERE"
    pista_c = "DÉ VUELTA A LA IZQUIERDA EN C HASTA UC3"
    complejo = "INGRESE AL COMPLEJO GIRANDO A LA DERECHA EN U"
    hangar = "DÉ UNA VUELTA A LA DERECHA Y SIGA DERECHO HASTA M13"
    puerta = "ESPERE A SER REMOLCADO HASTA E; HANGAR M13"
    Label(ventana_instrucciones_carganorte_complejidad1_estambul, text=aterrizaje ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_estambul, text=vel ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_estambul, text=taxiway_1,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_estambul, text=taxiway_2 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_estambul, text=pista_at,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_estambul, text=pista_c ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_estambul, text=complejo,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_estambul, text=hangar ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_estambul, text=puerta ,font= ("Calibri", 11)).pack()
#Complejidad3
def complejidad3_ventana():
    global ventana_complejidad3
    ventana_complejidad3 = Toplevel(ventana_seleccionar_dificultad)
    ventana_complejidad3.title("ITESO AERONAUTICS")
    ventana_complejidad3.geometry("300x340")
    Label(ventana_complejidad3, text= "De donde vienes?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_complejidad3, text="JFK - New York", height= 1,width= 20, bg= "darkgrey",command=tipovuelo_newyork3).pack(())
    Button(ventana_complejidad3, text="LYC - Londres", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_londres3).pack(())
    Button(ventana_complejidad3, text="BCN - Barcelona", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_barcelona3).pack(())
    Button(ventana_complejidad3, text="FCO - Roma", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_roma3).pack(())
    Button(ventana_complejidad3, text="YUL - Montreal", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_montreal3).pack(())
    Button(ventana_complejidad3, text="AMS - Ámsterdam", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_amsterdam3).pack(())
    Button(ventana_complejidad3, text="DXB - Dubái", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_dubai3).pack(())
    Button(ventana_complejidad3, text="FRA - Fránkfurt", height= 1,width= 20, bg= "darkgrey", command=tipovuelo_frankfurt3).pack(())
    Button(ventana_complejidad3, text="SVO - Moscú", height= 1,width= 20, bg= "darkgrey", command=tipovuelo_moscu3).pack(())
    Button(ventana_complejidad3, text="IST - Estambul", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_estambul3).pack(())
def tipovuelo_newyork3():
    global ventana_tipovuelo_newyork3
    ventana_tipovuelo_newyork3 = Toplevel(ventana_complejidad3)
    ventana_tipovuelo_newyork3.title("ITESO AERONAUTICS")
    ventana_tipovuelo_newyork3.geometry("300x250")
    Label(ventana_tipovuelo_newyork3, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_newyork3,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_carganorte_complejidad3_newyork3).place(x=72,y=80)
    Button(ventana_tipovuelo_newyork3, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad3_newyork3).place(x=72,y=150)
def tipovuelo_londres3():
    global ventana_tipovuelo_londres3
    ventana_tipovuelo_londres3 = Toplevel(ventana_complejidad3)
    ventana_tipovuelo_londres3.title("ITESO AERONAUTICS")
    ventana_tipovuelo_londres3.geometry("300x250")
    Label(ventana_tipovuelo_londres3, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_londres3,text="Carga",height=2,width= 20, bg= "darkgrey", command=instrucciones_carga_complejidad3_londres).place(x=72,y=80)
    Button(ventana_tipovuelo_londres3, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad3_londres).place(x=72,y=150)
def tipovuelo_barcelona3():
    global ventana_tipovuelo_barcelona3
    ventana_tipovuelo_barcelona3 = Toplevel(ventana_complejidad3)
    ventana_tipovuelo_barcelona3.title("ITESO AERONAUTICS")
    ventana_tipovuelo_barcelona3.geometry("300x250")
    Label(ventana_tipovuelo_barcelona3, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_barcelona3, text="Carga", height=2, width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad3_barcelona3()).place(x=72, y=80)
    Button(ventana_tipovuelo_barcelona3, text="Pasajeros",height= 2,width= 20, bg= "darkgrey",command= instrucciones_pasajerossur_complejidad3_barcelona3).place(x=72,y=150)
def tipovuelo_roma3():
    global ventana_tipovuelo_roma3
    ventana_tipovuelo_roma3 = Toplevel(ventana_complejidad3)
    ventana_tipovuelo_roma3.title("ITESO AERONAUTICS")
    ventana_tipovuelo_roma3.geometry("300x250")
    Label(ventana_tipovuelo_roma3, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_roma3,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad3_roma).place(x=72,y=80)
    Button(ventana_tipovuelo_roma3, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command=instrucciones_pasajerossur_complejidad3_roma).place(x=72,y=150)
def tipovuelo_montreal3():
    global ventana_tipovuelo_montreal3
    ventana_tipovuelo_montreal3 = Toplevel(ventana_complejidad3)
    ventana_tipovuelo_montreal3.title("ITESO AERONAUTICS")
    ventana_tipovuelo_montreal3.geometry("300x250")
    Label(ventana_tipovuelo_montreal3, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_montreal3,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_carganorte_complejidad3_montreal).place(x=72,y=80)
    Button(ventana_tipovuelo_montreal3, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad3_montreal).place(x=72,y=150)
def tipovuelo_amsterdam3():
    global ventana_tipovuelo_amsterdam3
    ventana_tipovuelo_amsterdam3 = Toplevel(ventana_complejidad3)
    ventana_tipovuelo_amsterdam3.title("ITESO AERONAUTICS")
    ventana_tipovuelo_amsterdam3.geometry("300x250")
    Label(ventana_tipovuelo_amsterdam3, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_amsterdam3,text="Carga",height=2,width= 20, bg= "darkgrey", command=instrucciones_carganorte_complejidad3_paisesbajos).place(x=72,y=80)
    Button(ventana_tipovuelo_amsterdam3, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad3_paisesbajos).place(x=72,y=150)
def tipovuelo_dubai3():
    global ventana_tipovuelo_dubai3
    ventana_tipovuelo_dubai3 = Toplevel(ventana_complejidad3)
    ventana_tipovuelo_dubai3.title("ITESO AERONAUTICS")
    ventana_tipovuelo_dubai3.geometry("300x250")
    Label(ventana_tipovuelo_dubai3, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_dubai3,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad3_dubai).place(x=72,y=80)
    Button(ventana_tipovuelo_dubai3, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command=instrucciones_pasajerossur_complejidad3_dubai).place(x=72,y=150)
def tipovuelo_frankfurt3():
    global ventana_tipovuelo_frankfurt3
    ventana_tipovuelo_frankfurt3 = Toplevel(ventana_complejidad3)
    ventana_tipovuelo_frankfurt3.title("ITESO AERONAUTICS")
    ventana_tipovuelo_frankfurt3.geometry("300x250")
    Label(ventana_tipovuelo_frankfurt3, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_frankfurt3,text="Carga",height=2,width= 20, bg= "darkgrey",command= instrucciones_carganorte_complejidad3_frankfurt).place(x=72,y=80)
    Button(ventana_tipovuelo_frankfurt3, text="Pasajeros",height= 2,width= 20, bg= "darkgrey",command=instrucciones_pasajerosnorte_complejidad3_frankfurt).place(x=72,y=150)
def tipovuelo_moscu3():
    global ventana_tipovuelo_moscu3
    ventana_tipovuelo_moscu3 = Toplevel(ventana_complejidad3)
    ventana_tipovuelo_moscu3.title("ITESO AERONAUTICS")
    ventana_tipovuelo_moscu3.geometry("300x250")
    Label(ventana_tipovuelo_moscu3, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_moscu3,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_carganorte_complejidad3_moscu).place(x=72,y=80)
    Button(ventana_tipovuelo_moscu3, text="Pasajeros",height= 2,width= 20, bg= "darkgrey",command= instrucciones_pasajerosnorte_complejidad3_moscu).place(x=72,y=150)
def tipovuelo_estambul3():
    global ventana_tipovuelo_estambul3
    ventana_tipovuelo_estambul3 = Toplevel(ventana_complejidad3)
    ventana_tipovuelo_estambul3.title("ITESO AERONAUTICS")
    ventana_tipovuelo_estambul3.geometry("300x250")
    Label(ventana_tipovuelo_estambul3, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_estambul3,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad3_estambul).place(x=72,y=80)
    Button(ventana_tipovuelo_estambul3 , text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerossur_complejidad3_estambul).place(x=72,y=150)
def instrucciones_pasajerosnorte_complejidad3_newyork3():
    global ventana_instrucciones_pasajerosnorte_complejidad3_newyork
    ventana_instrucciones_pasajerosnorte_complejidad3_newyork = Toplevel(ventana_tipovuelo_newyork3)
    ventana_instrucciones_pasajerosnorte_complejidad3_newyork.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad3_newyork.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_newyork, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_pasajeros_3()
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_newyork, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_newyork, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad3_newyork3():
    global ventana_instrucciones_carganorte_complejidad1_newyork3
    ventana_instrucciones_carganorte_complejidad1_newyork3 = Toplevel(ventana_tipovuelo_newyork3)
    ventana_instrucciones_carganorte_complejidad1_newyork3.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad1_newyork3.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad1_newyork3, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_carga_3()
    instrucciones2 = TERMINALES.hangares_norte()
    Label(ventana_instrucciones_carganorte_complejidad1_newyork3, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad1_newyork3, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_carga_complejidad3_londres():
    global ventana_instrucciones_carganorte_complejidad3_londres
    ventana_instrucciones_carganorte_complejidad3_londres = Toplevel(ventana_tipovuelo_londres3)
    ventana_instrucciones_carganorte_complejidad3_londres.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad3_londres.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad3_londres, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_carga_3()
    instrucciones2 = TERMINALES.hangares_norte()

    Label(ventana_instrucciones_carganorte_complejidad3_londres, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad3_londres, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad3_londres():
    global ventana_instrucciones_pasajerosnorte_complejidad3_londres
    ventana_instrucciones_pasajerosnorte_complejidad3_londres = Toplevel(ventana_tipovuelo_londres3)
    ventana_instrucciones_pasajerosnorte_complejidad3_londres.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad3_londres.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_londres, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_pasajeros_3()
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_londres, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_londres, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad3_barcelona3():
    global ventana_instrucciones_pasajerosur_complejidad3_barcelona
    ventana_instrucciones_pasajerosur_complejidad3_barcelona = Toplevel(ventana_tipovuelo_barcelona3)
    ventana_instrucciones_pasajerosur_complejidad3_barcelona.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad3_barcelona.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad3_barcelona, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.sur_pasajeros_3()
    instrucciones2 = TERMINALES.terminal_sur()
    Label(ventana_instrucciones_pasajerosur_complejidad3_barcelona, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad3_barcelona, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad3_barcelona3():
    global ventana_instrucciones_carganorte_complejidad3_barcelona
    ventana_instrucciones_carganorte_complejidad3_barcelona =  Toplevel(ventana_tipovuelo_barcelona3)
    ventana_instrucciones_carganorte_complejidad3_barcelona.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad3_barcelona.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad3_barcelona, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.sur_carga_3()
    instrucciones2 = TERMINALES.hangares_sur()
    Label(ventana_instrucciones_carganorte_complejidad3_barcelona, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad3_barcelona, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad3_roma():
    global ventana_instrucciones_pasajerosur_complejidad3_roma
    ventana_instrucciones_pasajerosur_complejidad3_roma = Toplevel(ventana_tipovuelo_roma3)
    ventana_instrucciones_pasajerosur_complejidad3_roma.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad3_roma.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad3_roma, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.sur_pasajeros_3()
    instrucciones2 = TERMINALES.terminal_sur()
    Label(ventana_instrucciones_pasajerosur_complejidad3_roma, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad3_roma, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad3_roma():
    global ventana_instrucciones_carganorte_complejidad3_roma
    ventana_instrucciones_carganorte_complejidad3_roma =  Toplevel(ventana_tipovuelo_roma3)
    ventana_instrucciones_carganorte_complejidad3_roma.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad3_roma.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad3_roma, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.sur_carga_3()
    instrucciones2 = TERMINALES.hangares_sur()
    Label(ventana_instrucciones_carganorte_complejidad3_roma, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad3_roma, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad3_montreal():
    global ventana_instrucciones_pasajerosnorte_complejidad3_montreal
    ventana_instrucciones_pasajerosnorte_complejidad3_montreal = Toplevel(ventana_tipovuelo_montreal3)
    ventana_instrucciones_pasajerosnorte_complejidad3_montreal.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad3_montreal.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_montreal, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_pasajeros_3()
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_montreal, text=instrucciones1, font=("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_montreal, text=instrucciones2, font=("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad3_montreal():
    global ventana_instrucciones_carganorte_complejidad3_montreal
    ventana_instrucciones_carganorte_complejidad3_montreal = Toplevel(ventana_tipovuelo_montreal3)
    ventana_instrucciones_carganorte_complejidad3_montreal.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad3_montreal.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad3_montreal, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_carga_3()
    instrucciones2 = TERMINALES.hangares_norte()
    Label(ventana_instrucciones_carganorte_complejidad3_montreal, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad3_montreal, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad3_paisesbajos():
    global ventana_instrucciones_pasajerosnorte_complejidad3_paisesbajos
    ventana_instrucciones_pasajerosnorte_complejidad3_paisesbajos = Toplevel(ventana_tipovuelo_amsterdam3)
    ventana_instrucciones_pasajerosnorte_complejidad3_paisesbajos.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad3_paisesbajos.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_paisesbajos, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_pasajeros_3()
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_paisesbajos, text=instrucciones1, font=("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_paisesbajos, text=instrucciones2, font=("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad3_paisesbajos():
    global ventana_instrucciones_carganorte_complejidad3_paisesbajos
    ventana_instrucciones_carganorte_complejidad3_paisesbajos = Toplevel(ventana_tipovuelo_amsterdam3)
    ventana_instrucciones_carganorte_complejidad3_paisesbajos.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad3_paisesbajos.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad3_paisesbajos, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_carga_3()
    instrucciones2 = TERMINALES.hangares_norte()
    Label(ventana_instrucciones_carganorte_complejidad3_paisesbajos, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad3_paisesbajos, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad3_dubai():
    global ventana_instrucciones_pasajerosur_complejidad3_dubai
    ventana_instrucciones_pasajerosur_complejidad3_dubai = Toplevel(ventana_tipovuelo_dubai3)
    ventana_instrucciones_pasajerosur_complejidad3_dubai.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad3_dubai.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad3_dubai, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.sur_pasajeros_3()
    instrucciones2 = TERMINALES.terminal_sur()
    Label(ventana_instrucciones_pasajerosur_complejidad3_dubai, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad3_dubai, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad3_dubai():
    global ventana_instrucciones_carganorte_complejidad3_dubai
    ventana_instrucciones_carganorte_complejidad3_dubai =  Toplevel(ventana_tipovuelo_dubai3)
    ventana_instrucciones_carganorte_complejidad3_dubai.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad3_dubai.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad3_dubai, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.sur_carga_3()
    instrucciones2 = TERMINALES.hangares_sur()
    Label(ventana_instrucciones_carganorte_complejidad3_dubai, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad3_dubai, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad3_frankfurt():
    global ventana_instrucciones_pasajerosnorte_complejidad3_frankfurt
    ventana_instrucciones_pasajerosnorte_complejidad3_frankfurt = Toplevel(ventana_tipovuelo_frankfurt3)
    ventana_instrucciones_pasajerosnorte_complejidad3_frankfurt.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad3_frankfurt.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_frankfurt, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_pasajeros_3()
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_frankfurt, text=instrucciones1, font=("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_frankfurt, text=instrucciones2, font=("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad3_frankfurt():
    global ventana_instrucciones_carganorte_complejidad3_frankfurt
    ventana_instrucciones_carganorte_complejidad3_frankfurt = Toplevel(ventana_tipovuelo_frankfurt3)
    ventana_instrucciones_carganorte_complejidad3_frankfurt.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad3_frankfurt.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad3_frankfurt, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_carga_3()
    instrucciones2 = TERMINALES.hangares_norte()
    Label(ventana_instrucciones_carganorte_complejidad3_frankfurt, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad3_frankfurt, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad3_moscu():
    global ventana_instrucciones_pasajerosnorte_complejidad3_moscu
    ventana_instrucciones_pasajerosnorte_complejidad3_moscu = Toplevel(ventana_tipovuelo_moscu3)
    ventana_instrucciones_pasajerosnorte_complejidad3_moscu.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad3_moscu.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_moscu, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_pasajeros_3()
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_moscu, text=instrucciones1, font=("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_moscu, text=instrucciones2, font=("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad3_moscu():
    global ventana_instrucciones_carganorte_complejidad3_moscu
    ventana_instrucciones_carganorte_complejidad3_moscu = Toplevel(ventana_tipovuelo_moscu3)
    ventana_instrucciones_carganorte_complejidad3_moscu.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad3_moscu.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad3_moscu, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_carga_3()
    instrucciones2 = TERMINALES.hangares_norte()
    Label(ventana_instrucciones_carganorte_complejidad3_moscu, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad3_moscu, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad3_estambul():
    global ventana_instrucciones_pasajerosur_complejidad3_estambul
    ventana_instrucciones_pasajerosur_complejidad3_estambul = Toplevel(ventana_tipovuelo_estambul3)
    ventana_instrucciones_pasajerosur_complejidad3_estambul.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad3_estambul.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad3_estambul, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.norte_pasajeros_3()
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosur_complejidad3_estambul, text=instrucciones1, font=("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad3_estambul, text=instrucciones2, font=("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad3_estambul():
    global ventana_instrucciones_carganorte_complejidad3_estambul
    ventana_instrucciones_carganorte_complejidad3_estambul =  Toplevel(ventana_tipovuelo_estambul3)
    ventana_instrucciones_carganorte_complejidad3_estambul.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad3_estambul.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad3_estambul, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_3.sur_carga_3()
    instrucciones2 = TERMINALES.hangares_sur()
    Label(ventana_instrucciones_carganorte_complejidad3_estambul, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad3_estambul, text=instrucciones2 ,font= ("Calibri", 11)).pack()
#Complejidad2
def complejidad2_ventana():
    global ventana_complejidad2
    ventana_complejidad2 = Toplevel(ventana_seleccionar_dificultad)
    ventana_complejidad2.title("ITESO AERONAUTICS")
    ventana_complejidad2.geometry("300x340")
    Label(ventana_complejidad2, text= "De donde vienes?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_complejidad2, text="JFK - New York", height= 1,width= 20, bg= "darkgrey",command=tipovuelo_newyork2).pack(())
    Button(ventana_complejidad2, text="LYC - Londres", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_londres2).pack(())
    Button(ventana_complejidad2, text="BCN - Barcelona", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_barcelona2).pack(())
    Button(ventana_complejidad2, text="FCO - Roma", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_roma2).pack(())
    Button(ventana_complejidad2, text="YUL - Montreal", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_montreal2).pack(())
    Button(ventana_complejidad2, text="AMS - Ámsterdam", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_amsterdam2).pack(())
    Button(ventana_complejidad2, text="DXB - Dubái", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_dubai2).pack(())
    Button(ventana_complejidad2, text="FRA - Fránkfurt", height= 1,width= 20, bg= "darkgrey", command=tipovuelo_frankfurt2).pack(())
    Button(ventana_complejidad2, text="SVO - Moscú", height= 1,width= 20, bg= "darkgrey", command=tipovuelo_moscu2).pack(())
    Button(ventana_complejidad2, text="IST - Estambul", height= 1,width= 20, bg= "darkgrey", command= tipovuelo_estambul2).pack(())
def tipovuelo_newyork2():
    global ventana_tipovuelo_newyork2
    ventana_tipovuelo_newyork2 = Toplevel(ventana_complejidad2)
    ventana_tipovuelo_newyork2.title("ITESO AERONAUTICS")
    ventana_tipovuelo_newyork2.geometry("300x250")
    Label(ventana_tipovuelo_newyork2, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_newyork2,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_carganorte_complejidad2_newyork).place(x=72,y=80)
    Button(ventana_tipovuelo_newyork2, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad2_newyork).place(x=72,y=150)
def tipovuelo_londres2():
    global ventana_tipovuelo_londres2
    ventana_tipovuelo_londres2 = Toplevel(ventana_complejidad2)
    ventana_tipovuelo_londres2.title("ITESO AERONAUTICS")
    ventana_tipovuelo_londres2.geometry("300x250")
    Label(ventana_tipovuelo_londres2, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_londres2,text="Carga",height=2,width= 20, bg= "darkgrey", command=instrucciones_carga_complejidad2_londres).place(x=72,y=80)
    Button(ventana_tipovuelo_londres2, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad2_londres).place(x=72,y=150)
def tipovuelo_barcelona2():
    global ventana_tipovuelo_barcelona2
    ventana_tipovuelo_barcelona2 = Toplevel(ventana_complejidad2)
    ventana_tipovuelo_barcelona2.title("ITESO AERONAUTICS")
    ventana_tipovuelo_barcelona2.geometry("300x250")
    Label(ventana_tipovuelo_barcelona2, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_barcelona2, text="Carga", height=2, width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad2_barcelona).place(x=72, y=80)
    Button(ventana_tipovuelo_barcelona2, text="Pasajeros",height= 2,width= 20, bg= "darkgrey",command= instrucciones_pasajerossur_complejidad2_barcelona).place(x=72,y=150)
def tipovuelo_roma2():
    global ventana_tipovuelo_roma2
    ventana_tipovuelo_roma2 = Toplevel(ventana_complejidad2)
    ventana_tipovuelo_roma2.title("ITESO AERONAUTICS")
    ventana_tipovuelo_roma2.geometry("300x250")
    Label(ventana_tipovuelo_roma2, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_roma2,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad2_roma).place(x=72,y=80)
    Button(ventana_tipovuelo_roma2, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command=instrucciones_pasajerossur_complejidad2_roma).place(x=72,y=150)
def tipovuelo_montreal2():
    global ventana_tipovuelo_montreal2
    ventana_tipovuelo_montreal2 = Toplevel(ventana_complejidad2)
    ventana_tipovuelo_montreal2.title("ITESO AERONAUTICS")
    ventana_tipovuelo_montreal2.geometry("300x250")
    Label(ventana_tipovuelo_montreal2, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_montreal2,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_carganorte_complejidad2_montreal).place(x=72,y=80)
    Button(ventana_tipovuelo_montreal2, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad2_montreal).place(x=72,y=150)
def tipovuelo_amsterdam2():
    global ventana_tipovuelo_amsterdam2
    ventana_tipovuelo_amsterdam2 = Toplevel(ventana_complejidad2)
    ventana_tipovuelo_amsterdam2.title("ITESO AERONAUTICS")
    ventana_tipovuelo_amsterdam2.geometry("300x250")
    Label(ventana_tipovuelo_amsterdam2, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_amsterdam2,text="Carga",height=2,width= 20, bg= "darkgrey", command=instrucciones_carganorte_complejidad2_paisesbajos).place(x=72,y=80)
    Button(ventana_tipovuelo_amsterdam2, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerosnorte_complejidad2_paisesbajos).place(x=72,y=150)
def tipovuelo_dubai2():
    global ventana_tipovuelo_dubai2
    ventana_tipovuelo_dubai2 = Toplevel(ventana_complejidad2)
    ventana_tipovuelo_dubai2.title("ITESO AERONAUTICS")
    ventana_tipovuelo_dubai2.geometry("300x250")
    Label(ventana_tipovuelo_dubai2, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_dubai2,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad2_dubai).place(x=72,y=80)
    Button(ventana_tipovuelo_dubai2, text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command=instrucciones_pasajerossur_complejidad2_dubai).place(x=72,y=150)
def tipovuelo_frankfurt2():
    global ventana_tipovuelo_frankfurt2
    ventana_tipovuelo_frankfurt2 = Toplevel(ventana_complejidad2)
    ventana_tipovuelo_frankfurt2.title("ITESO AERONAUTICS")
    ventana_tipovuelo_frankfurt2.geometry("300x250")
    Label(ventana_tipovuelo_frankfurt2, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_frankfurt2,text="Carga",height=2,width= 20, bg= "darkgrey",command= instrucciones_carganorte_complejidad2_frankfurt).place(x=72,y=80)
    Button(ventana_tipovuelo_frankfurt2, text="Pasajeros",height= 2,width= 20, bg= "darkgrey",command=instrucciones_pasajerosnorte_complejidad2_frankfurt).place(x=72,y=150)
def tipovuelo_moscu2():
    global ventana_tipovuelo_moscu2
    ventana_tipovuelo_moscu2 = Toplevel(ventana_complejidad2)
    ventana_tipovuelo_moscu2.title("ITESO AERONAUTICS")
    ventana_tipovuelo_moscu2.geometry("300x250")
    Label(ventana_tipovuelo_moscu2, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_moscu2,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_carganorte_complejidad2_moscu).place(x=72,y=80)
    Button(ventana_tipovuelo_moscu2, text="Pasajeros",height= 2,width= 20, bg= "darkgrey",command= instrucciones_pasajerosnorte_complejidad2_moscu).place(x=72,y=150)
def tipovuelo_estambul2():
    global ventana_tipovuelo_estambul2
    ventana_tipovuelo_estambul2 = Toplevel(ventana_complejidad2)
    ventana_tipovuelo_estambul2.title("ITESO AERONAUTICS")
    ventana_tipovuelo_estambul2.geometry("300x250")
    Label(ventana_tipovuelo_estambul2, text="Cual es su tipo de vuelo?", width= "300", height="2", font=("Calibri", 13)).pack()
    Button(ventana_tipovuelo_estambul2,text="Carga",height=2,width= 20, bg= "darkgrey", command= instrucciones_cargasur_complejidad2_estambul).place(x=72,y=80)
    Button(ventana_tipovuelo_estambul2 , text="Pasajeros",height= 2,width= 20, bg= "darkgrey", command= instrucciones_pasajerossur_complejidad2_estambul).place(x=72,y=150)
def instrucciones_pasajerosnorte_complejidad2_newyork():
    global ventana_instrucciones_pasajerosnorte_complejidad2_newyork
    ventana_instrucciones_pasajerosnorte_complejidad2_newyork = Toplevel(ventana_tipovuelo_newyork2)
    ventana_instrucciones_pasajerosnorte_complejidad2_newyork.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad2_newyork.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_newyork, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_pasajeros_2()  #CORREGIR ESTO
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_newyork, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_newyork, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad2_newyork():
    global ventana_instrucciones_carganorte_complejidad2_newyork
    ventana_instrucciones_carganorte_complejidad2_newyork = Toplevel(ventana_tipovuelo_newyork2)
    ventana_instrucciones_carganorte_complejidad2_newyork.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad2_newyork.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad2_newyork, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_carga_2()
    instrucciones2 = TERMINALES.hangares_norte()
    Label(ventana_instrucciones_carganorte_complejidad2_newyork, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad2_newyork, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_carga_complejidad2_londres():
    global ventana_instrucciones_carganorte_complejidad2_londres
    ventana_instrucciones_carganorte_complejidad2_londres = Toplevel(ventana_tipovuelo_londres3)
    ventana_instrucciones_carganorte_complejidad2_londres.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad2_londres.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad2_londres, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_carga_2()  #Corregir esto
    instrucciones2 = TERMINALES.hangares_norte()
    Label(ventana_instrucciones_carganorte_complejidad2_londres, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad2_londres, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad2_londres():
    global ventana_instrucciones_pasajerosnorte_complejidad2_londres
    ventana_instrucciones_pasajerosnorte_complejidad2_londres = Toplevel(ventana_tipovuelo_londres2)
    ventana_instrucciones_pasajerosnorte_complejidad2_londres.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad2_londres.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_londres, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_pasajeros_2() #Corregir esta
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_londres, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_londres, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad2_barcelona():
    global ventana_instrucciones_pasajerosur_complejidad2_barcelona
    ventana_instrucciones_pasajerosur_complejidad2_barcelona = Toplevel(ventana_tipovuelo_barcelona2)
    ventana_instrucciones_pasajerosur_complejidad2_barcelona.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad2_barcelona.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad2_barcelona, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.sur_pasajeros_2()    #Corregir esto
    instrucciones2 = TERMINALES.terminal_sur()
    Label(ventana_instrucciones_pasajerosur_complejidad2_barcelona, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad2_barcelona, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad2_barcelona():
    global ventana_instrucciones_carganorte_complejidad2_barcelona
    ventana_instrucciones_carganorte_complejidad2_barcelona =  Toplevel(ventana_tipovuelo_barcelona2)
    ventana_instrucciones_carganorte_complejidad2_barcelona.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad2_barcelona.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad2_barcelona, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.sur_carga_2() # Corregir esto
    instrucciones2 = TERMINALES.hangares_sur()
    Label(ventana_instrucciones_carganorte_complejidad2_barcelona, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad2_barcelona, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad2_roma():
    global ventana_instrucciones_pasajerosur_complejidad2_roma
    ventana_instrucciones_pasajerosur_complejidad2_roma = Toplevel(ventana_tipovuelo_roma2)
    ventana_instrucciones_pasajerosur_complejidad2_roma.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad2_roma.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad2_roma, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.sur_pasajeros_2() #Corrgir esto
    instrucciones2 = TERMINALES.terminal_sur()
    Label(ventana_instrucciones_pasajerosur_complejidad2_roma, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad2_roma, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad2_roma():
    global ventana_instrucciones_carganorte_complejidad2_roma
    ventana_instrucciones_carganorte_complejidad2_roma =  Toplevel(ventana_tipovuelo_roma2)
    ventana_instrucciones_carganorte_complejidad2_roma.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad2_roma.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad2_roma, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.sur_carga_2() #corregir esto
    instrucciones2 = TERMINALES.hangares_sur()
    Label(ventana_instrucciones_carganorte_complejidad2_roma, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad2_roma, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad2_montreal():
    global ventana_instrucciones_pasajerosnorte_complejidad2_montreal
    ventana_instrucciones_pasajerosnorte_complejidad2_montreal = Toplevel(ventana_tipovuelo_montreal2)
    ventana_instrucciones_pasajerosnorte_complejidad2_montreal.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad2_montreal.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_montreal, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_pasajeros_2()  #corregir esto
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_montreal, text=instrucciones1, font=("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad3_montreal, text=instrucciones2, font=("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad2_montreal():
    global ventana_instrucciones_carganorte_complejidad2_montreal
    ventana_instrucciones_carganorte_complejidad2_montreal = Toplevel(ventana_tipovuelo_montreal2)
    ventana_instrucciones_carganorte_complejidad2_montreal.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad2_montreal.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad2_montreal, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_carga_2()  #corregir esto
    instrucciones2 = TERMINALES.hangares_norte()
    Label(ventana_instrucciones_carganorte_complejidad2_montreal, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad2_montreal, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad2_paisesbajos():
    global ventana_instrucciones_pasajerosnorte_complejidad2_paisesbajos
    ventana_instrucciones_pasajerosnorte_complejidad2_paisesbajos = Toplevel(ventana_tipovuelo_amsterdam2)
    ventana_instrucciones_pasajerosnorte_complejidad2_paisesbajos.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad2_paisesbajos.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_paisesbajos, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_pasajeros_2()  #corregir esto
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_paisesbajos, text=instrucciones1, font=("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_paisesbajos, text=instrucciones2, font=("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad2_paisesbajos():
    global ventana_instrucciones_carganorte_complejidad2_paisesbajos
    ventana_instrucciones_carganorte_complejidad2_paisesbajos = Toplevel(ventana_tipovuelo_amsterdam2)
    ventana_instrucciones_carganorte_complejidad2_paisesbajos.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad2_paisesbajos.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad2_paisesbajos, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_carga_2()  # corrgir esto
    instrucciones2 = TERMINALES.hangares_norte()
    Label(ventana_instrucciones_carganorte_complejidad2_paisesbajos, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad2_paisesbajos, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad2_dubai():
    global ventana_instrucciones_pasajerosur_complejidad2_dubai
    ventana_instrucciones_pasajerosur_complejidad2_dubai = Toplevel(ventana_tipovuelo_dubai2)
    ventana_instrucciones_pasajerosur_complejidad2_dubai.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad2_dubai.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad2_dubai, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.sur_pasajeros_2()    #corregir esto
    instrucciones2 = TERMINALES.terminal_sur()
    Label(ventana_instrucciones_pasajerosur_complejidad2_dubai, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad2_dubai, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad2_dubai():
    global ventana_instrucciones_carganorte_complejidad2_dubai
    ventana_instrucciones_carganorte_complejidad2_dubai =  Toplevel(ventana_tipovuelo_dubai2)
    ventana_instrucciones_carganorte_complejidad2_dubai.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad2_dubai.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad2_dubai, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.sur_carga_2()    #corregir esto
    instrucciones2 = TERMINALES.hangares_sur()
    Label(ventana_instrucciones_carganorte_complejidad2_dubai, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad2_dubai, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad2_frankfurt():
    global ventana_instrucciones_pasajerosnorte_complejidad2_frankfurt
    ventana_instrucciones_pasajerosnorte_complejidad2_frankfurt = Toplevel(ventana_tipovuelo_frankfurt2)
    ventana_instrucciones_pasajerosnorte_complejidad2_frankfurt.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad2_frankfurt.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_frankfurt, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_pasajeros_2()  #corregir esto
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_frankfurt, text=instrucciones1, font=("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_frankfurt, text=instrucciones2, font=("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad2_frankfurt():
    global ventana_instrucciones_carganorte_complejidad2_frankfurt
    ventana_instrucciones_carganorte_complejidad2_frankfurt = Toplevel(ventana_tipovuelo_frankfurt2)
    ventana_instrucciones_carganorte_complejidad2_frankfurt.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad2_frankfurt.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad2_frankfurt, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_carga_2()  #corregir esto
    instrucciones2 = TERMINALES.hangares_norte()
    Label(ventana_instrucciones_carganorte_complejidad2_frankfurt, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad2_frankfurt, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerosnorte_complejidad2_moscu():
    global ventana_instrucciones_pasajerosnorte_complejidad2_moscu
    ventana_instrucciones_pasajerosnorte_complejidad2_moscu = Toplevel(ventana_tipovuelo_moscu2)
    ventana_instrucciones_pasajerosnorte_complejidad2_moscu.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosnorte_complejidad2_moscu.geometry("500x270")
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_moscu, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_pasajeros_2()  #corregir esto
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_moscu, text=instrucciones1, font=("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosnorte_complejidad2_moscu, text=instrucciones2, font=("Calibri", 11)).pack()
def instrucciones_carganorte_complejidad2_moscu():
    global ventana_instrucciones_carganorte_complejidad2_moscu
    ventana_instrucciones_carganorte_complejidad2_moscu = Toplevel(ventana_tipovuelo_moscu2)
    ventana_instrucciones_carganorte_complejidad2_moscu.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad2_moscu.geometry("700x240")
    Label(ventana_instrucciones_carganorte_complejidad2_moscu, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_carga_2()  #CORREGFIR ESTO
    instrucciones2 = TERMINALES.hangares_norte()
    Label(ventana_instrucciones_carganorte_complejidad2_moscu, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad2_moscu, text=instrucciones2 ,font= ("Calibri", 11)).pack()
def instrucciones_pasajerossur_complejidad2_estambul():
    global ventana_instrucciones_pasajerosur_complejidad2_estambul
    ventana_instrucciones_pasajerosur_complejidad2_estambul = Toplevel(ventana_tipovuelo_estambul2)
    ventana_instrucciones_pasajerosur_complejidad2_estambul.title("ITESO AERONAUTICS")
    ventana_instrucciones_pasajerosur_complejidad2_estambul.geometry("500x270")
    Label(ventana_instrucciones_pasajerosur_complejidad2_estambul, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.norte_pasajeros_2() #corregir esto
    instrucciones2 = TERMINALES.terminal_norte()
    Label(ventana_instrucciones_pasajerosur_complejidad2_estambul, text=instrucciones1, font=("Calibri", 11)).pack()
    Label(ventana_instrucciones_pasajerosur_complejidad2_estambul, text=instrucciones2, font=("Calibri", 11)).pack()
def instrucciones_cargasur_complejidad2_estambul():
    global ventana_instrucciones_carganorte_complejidad2_estambul
    ventana_instrucciones_carganorte_complejidad2_estambul =  Toplevel(ventana_tipovuelo_estambul2)
    ventana_instrucciones_carganorte_complejidad2_estambul.title("ITESO AERONAUTICS")
    ventana_instrucciones_carganorte_complejidad2_estambul.geometry("450x240")
    Label(ventana_instrucciones_carganorte_complejidad2_estambul, text= "Siga las siguientes instrucciones",font=("Calibri", 13), bg= "royalblue3", fg= "white",
          width= "500").pack()
    instrucciones1 = COMPLEJIDAD_2.sur_carga_2()    #corregir esto
    instrucciones2 = TERMINALES.hangares_sur()
    Label(ventana_instrucciones_carganorte_complejidad2_estambul, text=instrucciones1 ,font= ("Calibri", 11)).pack()
    Label(ventana_instrucciones_carganorte_complejidad2_estambul, text=instrucciones2 ,font= ("Calibri", 11)).pack()
#Fin

ventana_inicio()
