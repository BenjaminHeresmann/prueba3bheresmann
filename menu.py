import funciones as fn

while True:
    print("MENU Gaxplosive")
    print("1. Registrar pedido")
    print("2. Listar los todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")

    opcion_menu = int(input("Digite opcion del menu: "))

    if opcion_menu == 1:
        fn.registrar_pedido(1,2,3,4,5,6)
    
    elif opcion_menu == 2:
        fn.listar_pedidos()

    elif opcion_menu == 3:
        fn.imprimir_hoja_ruta()

    elif opcion_menu == 4:
        print("Saliendo del programa...")
        break