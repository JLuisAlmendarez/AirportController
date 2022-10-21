# TERMINALES/HANGARES
import random

def terminal_norte():  # DEJA EL AVIÓN EN LA PISTA B JUSTO DONDE SE ENCUENTRA LA ROTONDA
    pista_terminal = "TOME LA PISTA A Y CONTINÚE A UNA VELOCIDAD DE 4 NUDOS"
    puertas_terminal = ["S1", "S2", "Z", "Y", "X", "W", "V", "U", "T"]
    puerta = random.choice(puertas_terminal)

    if puerta == "S1":
        puerta = "S"
        numero = random.randint(6, 22)
        pista_final = "DESPUÉS DE PASAR LA RUTA 13, TOME LA PISTA LATERAL SOBRE A AGUARDE INDICACIONES"
    elif puerta == "Z":
        numero = random.randint(1, 9)
        if numero <= 3:
            pista_final = "TOME LA RUTA 13"
        elif numero <= 5:
            pista_final = "TOME LA RUTA 14"
        else:
            pista_final = "TOME LA RUTA 15B HACIA 16 Y CONTINÚE POR A HASTA EL EDIFICIO Z"
    elif puerta == "S2":
        puerta = "S"
        numero = random.randint(23, 31)
        pista_final = "SIGA POR A HASTA CRUZAR LA TERMINAL RUMBO A LA PISTA NA"
    else:
        numero = random.randint(1, 8)
        pista_final = "TOME LA RUTA 15B HACIA 16 Y CONTINÚE POR A HASTA EL EDIFICIO " + puerta

    instr_fin = "ESPERE A SER REMOLCADO HASTA LA PUERTA " + puerta + str(numero)
    print(pista_terminal)
    print(pista_final)
    print(instr_fin)


