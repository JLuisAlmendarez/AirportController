# MENÚ
import time
from tqdm import tqdm
from TERMINALES import *
from COMPLEJIDAD_1 import *
from COMPLEJIDAD_2 import *
from COMPLEJIDAD_3 import *
from ADMIN import *
path = 'base_aeropuerto.xlsx'
archivo = openpyxl.load_workbook(path)


archivo.active = 2
reportes_finales = archivo.active
cont_us = reportes_finales.cell(row=2, column=1).value
cont_us = cont_us + 1
reportes_finales.cell(row=2, column=1).value = cont_us
archivo.save(path)

# ENCABEZADO DEL MENÚ
def encabezado_menu():
    print("-" * 80)
    print(('|'+' ' * 15)+"SIMULADOR DE MANEJO DE TRÁNSITO AÉREO EN TIERRA"+' ' * 16 + '|')
    print(('|'+' ' * 18)+"Aéroport Charles de Gaulle, Paris, France"+' ' * 19 + '|')
    import time
    print('|'+" " * 28, time.strftime("%d/%m/%y"), "-", time.strftime("%I:%M:%S")+' ' * 30 + '|')
    print("-" * 80)
    print()  # Encabezado principal del programa

# PROCEDENCIA DEL Y TIPO DE VUELO, RETORNA NORTE O SUR Y SI ES DE CARGA O PASAJEROS
def procedencia_y_tipo():
    print()
    archivo.active = 0
    origen = archivo.active
    print('\n' + '-' * 80)
    print('|                  VUELOS DE LLEGADA / INTERNATIONAL ARRIVALS                  |')
    print('-' * 80)
    for t in range(1, 2):
        print('   '+origen.cell(row=t, column=1).value, end='\t\t')
        print('\t'+origen.cell(row=t, column=2).value, end='\t')
        print('\t\t\t'+origen.cell(row=t, column=3).value, end='\t')
        print('\t\t\t'+origen.cell(row=t, column=4).value)
    print('-' * 80)
    for r in range(2, origen.max_row+1):
        for c in range(1, 4):
            print('\t'+origen.cell(row=r, column=c).value, end='  \t\t')
        for c in range(1):
            print(''+time.strftime("%I:%M"))
    print('-' * 80)

    posibilidades = {'JFK': 'N', 'LYC': 'N', 'BCN': 'S', 'FCO': 'S', 'YUL': 'N', 'AMS': 'N', 'DXB': 'S', 'FRA': 'N', 'SVO': 'N', 'IST': 'S'}
    origen = input('INTRODUZCA EL ORIGEN DEL VUELO: ').upper()
    while origen not in posibilidades:
        origen = input('[!] Origen no válido [!] - Teclee el origen correspondiente: ').upper()
        if origen in posibilidades:
            break
    if posibilidades.get(origen) == 'N':
        aterrizaje = 'Norte'
    else:
        aterrizaje = 'Sur'
    print()
    vuelos_origen = {'JFK': 'NUEVA YORK', 'LYC': 'LONDRES', 'BCN': 'BARCELONA', 'FCO': 'ROMA', 'YUL': 'MONTRÉAL', 'AMS': 'ÁMSTERDAM', 'DXB': 'DUBÁI', 'FRA': 'FRÁNKFURT', 'SVO': 'MOSCÚ', 'IST': 'ESTAMBUL'}
    tipo_vuelo = input('EL VUELO PROVENIENTE DE '+vuelos_origen.get(origen)+' ES DE:\n\ta. Carga\n\tb. Pasajeros\nTeclee la letra correspondiente: ')
    while tipo_vuelo != 'a' and tipo_vuelo != 'b':
        tipo_vuelo = input('[!] Tipo de vuelo no válido [!] - Teclee el tipo de vuelo correspondiente: ')
        if tipo_vuelo == 'a' or tipo_vuelo == 'b':
            break
    if tipo_vuelo == 'a':
        tipo_vuelo = 'Carga'
    else:
        tipo_vuelo = 'Pasajeros'
    return aterrizaje, tipo_vuelo

# COMPELJIDAD, RETORNA 1, 2 Ó 3
def complejidad():
    print('\n' + '-' * 80)
    print('|               DENSIDAD DEL TRÁFICO AÉREO / AIR TRAFFIC CONTROL               |')
    print('-' * 80)
    dificultad = input('CONDICIONES DEL AEROPUERTO:\n\t1. Las pistas están prácticamente libres y se toma la ruta más corta.\n\t2. Hay diversas aeronaves en el aeropuerto; se intenta evitar el tráfico.\n\t3. El tráfico aéreo es denso y hay pistas con embotellajes severos.\n\nSeleccione la condición en la que se encuentra el aeropuerto: ')
    if dificultad == '1' or dificultad == '2' or dificultad == '3':
        dificultad = eval(dificultad)
        pass
    else:
        while dificultad != '1' or dificultad != '2' or dificultad != '3':
            dificultad = input('[!] Dificultad no válida [!] - Seleccione la dificultad correspondiente: ')
            if dificultad == '1' or dificultad == '2' or dificultad == '3':
                dificultad = eval(dificultad)
                break
    return dificultad

