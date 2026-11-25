class VistaPanaderia:
    def mostrar_menu(self):
        print("\n--- MENÚ PANADERÍA LA ESPIGA ---")
        print("1. Registrar pan")
        print("2. Mostrar panes")
        print("3. Vender pan")
        print("4. Reservar pan")
        print("5. Ver reservas")
        print("6. Salir")
        return input("Seleccione una opción: ")

    def pedir_datos_pan(self):
        tipo = input("Ingrese el tipo de pan: ")
        precio = input("Ingrese el precio: ")
        unidades = input("Ingrese las unidades: ")
        return tipo, precio, unidades

    def mostrar_lista_panes(self, lista_panes):
        print("\n" + "=" * 58)
        print(f"{'CÓDIGO':<8} {'TIPO':<15} {'PRECIO':<10} {'UNIDADES':<10} {'RESERVADAS':<10}")
        print("-" * 58)
        for pan in lista_panes:
            print(pan)
        print("=" * 58)

    def pedir_datos_venta(self):
        codigo = input("Ingrese el código del pan a vender: ")
        cantidad = input("Ingrese la cantidad a vender: ")
        return codigo, cantidad

    def pedir_datos_reserva(self):
        cliente = input("Ingrese el nombre del cliente: ")
        codigo = input("Ingrese el código del pan a reservar: ")
        cantidad = input("Ingrese la cantidad a reservar: ")
        return cliente, codigo, cantidad

    def mostrar_reservas(self, reservas):
        if not reservas:
            print("\nNo hay reservas registradas.")
            return

        print("\n" + "=" * 64)
        print(f"{'FOLIO':<7} {'CLIENTE':<15} {'PAN':<14} {'CANT.':<7} {'TOTAL':<10}")
        print("-" * 64)
        for r in reservas:
            print(f"{r['folio']:<7} {r['cliente']:<15} {r['tipo_pan']:<14} {r['cantidad']:<7} ${r['total']:<9.2f}")
        print("=" * 64)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)