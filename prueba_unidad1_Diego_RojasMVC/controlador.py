from modelo import ListaPanes
from vista import VistaPanaderia


class ControladorPanaderia:
    def __init__(self):
        self.modelo = ListaPanes()
        self.vista = VistaPanaderia()

    def registrar_pan(self):
        tipo, precio_txt, unidades_txt = self.vista.pedir_datos_pan()

        if tipo.strip() == "":
            self.vista.mostrar_mensaje("Error: el tipo de pan no puede estar vacío.")
            return

        try:
            precio = float(precio_txt)
            unidades = int(unidades_txt)
        except ValueError:
            self.vista.mostrar_mensaje("Error: el precio y las unidades deben ser valores numéricos.")
            return

        if precio <= 0 or unidades < 0:
            self.vista.mostrar_mensaje("Error: el precio debe ser mayor a 0 y las unidades no pueden ser negativas.")
            return

        nuevo_codigo = self.modelo.agregar_pan(tipo.strip(), precio, unidades)
        self.vista.mostrar_mensaje(f"Registrado con el código {nuevo_codigo}.")

    def mostrar_panes(self):
        panes = self.modelo.obtener_todos()
        self.vista.mostrar_lista_panes(panes)

    def vender_pan(self):
        codigo_txt, cantidad_txt = self.vista.pedir_datos_venta()

        try:
            codigo = int(codigo_txt)
            cantidad = int(cantidad_txt)
        except ValueError:
            self.vista.mostrar_mensaje("Error: el código y la cantidad deben ser números enteros.")
            return

        pan_encontrado = self.modelo.buscar_por_codigo(codigo)

        if pan_encontrado is None:
            self.vista.mostrar_mensaje("Error: no existe ese código.")
        else:
            ok, mensaje = pan_encontrado.vender(cantidad)
            self.vista.mostrar_mensaje(mensaje)

    def reservar_pan(self):
        cliente, codigo_txt, cantidad_txt = self.vista.pedir_datos_reserva()

        if cliente.strip() == "":
            self.vista.mostrar_mensaje("Error: el nombre del cliente no puede estar vacío.")
            return

        try:
            codigo = int(codigo_txt)
            cantidad = int(cantidad_txt)
        except ValueError:
            self.vista.mostrar_mensaje("Error: el código y la cantidad deben ser números enteros.")
            return

        pan_encontrado = self.modelo.buscar_por_codigo(codigo)

        if pan_encontrado is None:
            self.vista.mostrar_mensaje("Error: no existe ese código.")
            return

        _, mensaje = self.modelo.registrar_reserva(pan_encontrado, cliente.strip(), cantidad)
        self.vista.mostrar_mensaje(mensaje)

    def ver_reservas(self):
        reservas = self.modelo.obtener_reservas()
        self.vista.mostrar_reservas(reservas)

    def ejecutor(self):
        opcion = ""
        while opcion != "6":
            opcion = self.vista.mostrar_menu().strip()

            if opcion == "1":
                self.registrar_pan()
            elif opcion == "2":
                self.mostrar_panes()
            elif opcion == "3":
                self.vender_pan()
            elif opcion == "4":
                self.reservar_pan()
            elif opcion == "5":
                self.ver_reservas()
            elif opcion == "6":
                self.vista.mostrar_mensaje("Saliendo del sistema...")
            else:
                self.vista.mostrar_mensaje("Opción no válida.")


if __name__ == "__main__":
    app = ControladorPanaderia()
    app.ejecutor()