def hangares_norte():  # DEJA EL AVIÓN EN LA INTERSECCIÓN DE BD CON LA PISTA M
    complejo_hangares = [1, 2, 3, 4, 5]
    complejo = random.choice(complejo_hangares)

    if complejo == 1:
        hangar_numero = random.randint(1, 8)
        salida = ""
        if hangar_numero == 1:
            salida = "EN40"
        elif hangar_numero == 2:
            salida = "EN50"
        elif hangar_numero == 3:
            salida = "EN51"
        elif hangar_numero == 4:
            salida = "EN41"
        elif hangar_numero == 5:
            salida = "EN52"
        elif hangar_numero == 6:
            salida = "EN42"
        elif hangar_numero == 7:
            salida = "EN55"
        elif hangar_numero == 8:
            salida = "EN43"
        print("GIRE A LA IZQUIERDA EN EN22 HACIA EM3 RUMBO; ESTARÁ ENTRANDO AL PRIMER COMPLEJO DE HANGARES; CONTINÚE POR LA PISTA")
        print("SIGA DERECHO HASTA EL HANGAR NÚMERO " + str(hangar_numero) + " CON SALIDA EN " + str(salida))

    elif complejo == 2:
        hangar_numero = random.randint(1, 5)
        print("GIRE A LA DERECHA EN EN" + str(20+hangar_numero) + " RUMBO AL SEGUNDO COMPLEJO DE HANGARES Y CONTINÚE DERECHO")

    elif complejo == 3:
        hangar_numero = random.randint(1, 15)
        print("EN LA INTERSECCIÓN, GIRE POR LA IZQUIERDA HACIA EM2 RUMBO AL TERCER COMPLEJO DE HANGARES, Y AGUARDE INDICACIONES")
        salida = ""
        if hangar_numero != 2:
            if hangar_numero == 1:
                salida = "I20"
            elif hangar_numero == 3:
                salida = "I21"
            elif hangar_numero == 4:
                salida = "I22"
            elif hangar_numero == 5:
                salida = "I23"
            elif hangar_numero == 6:
                salida = "I24"
            elif hangar_numero == 7:
                salida = "I14"
            elif hangar_numero == 8:
                salida = "I25"
            elif hangar_numero == 9:
                salida = "I15"
            elif hangar_numero == 10:
                salida = "I16"
            elif hangar_numero == 11:
                salida = "I26"
            elif hangar_numero == 12:
                salida = "I27"
            elif hangar_numero == 13:
                salida = "I17"
            elif hangar_numero == 14:
                salida = "I18"
            elif hangar_numero == 15:
                salida = "I19"
            print("CONTINÚE POR EM2 EN DIRECCIÓN AL HANGAR " + str(hangar_numero) + " CON SALIDA EN " + salida)
        else:
            esp_aparcamiento = random.choice(["I04", "I09", "I05", "I10", "I07", "I06", "I11", "I12"])
            print("TOME EM23 A SU IZQUIERDA, ENTRANDO AL HANGAR NÚMERO 2")
            print("CONTINÚE DERECHO HASTA EL ESPACIO DE APARCAMIENTO NÚMERO " + esp_aparcamiento)

    elif complejo == 4:
        print("EN LA INTERSECCIÓN, CONTINÚE DERECHO POR M RUMBO AL CUARTO COMPLEJO DE HANGARES")
        hangar_numero = random.randint(1, 16)
        dict_posibilidades = {1: "I40", 2: "I41", 3: "I42", 4: "I43", 5: "I44", 6: "I45", 7: "I46", 8: "I47", 9: "I48", 10: "I49", 11: "I50", 12: "I51", 13: "I52", 14: "I53", 15: "I54", 16: "I55"}
        if hangar_numero > 11:
            print("TOME LA RUTA EM1 Y CONTINÚE")
        print("GIRE A LA IZQUIERDA HACIA EL HANGAR " + str(hangar_numero) + " CON SALIDA EN " + dict_posibilidades.get(hangar_numero))

    elif complejo == 5:
        print("EN LA INTERSECCIÓN, CONTINÚE DERECHO POR M RUMBO AL QUINTO COMPLEJO DE HANGARES")
        hangar_numero = random.randint(1, 5)
        print("GIRE A LA DERECHA EN I" + str(29+hangar_numero) + " Y CONTINÚE DERECHO")

    else:
        print("EN LA INTERSECCIÓN, CONTINÚE DERECHO POR M")
        print("DESPUÉS DE PASAR I49, GIRE POR LA DERECHA HACIA BM1 RUMBO AL SEXTO COMPLEJO DE HANGARES")
        hangar_numero = random.randint(1, 10)
        dict_posibilidades = {1: "I88", 2: "I89", 3: "I87", 4: "I80", 5: "I86", 6: "I81", 7: "I85", 8: "I82", 9: "I84", 10: "I83"}
        print("CONTINÚE DERECHO Y GIRE EN LA SALIDA " + dict_posibilidades.get(hangar_numero) + " RUMBO AL HANGAR NÚMERO " + str(hangar_numero))

    print("LO ESTARÁN ESPERANDO PARA SER REMOLCADO")


