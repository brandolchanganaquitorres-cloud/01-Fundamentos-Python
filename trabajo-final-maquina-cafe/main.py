from menu import mostrar_menu

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            #pedir un cafe
            pass
        elif opcion == "2":
            # ver el historial
            pass
        elif opcion == "3":
            print("\n Muchas gracias por haber tomado nuestros riquísimos cafés")
            break
        else:
            print("Opción inválida, por favor indique una de las opciones sugeridas")

if __name__ == "__main__":
    main()