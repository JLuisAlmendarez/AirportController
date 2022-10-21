import random

#Pasajeros Sur Complejidad 3
#Llamar unicamente "pasajeros_complejidad3_sur"
def sur_pasajeros_3():
    pistasAterrizaje= "26L"
    print("Aterrice en la pista", pistasAterrizaje, "y reduzca su velocidad a 4 nudos.")
    pistasvtexto()
def pistasvtexto():
    pistasocupacion1= ["V1", "V2", "V3","V4"]
    pistaocupada = random.choice(pistasocupacion1)
    pistalista = ["V1", "V2", "V3","V4"]
    pistaseleccionada = random.choice(pistalista)
    if pistaseleccionada != pistaocupada:
        print("En las taxiways 'V': (la pista", pistaocupada,"está ocupada) díríjase hacia la pista", pistaseleccionada)
        pistasStexto1()
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pistalista)
            if pistaseleccionada !=  pistaocupada:
                print("En las taxiways 'V': (la pista", pistaocupada, "está ocupada) díríjase hacia la pista", pistaseleccionada)
                pistasStexto1()
                break
def pistasStexto1():
    pistasocupacion1= ["S1", "S2", "S3"]
    pistaocupada = random.choice(pistasocupacion1)
    pistalista = ["S1", "S2", "S3"]
    pistaseleccionada = random.choice(pistalista)
    if pistaseleccionada != pistaocupada:
        print("En las taxiways 'S': (la pista", pistaocupada,"está ocupada) díríjase hacia la pista", pistaseleccionada)
        pistas_SW_texto1()
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pistalista)
            if pistaseleccionada !=  pistaocupada:
                print("En las taxiways 'S': (la pista", pistaocupada, "está ocupada) díríjase hacia la pista", pistaseleccionada)
                pistas_SW_texto1()
                break
def pistas_SW_texto1():
    pistasocupacion1= ["S1","S2", "W2", "S3"]
    pistaocupada=random.choice(pistasocupacion1)
    pista_lista= ["S1","S2", "W2", "S3"]
    pistaseleccionada = random.choice(pista_lista)
    if pistaseleccionada != pistaocupada:
        print("En las taxiways 'SW': (la pista", pistaocupada,"está ocupada) díríjase hacia la pista", pistaseleccionada)
        pass
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pista_lista)
            if pistaseleccionada !=  pistaocupada:
                print("En las taxiways 'SW': (la pista", pistaocupada, "está ocupada) díríjase hacia la pista", pistaseleccionada)
                break
    if pistaseleccionada == "S1":
        print("Continúe derecho por S1 hasta la intersección con C; gire a la izquierda en C")
        print("Tome el retorno en UC1, continúe por U y espere frente a UN")
    else:
        tomarN_HaciaUC1_pasajerossur()
def tomarN_HaciaUC1_pasajerossur():
    print("Tome la pista N hasta la intersección con C; gire a la izquierda en C")
    print("Tome el retorno en UC1, continúe por U y espere frente a UN")


#Carga Sur Complejidad 3
#Llamar unicamente "hangares_complejidad3_sur"
def sur_carga_3():
    pistasAterrizaje= "26L"
    print("Aterrice en",pistasAterrizaje, "y reduzca su velocidad a 4 nudos.")
    if pistasAterrizaje == "26L":
        pistasvhangar()
def pistasvhangar():
    pistasocupacion1= ["V1", "V2", "V3","V4"]
    pistaocupada = random.choice(pistasocupacion1)
    pistalista = ["V1", "V2", "V3","V4"]
    pistaseleccionada = random.choice(pistalista)
    if pistaseleccionada != pistaocupada:
        print("En las taxiways 'V': (la pista", pistaocupada,"está ocupada) díríjase hacia la pista", pistaseleccionada)
        pistasShangar()
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pistalista)
            if pistaseleccionada !=  pistaocupada:
                print("En las taxiways 'V': (la pista", pistaocupada, "está ocupada) díríjase hacia la pista", pistaseleccionada)
                pistasShangar()
                break
def pistasShangar():
    pistasocupacion1= ["S1", "S2", "S3"]
    pistaocupada = random.choice(pistasocupacion1)
    pistalista = ["S1", "S2", "S3"]
    pistaseleccionada = random.choice(pistalista)
    if pistaseleccionada != pistaocupada:
        print("En las taxiways 'S': (la pista", pistaocupada,"está ocupada) díríjase hacia la pista", pistaseleccionada)
        pistas_SW_hangar()
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pistalista)
            if pistaseleccionada !=  pistaocupada:
                print("En las taxiways 'S': (la pista", pistaocupada, "está ocupada) díríjase hacia la pista", pistaseleccionada)
                pistas_SW_hangar()
                break
def pistas_SW_hangar():
    pistasocupacion1= ["S1","S2", "W2", "S3"]
    pistaocupada=random.choice(pistasocupacion1)
    pista_lista= ["S1","S2", "W2", "S3"]
    pistaseleccionada = random.choice(pista_lista)
    if pistaseleccionada != pistaocupada:
        print("En las taxiways 'SW': (la pista", pistaocupada,"está ocupada) díríjase hacia la pista", pistaseleccionada)
        pass
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pista_lista)
            if pistaseleccionada != pistaocupada:
                print("En las taxiways 'SW': (la pista", pistaocupada, "está ocupada) díríjase hacia la pista", pistaseleccionada)
                break
    if pistaseleccionada == "S1":
        print("Continúe derecho por S1 hasta la intersección con C; gire a la izquierda en C")
        print("Continúe derecho por la pista C y en la intersección de C con SW1, aguarde indicaciones")
    else:
        tomarN_HaciaUC3_cargasur()
