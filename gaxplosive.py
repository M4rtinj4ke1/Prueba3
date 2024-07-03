from fun import *
import os, time, csv

while True:
    os.system('cls')
    print ('''
    \t-----Gaxplosive-----
    [1] Registrar pedido.
    [2] Listar todos los pedidos.
    [3] Buscar pedido por RUT.
    [4] Imprimir hoja de ruta.
    [5] Salir del programa.''')
    while True:
        try:
            opc = int(input('Ingrese una opcion> '))
            if opc in (1,2,3,4,5):
                    break 
            else:
                print('ERROR, opcion incorrecta')
        except:
            print ('ERROR, debe ser un numero entero')
    os.system('cls')
    if opc == 1:
        registrar_pedido()
    elif opc == 2:
        listar_pedidos ()
    elif opc == 3:
        buscar_rut ()
    elif opc ==4:
        imprimir ()
    else:
        print ('Gracias vuelva pronto')
        break
    time.sleep(3)
