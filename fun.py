import csv, os, time
pedidos = []
cincoKG = 12500
quinceKG = 22500
def  registrar_pedido ():
    print('----------REGISTRAR PEDIDO----------')
    while True:
        try:
            rut = int(input('Indique su rut (sin punto ni guion): '))
            if len(str(rut)) == 9:
                break
            else:
                print("deber tener 9 caracteres")
        except:
            print('ERROR, DEBEN SER SOLO NUMERO')
    while True:
        nombre = input('Indique su nombre:').capitalize()
        if len(nombre) >= 3:
            break
        else:
            print ('DEBE TENER MAS DE 2 CARACTERES')
    while True:
        direccion = input('Indique direccion: ')
        if len(direccion) >= 5:
            break
        else:
            print ('DEBE TENER MAS DE 4 CARACTERES')
    while True:
        comuna = input('Indique comuna: ')
        if len(comuna) >= 5 and comuna.isalpha:
            break
        else:
            print ('DEBE TENER MAS DE 4 CARACTERES')
    while True:
        try:
            galon = int(input('Ingrese el galon deseado (5 o 15): '))
            if galon in (5,15):
                break
            else:
                print ('Opcion incorecta')
        except:
            print ('Debe ser un numero entero')
    if galon == 5:
        cantidadcinco = ('Ingrese cantidad: ')
        total = cantidadcinco * cincoKG
    print('El total es:',total)
    Cliente = {
        "Rut":rut,
        "Nombre":nombre,
        "Direccion":direccion,
        "Comuna":comuna,
        "Gal.5kg":cantidadcinco,
        "Total":total
    }
    pedidos.append(Cliente)
    print('ENCARGO GUADADO')

    
    
        

def listar_pedidos ():
    if not pedidos:
        print ("Ingrese algun pedido en la opcion 1")
    else:
        for x in pedidos:
            print(f'RUT:{x["Rut"]}')
            print(f'NOMBRE:{x["Nombre"]}')
            print(f'DIRECCION:{x["Direccion"]}')
            print(f'COMUNA:{x["Comuna"]}')
            print(f'GALON 5KG:{x["Gal.5kg"]}')
            print(f'TOTAL:{x["total"]}')
            
            time.sleep(3)

def buscar_rut ():
    if not pedidos:
        print ("Ingrese algun pedido en la opcion 1")
    else:
        rutbuscar = int(input('Buscar pedido por RUT'))
        print ('Ingrese rut: ')
        for x in pedidos:
            if x["Rut"] in rutbuscar:
                print(f'RUT:{x["Rut"]}')
                print(f'NOMBRE:{x["Nombre"]}')
                print(f'DIRECCION:{x["Direccion"]}')
                print(f'COMUNA:{x["Comuna"]}')
                print(f'GALON 5KG:{x["Gal.5kg"]}')
                print(f'TOTAL:{x["total"]}')
                time.sleep(3)
def imprimir ():
    nomArchivo = input('Ingrese nombre para el archivo: ')
    if not nomArchivo:
        print ('el archivo existe')
    else:
        print ('Imprimir hoja de ruta')
        
        with open (nomArchivo+'.csv','a', newline='') as archivo:
            titulo = ('Nombre','Direccion','Comuna')
            escritor = csv.DictWriter(archivo, fieldnames=titulo)
            if archivo.tell()==0:
                escritor.writeheader()
            escritor.writerow(pedidos)