def tomarN_HaciaUC3_cargasur():
    print("Tome la pista N hasta la intersección con C; gire a la izquierda en C")
    print("Continúe derecho por la pista C y en la intersección de C con SW1, aguarde indicaciones")


#Pasajeros Norte Complejidad 3
#Llamar unicamente pasajeros_complejidad_norte
def norte_pasajeros_3():
    pistasAterrizaje= "27R"
    print("Aterrice en",pistasAterrizaje, "y reduzca su velocidad a 4 nudos.")
    if pistasAterrizaje == "27R":
        pistasZ()
def pistasZ():
    pistasocupacion1= ["Z1","Z2", "Z2"]
    pistaocupada=random.choice(pistasocupacion1)
    pista_lista= ["Z1","Z2", "Z3"]
    pistaseleccionada = random.choice(pista_lista)
    if pistaseleccionada != pistaocupada:
        print("En las taxiways 'Z': (la pista", pistaocupada,"está ocupada) díríjase hacia la pista", pistaseleccionada)
        pistasK()
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pista_lista)
            if pistaseleccionada !=  pistaocupada:
                print("En las taxiways 'Z': (la pista", pistaocupada, "está ocupada) díríjase hacia la pista", pistaseleccionada)
                pistasK()
                break
def pistasK():
    pistasocupacion1= ["K1","K2", "K3"]
    pistaocupada=random.choice(pistasocupacion1)
    pista_lista= ["K1","K2", "K3"]
    pistaseleccionada = random.choice(pista_lista)
    if pistaseleccionada != pistaocupada:
        print("En las taxiways 'K': (la pista", pistaocupada,"está ocupada) díríjase hacia la pista", pistaseleccionada)
        pistasKD()
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pista_lista)
            if pistaseleccionada !=  pistaocupada:
                print("En las taxiways 'K': (la pista", pistaocupada, "está ocupada) díríjase hacia la pista", pistaseleccionada)
                pistasKD()
                break
def pistasKD():
    pistasocupacion1= ["K1","K2", "K3"]
    pistaocupada=random.choice(pistasocupacion1)
    pista_lista= ["K1","K2", "K3"]
    pistaseleccionada = random.choice(pista_lista)
    if pistaseleccionada != pistaocupada:
        print("La taxiway", pistaocupada," está ocupada; cruce la pista 09R y continue por la pista", pistaseleccionada, "hasta llegar a D")
        doblarD_Rotonda_esperar()
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pista_lista)
            if pistaseleccionada !=  pistaocupada:
                print("La taxiway", pistaocupada, " está ocupada; cruce la pista 09R y continue por la pista",pistaseleccionada, "hasta llegar a D")
                doblarD_Rotonda_esperar()
                break
def doblarD_Rotonda_esperar():
    print("Doble a la izquierda y continúe por la pista D hasta llegar a la rotonda")
    print("Tome la rotonda y continúe girando hasta posicionarse frente a BD11; aguarde indicaciones")


#Carga norte Complejidad 3
#Llamar unicamente "hangares_complejidad3_norte"
def norte_carga_3():
    pistasAterrizaje= "27R"
    print("Aterrice en",pistasAterrizaje)
    if pistasAterrizaje == "27R":
        pistasZhangar()
def pistasZhangar():
    pistasocupacion1= ["Z1","Z2", "Z2"]
    pistaocupada=random.choice(pistasocupacion1)
    pista_lista= ["Z1","Z2", "Z3"]
    pistaseleccionada = random.choice(pista_lista)
    if pistaseleccionada != pistaocupada:
        print("En las taxiways 'Z': (la pista", pistaocupada,"está ocupada) díríjase hacia la pista", pistaseleccionada)
        pistashangarK()
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pista_lista)
            if pistaseleccionada != pistaocupada:
                print("En las taxiways 'Z': (la pista", pistaocupada, "está ocupada) díríjase hacia la pista", pistaseleccionada)
                pistashangarK()
                break
def pistashangarK():
    pistasocupacion1= ["K1","K2", "K3"]
    pistaocupada=random.choice(pistasocupacion1)
    pista_lista= ["K1","K2", "K3"]
    pistaseleccionada = random.choice(pista_lista)
    if pistaseleccionada != pistaocupada:
        print("En las taxiways 'K': (la pista", pistaocupada,"está ocupada) díríjase hacia la pista", pistaseleccionada)
        pistasY()
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pista_lista)
            if pistaseleccionada !=  pistaocupada:
                print("En las taxiways 'K': (la pista", pistaocupada, "está ocupada) díríjase hacia la pista", pistaseleccionada)
                pistasY()
                break
def pistasY():
    pistasocupacion1= ["Y1","Y2A", "Y2"]
    pistaocupada=random.choice(pistasocupacion1)
    pista_lista= ["Y1","Y2A", "Y2"]
    pistaseleccionada = random.choice(pista_lista)
    if pistaseleccionada != pistaocupada:
        print("La taxiway", pistaocupada," está ocupada; cruce la pista 09R y continúe por la pista", pistaseleccionada, "y aguarde indicaciones")
    else:
        while pistaseleccionada == pistaocupada:
            pistaseleccionada = random.choice(pista_lista)
            if pistaseleccionada !=  pistaocupada:
                print("La taxiway", pistaocupada, " está ocupada; cruce la pista 09R y continúe por la pista", pistaseleccionada, "y aguarde indicaciones")
                break
    print("Continúe derecho por la pista BD hasta llegar a la pista M")
    print("En la pista M, gire a su derecha; en breve recibirá indicaciones")
