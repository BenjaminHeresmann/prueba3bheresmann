lista_pedidos_centro = []
lista_pedidos_colina = []
lista_pedidos_industrias = []

def registrar_pedido(nombre, direccion, sector, cilindro5, cilindro15, cilindro45):
    while True:
        nombre = input("Ingrese nombre y apellido de cliente: ")
        if nombre == None:
            print("debe ingresar nombre, repita por favor")
        else:
            print("Nombre ingresado")
            break
    while True:
        direccion = input("ingrese direccion: ")
        if direccion == None:
            print("debe ingresar direccion, repita por favor")
        else:
            print("direccion ingresada")
            break
    while True:   
        sector = input("ingrese sector (centro, colina, industrias): ")
        if sector == "centro" or sector == "colina" or sector == "industrias":
            print("sector ingresado")
            break
        else:
            print("debe ingresar sector correcto, repita por favor")
            
    cilindro5 = int(input("digite numero de cilindros de 5 KG: "))
    cilindro15 = int(input("digite numero de cilindros de 15 KG: "))
    cilindro45 = int(input("digite numero de cilindros de 45 KG: "))

    if sector == "centro":
        lista_pedidos_centro.append(["Cliente:", nombre, "Direccion: ", direccion, "Sector: ", sector, "Cil. 5kg: ", cilindro5, "Cil. 15kg: ", cilindro15, "Cil. 45kg: ", cilindro45])
        print(lista_pedidos_centro)
    elif sector == "colina":
        lista_pedidos_colina.append(["Cliente:", nombre, "Direccion: ", direccion, "Sector: ", sector, "Cil. 5kg: ", cilindro5, "Cil. 15kg: ", cilindro15, "Cil. 45kg: ", cilindro45])
        print(lista_pedidos_colina)
    elif sector == "industrias":
        lista_pedidos_industrias.append(["Cliente:", nombre, "Direccion: ", direccion, "Sector: ", sector, "Cil. 5kg: ", cilindro5, "Cil. 15kg: ", cilindro15, "Cil. 45kg: ", cilindro45])
        print(lista_pedidos_industrias)

def listar_pedidos():
    for i in lista_pedidos_centro:
        print(i)
    for i in lista_pedidos_colina:
        print(i)
    for i in lista_pedidos_industrias:
        print(i)


def imprimir_hoja_ruta():
    sector = input("Escriba sector de ruta (Centro, Colina, Industrias): ")
    if sector == "centro":
        with open("ruta_centro.txt", "w") as archivo:
            archivo.write(str(lista_pedidos_centro))
            print("imprimiendo...")

    elif sector == "colina":
        with open("ruta_colina.txt", "w") as archivo:
            archivo.write(str(lista_pedidos_colina))
            print("imprimiendo...")

    elif sector == "industrias":
        with open("ruta_industrias.txt", "w") as archivo:
            archivo.write(str(lista_pedidos_industrias))
            print("imprimiendo...")