# CORRE SIMULADOR
def simulador():
    pt = procedencia_y_tipo()
    dif = complejidad()
    print()
    print()

    with tqdm(total=100, ascii=False, colour="green") as barra:
        for num in range(20):
            barra.set_description("Calculando ruta... ")
            barra.update(5)
            time.sleep(0.2)

    print()
    print()

    if pt == ('Norte', 'Pasajeros') and dif == 1:
        norte_pasajeros_1()
    elif pt == ('Norte', 'Carga') and dif == 1:
        norte_carga_1()
    elif pt == ('Sur', 'Pasajeros') and dif == 1:
        sur_pasajeros_1()
    elif pt == ('Sur', 'Carga') and dif == 1:
        sur_carga_1()
    elif pt == ('Norte', 'Pasajeros') and dif == 2:
        print(norte_pasajeros_2())
        terminal_norte()
    elif pt == ('Norte', 'Carga') and dif == 2:
        print(norte_carga_2())
        hangares_norte()
    elif pt == ('Sur', 'Pasajeros') and dif == 2:
        print(sur_pasajeros_2())
        terminal_sur()
    elif pt == ('Sur', 'Carga') and dif == 2:
        print(sur_carga_2())
        hangares_sur()
    elif pt == ('Norte', 'Pasajeros') and dif == 3:
        print(norte_pasajeros_3())
        terminal_norte()
    elif pt == ('Norte', 'Carga') and dif == 3:
        print(norte_carga_3())
        hangares_norte()
    elif pt == ('Sur', 'Pasajeros') and dif == 3:
        print(sur_pasajeros_3())
        terminal_sur()
    elif pt == ('Sur', 'Carga') and dif == 3:
        print(sur_carga_3())
        hangares_sur()

# MENÚ (A) - INSTRUCCIONES PARA EL ATERRIZAJE
def menu_a():
    simulador()
    archivo.active = 2
    reportes_finales = archivo.active
    cont_sim = reportes_finales.cell(row=2, column=3).value
    cont_sim = cont_sim + 1
    reportes_finales.cell(row=2, column=3).value = cont_sim
    archivo.save(path)
    print()
    print()

# MENÚ (B) - INSTRUCCIONES PARA EL DESPEGUE
def menu_b():
    archivo.active = 2
    reportes_finales = archivo.active
    cont_sim = reportes_finales.cell(row=2, column=3).value
    cont_sim = cont_sim + 1
    reportes_finales.cell(row=2, column=3).value = cont_sim
    archivo.save(path)
    print()
    print()

    with tqdm(total=100, ascii=False, colour="green") as barra:
        for num in range(20):
            barra.set_description("Calculando ruta... ")
            barra.update(5)
            time.sleep(0.2)

    print()
    print()

    print("Seguimos trabajando en ello. Gracias por su paciencia. :)")
    print()
    input('[!] Por favor presione "enter" para volver al menú principal [!] ')

    print()
    print()

# MENÚ (C) - INICIAR SESIÓN COMO ADMIN.
def menu_c():
    print()
    print()
    with tqdm(total=100, ascii=False, colour="green") as barra:
        for num in range(20):
            barra.set_description("Conectando con el servidor... ")
            barra.update(5)
            time.sleep(0.2)
    print()

    letra = iniciosecure()

    while letra == 'a':
        motivo_admin = mnforad()
        motivo_admin = int(motivo_admin)
        if motivo_admin == 1:
            mnforadop1()
        elif motivo_admin == 2:
            mnforadop2()
        elif motivo_admin == 3:
            mnforadop3()
        elif motivo_admin == 4:
            mnforadop4()
        elif motivo_admin == 5:
            mnforadop5()
        elif motivo_admin == 6:
            mnforadop6()
            main()
        while motivo_admin < 1 or motivo_admin > 6:
            motivo_admin = mnforad()
            motivo_admin = int(motivo_admin)

    while letra == 'b':
        print('\n\t\t - CONTACTE CON SOPORTE TÉCNICO -')
        break

    print()
    print()

# MENÚ (D) - SALIR
def menu_d():
    from PIL import Image
    i = Image.open('cdg.jfif')
    i.show()

# MENÚ PRINCIPAL
def main():
    encabezado_menu()
    menu = input('MENÚ DE SIMULADOR:\n\ta. Instrucciones para el aterrizaje\n\tb. Instrucciones para el despegue\n\tc. Iniciar sesión como admin.\n\td. Salir\nTeclee la letra correspondiente: ').lower()
    if menu == 'a' or menu == 'b' or menu == 'c' or menu == 'd':
        pass
    else:
        while menu != 'a' or menu != 'b' or menu != 'c' or menu != 'd':
            menu = input('[!] Letra no válida [!] - Teclee la letra correspondiente: ').lower()
            if menu == 'a' or menu == 'b' or menu == 'c' or menu == 'd':
                break
    if menu == 'a':
        menu_a()
        print()
        input('[!] Por favor presione "enter" para volver al menú principal [!] ')
        main()
    elif menu == 'b':
        menu_b()
        while menu == 'b':
            main()
    elif menu == 'c':
        menu_c()
        print()
    elif menu == 'd':
        menu_d()
        print()
        input('[!] Por favor presione "enter" para ingresar al menú principal [!] ')
        main()


if __name__ == "__main__":
    main()