def terminal_sur():  # DEJEN EL AVIÓN EN LA INTERSECCIÓN DE LA PISTA U CON UN
    print("SIGA POR LA PISTA U Y TOME LA PISTA UN PARA CONECTAR CON LA PISTA N Y ATIENDA")
    print("CONTINÚE DERECHO POR N HASTA LA INTERSECCIÓN CON FN2 Y AGUARDE INDICACIONES")
    terminal_2 = ["A", "B", "C", "D", "E", "F", "TK1", "TK2", "TK3", "TK4", "TL1", "TL2", "G"]
    sub_terminal = random.choice(terminal_2)

    if sub_terminal == "TK1" or sub_terminal == "TK2" or sub_terminal == "TK3" or sub_terminal == "TK4" or sub_terminal == "TL1" or sub_terminal == "TL2":
        if sub_terminal == "TK1" or sub_terminal == "TK2" or sub_terminal == "TK3" or sub_terminal == "TK4":
            correccion = "K"
        else:
            correccion = "L"
        print("HA SIDO ASIGNADO A LA TERMINAL 2"+correccion)
    else:
        print("HA SIDO ASIGNADO A LA TERMINAL 2"+sub_terminal)

    if sub_terminal == "A" or sub_terminal == "C" or sub_terminal == "E" or sub_terminal == "TK3" or sub_terminal == "TK4" or sub_terminal == "G":
        camino = "abajo"
    else:
        camino = "arriba"

    if camino == "abajo":
        print("TOME FN2 PARA RETORNARSE Y BAJE POR F HASTA U")
        print("GIRE A LA IZQUIERDA EN LA PISTA U RUMBO A LA PISTA F")
        print("CONTINÚE SOBRE F HASTA LA PISTA R Y CONTINÚE DERECHO")
        print("AL LLEGAR A LA INTERSECCIÓN CON RT2, CONTINÚE DERECHO")

        if sub_terminal == "A":
            print("AL LLEGAR A LA INTERSECCIÓN CON RP1, GIRE A LA IZQUIERDA Y ESPERE")
            lista_puertas = [*range(1, 11), 12, 14, 16, 18, 30, 32, 34, 36, 38]
            puerta = random.choice(lista_puertas)
            print("ESTÁ ENTRANDO A TERMINAL "+sub_terminal)
            print("GIRE A LA IZQUIERDA Y CONTINÚE DERECHO RUMBO A LA PUERTA "+sub_terminal+str(puerta))

        elif sub_terminal == "C":
            print("AL LLEGAR A LA INTERSECCIÓN CON RT3, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RP2, GIRE A LA IZQUIERDA Y ESPERE")
            lista_puertas = [*range(2, 11), 12, 14]
            puerta = random.choice(lista_puertas)
            print("ESTÁ ENTRANDO A TERMINAL "+sub_terminal)
            if puerta == 10 or puerta == 12 or puerta == 14:
                print("GIRE A LA DERECHA Y CONTINÚE DERECHO RUMBO A LA PUERTA "+sub_terminal+str(puerta))
            else:
                print("GIRE A LA IZQUIERDA Y CONTINÚE DERECHO RUMBO A LA PUERTA "+sub_terminal+str(puerta))

        elif sub_terminal == "E":
            print("AL LLEGAR A LA INTERSECCIÓN CON RT3, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT4, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RP3, GIRE A LA IZQUIERDA Y ESPERE")
            lista_puertas = [*range(10, 45, 2)]
            puerta = random.choice(lista_puertas)
            print("ESTÁ ENTRANDO A TERMINAL "+sub_terminal)
            print("GIRE A LA DERECHA Y CONTINÚE DERECHO RUMBO A LA PUERTA "+sub_terminal+str(puerta))

        elif sub_terminal == "TK3":
            print("AL LLEGAR A LA INTERSECCIÓN CON RT3, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT4, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT5, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RP6, GIRE A LA IZQUIERDA Y ESPERE")
            lista_puertas = [53, 59, 65, 71]
            puerta = random.choice(lista_puertas)
            print("ESTÁ ENTRANDO A TERMINAL K")
            print("CONTINÚE DERECHO RUMBO A LA PUERTA K"+str(puerta))

        elif sub_terminal == "TK4":
            print("AL LLEGAR A LA INTERSECCIÓN CON RT3, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT4, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT5, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT6, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RP7, GIRE A LA IZQUIERDA Y ESPERE")
            lista_puertas = [52, 58, 64, 70, 76]
            puerta = random.choice(lista_puertas)
            print("ESTÁ ENTRANDO A TERMINAL K")
            print("CONTINÚE DERECHO RUMBO A LA PUERTA K"+str(puerta))

        elif sub_terminal == "TL2":
            print("AL LLEGAR A LA INTERSECCIÓN CON RT3, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT4, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT5, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT6, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT6, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT7, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT9, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RP15, GIRE A LA IZQUIERDA Y ESPERE")
            lista_puertas = [53, 59, 65, 71]
            puerta = random.choice(lista_puertas)
            print("ESTÁ ENTRANDO A TERMINAL L")
            print("CONTINÚE DERECHO RUMBO A LA PUERTA L"+str(puerta))

        else:
            print("AL LLEGAR A LA INTERSECCIÓN CON RT3, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT4, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT5, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT6, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT6, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT7, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT9, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT15, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RT16, CONTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON RP17, GIRE A LA IZQUIERDA Y ESPERE")
            print("CONTINÚE POR RP17, CRUZANDO LA PISTA P1 Y ESPERE")
            print("CONTINÚE POR RP17, CRUZANDO LA PISTA P3 Y ESPERE")
            print("CONTINÚE POR RP17 HASTA LA PISTA P5, GIRE A LA DERECHA Y AGUARDE")
            print("ESTÁ ENTRANDO A TERMINAL G")
            lista_puertas = [*range(1, 7), *range(10, 15), 16, 18, 20, 21, 30, 31, 33, 34, 37, 38, 39, 40, 41]
            puerta = random.choice(lista_puertas)
            if puerta == 1 or puerta == 2 or puerta == 3:
                print("CONTINÚE DERECHO RUMBO A LA PUERTA J"+str(puerta))
            elif puerta == 4 or puerta == 5 or puerta == 6 or puerta == 10 or puerta == 11 or puerta == 12:
                print("AL LLEGAR A LA INTERSECCIÓN CON E10, GIRE A LA IZQUIERDA Y ESPERE INDICACIONES")
                print("CONTINÚE DERECHO RUMBO A LA PUERTA J"+str(puerta))
            elif puerta == 13 or puerta == 14 or puerta == 16:
                print("AL LLEGAR A LA INTERSECCIÓN CON E10, CONTINÚE DERECHO RUMBO A LA PUERTA J"+str(puerta))
            elif puerta == 18 or puerta == 20 or puerta == 21 or puerta == 30 or puerta == 31 or puerta == 33:
                print("AL LLEGAR A LA INTERSECCIÓN CON E10, CONTINÚE DERECHO")
                print("AL LLEGAR A LA INTERSECCIÓN CON E11, GIRE A LA IZQUIERDA Y ESPERE INDICACIONES")
                print("CONTINÚE DERECHO RUMBO A LA PUERTA J"+str(puerta))
            elif puerta == 34 or puerta == 37:
                print("AL LLEGAR A LA INTERSECCIÓN CON E10, CONTINÚE DERECHO")
                print("AL LLEGAR A LA INTERSECCIÓN CON E11, CONTINÚE DERECHO RUMBO A LA PUERTA J"+str(puerta))
            else:
                print("AL LLEGAR A LA INTERSECCIÓN CON E10, CONTINÚE DERECHO")
                print("AL LLEGAR A LA INTERSECCIÓN CON E11, CONTINÚE DERECHO")
                print("AL LLEGAR A LA INTERSECCIÓN CON E12, GIRE A LA IZQUIERDA Y ESPERE INDICACIONES")
                print("CONTINÚE DERECHO RUMBO A LA PUERTA J"+str(puerta))

    else:
        print("CONTINÚE DERECHO POR N HASTA LA INTERSECCIÓN CON G Y AGUARDE INDICACIONES")
        print("CONTINÚE DERECHO POR N HASTA SU INTERSECCIÓN CON E Y ESPERE")
        print("TOME LA PISTA E A SU DERECHA Y CONTINÚE DERECHO")

        if sub_terminal == "B":
            print("AL LLEGAR A LA INTERSECCIÓN CON GE1, GIRE A LA DERECHA Y ATIENDA")
            lista_puertas = [*range(1, 15), 16, 18, 20]
            puerta = random.choice(lista_puertas)
            print("ESTÁ ENTRANDO A TERMINAL "+sub_terminal)
            print("GIRE A LA DERECHA Y CONTINÚE DERECHO RUMBO A LA PUERTA "+sub_terminal+str(puerta))

        elif sub_terminal == "D":
            print("AL LLEGAR A LA INTERSECCIÓN CON GE1, COMTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON GE2, GIRE A LA DERECHA Y ATIENDA")
            lista_puertas = [*range(2, 21), 22, 24]
            puerta = random.choice(lista_puertas)
            print("ESTÁ ENTRANDO A TERMINAL "+sub_terminal)
            print("GIRE A LA DERECHA Y CONTINÚE DERECHO RUMBO A LA PUERTA "+sub_terminal+str(puerta))

        elif sub_terminal == "F":
            print("AL LLEGAR A LA INTERSECCIÓN CON GE1, COMTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON GE2, COMTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON GE3, GIRE A LA DERECHA Y ATIENDA")
            lista_puertas = [*range(2, 35, 2), *range(66, 97, 2), *range(1, 18, 2)]
            puerta = random.choice(lista_puertas)
            print("ESTÁ ENTRANDO A TERMINAL "+sub_terminal)
            if puerta == 2 or puerta == 4 or puerta == 6 or puerta == 8 or puerta == 10 or puerta == 12 or puerta == 14 or puerta == 16 or puerta == 18 or 19 < puerta < 35:
                print("CONTINÚE DERECHO RUMBO A LA PUERTA "+sub_terminal+str(puerta))
            elif 15 < puerta < 23:
                print("AL LLEGAR A LA INTERSECCIÓN CON G4, GIRE A LA IZQUIERDA")
                print("CONTINÚE DERECHO RUMBO A LA PUERTA "+sub_terminal+str(puerta))
            elif 23 < puerta < 34 or 66 < puerta < 71:
                print("AL LLEGAR A LA INTERSECCIÓN CON G4, GIRE A LA IZQUIERDA")
                print("AL LLEGAR RUMBO A LA PUERTA F26, GIRE A LA DERECHA")
                print("CONTINÚE DERECHO RUMBO A LA PUERTA "+sub_terminal+str(puerta))
            elif 71 < puerta < 85:
                print("AL LLEGAR A LA INTERSECCIÓN CON G4, GIRE A LA IZQUIERDA")
                print("AL LLEGAR RUMBO A LA PUERTA F26, CONTINÚE DERECHO RUMBO A LA PUERTA "+sub_terminal+str(puerta))
            else:
                print("AL LLEGAR A LA INTERSECCIÓN CON G4, GIRE A LA IZQUIERDA")
                print("AL LLEGAR RUMBO A LA PUERTA F26, CONTINÚE DERECHO")
                print("AL LLEGAR RUMBO A LA PUERTA F84, AGUARDE INDICACIONES FRENTE A TF4")
                print("GIRE A LA DERECHA, TOMANDO TF4 Y AGUARDE INDICACIONES FRENTE A TF5")
                print("CONTINÚE DERECHO RUMBO A LA PUERTA "+sub_terminal+str(puerta))

        else:
            print("AL LLEGAR A LA INTERSECCIÓN CON GE1, COMTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON GE2, COMTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON GE3, COMTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON GE4, COMTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON GE5, COMTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON GE6, COMTINÚE DERECHO")
            print("AL LLEGAR A LA INTERSECCIÓN CON GE9, GIRE A LA DERECHA Y ATIENDA")
            print("CONTINÚE HASTA POR LA PISTA E5 HASTA LA BIFURCACIÓN DEL CAMINO Y ESPERE INDICACIONES")
            if sub_terminal == "TK1":
                print("CONTINÚE DERECHO POR E5 Y AGUARDE FRENTE A TK1")
                lista_puertas = [2, 5, 9, 13, 17, 21]
                puerta = random.choice(lista_puertas)
                print("ESTÁ ENTRANDO A TERMINAL K")
                print("CONTINÚE DERECHO RUMBO A LA PUERTA K"+str(puerta))
            else:
                print("GIRE POR IZQUIERDA SOBRE E5")
                if sub_terminal == "TK2":
                    print("DONDE EL CAMINO SE BIFURCA, TOME E6 A SU DERECHA Y AGUARDE FRENTE A TK2")
                    lista_puertas = [26, 32, 38, 44]
                    puerta = random.choice(lista_puertas)
                    print("ESTÁ ENTRANDO A TERMINAL K")
                    print("CONTINÚE DERECHO RUMBO A LA PUERTA K"+str(puerta))
                else:
                    print("DONDE EL CAMINO SE BIFURCA, CONTINÚE DERECHO SOBRE E5")
                    print("CONTINÚE DERECHO HASTA E7 Y AGUARDE EN LA BIFURCACIÓN")
                    print("TOME LA PISTA E7 POR DERECHA Y AGUARDE FRENTE A TL1")
                    lista_puertas = [27, 33, 39]
                    puerta = random.choice(lista_puertas)
                    print("ESTÁ ENTRANDO A TERMINAL L")
                    print("CONTINÚE DERECHO RUMBO A LA PUERTA L"+str(puerta))

    print("LO ESTARÁN ESPERANDO PARA SER REMOLCADO")


def hangares_sur():  # DEJEN EL AVIÓN EN LA PISTA C ADELANTE DEL CRUCE DE C CON WA (APARECE COMO UT1 EN MAPS)
    hangares = ["M", "N", "P"]
    hangar = random.choice(hangares)
    print("CONTINÚE DERECHO POR LA PISTA C HASTA UC5 Y AGUARDE INDICACIONES")

    if hangar == "M":
        print("EN LA BIFURCACIÓN DEL CAMINO, GIRE POR DERECHA Y ATIENDA")
        hangares_m = [*range(6, 19)]
        numero = random.choice(hangares_m)
        if 15 < numero < 19:
            print("GIRE A LA IZQUIERDA Y COTNINÚE DERECHO RUMBO A LA PUERTA "+hangar+str(numero))
        else:
            print("GIRE A LA DERECHA Y COTNINÚE DERECHO RUMBO A LA PUERTA "+hangar+str(numero))

    else:
        print("EN LA BIFURCACIÓN DEL CAMINO, GIRE POR IZQUIERDA Y ATIENDA")
        print("CONTINÚE DERECHO POR LA PISTA C HASTA UC6 Y AGUARDE INDICACIONES")
        if hangar == "N":
            print("EN LA BIFURCACIÓN DEL CAMINO, GIRE POR IZQUIERDA Y ATIENDA")
            hangares_n = [*range(1, 12)]
            numero = random.choice(hangares_n)
            if numero < 3:
                print("GIRE A LA DERECHA Y COTNINÚE DERECHO RUMBO A LA PUERTA "+hangar+str(numero))
            else:
                print("GIRE A LA IZQUIERDA Y COTNINÚE DERECHO RUMBO A LA PUERTA "+hangar+str(numero))
        else:
            print("EN LA BIFURCACIÓN DEL CAMINO, GIRE POR DERECHA HASTA LA PISTA C2 Y ATIENDA")
            hangares_p = [*range(70, 77), *range(80, 92)]
            numero = random.choice(hangares_p)
            if 79 < numero < 90:
                print("GIRE A LA IZQUIERDA Y COTNINÚE DERECHO RUMBO A LA PUERTA "+hangar+str(numero))
            else:
                print("COTNINÚE DERECHO POR LA PISTA C1 RUMBO A LA PUERTA "+hangar+str(numero))

    print("LO ESTARÁN ESPERANDO PARA SER REMOLCADO")
