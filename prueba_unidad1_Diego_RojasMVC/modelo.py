class Pan:
    def __init__(self, codigo, tipo, precio, unidades):
        self.codigo = codigo
        self.tipo = tipo
        self.precio = precio
        self.unidades = unidades
        self.reservadas = 0

    def vender(self, cantidad):
        if cantidad <= 0:
            return False, "Error: la cantidad debe ser mayor a 0."
        elif cantidad > self.unidades:
            return False, f"Error: solo hay {self.unidades} unidades disponibles."
        else:
            self.unidades -= cantidad
            return True, f"Listo. Quedan {self.unidades} unidades."

    def reservar(self, cantidad):
        if cantidad <= 0:
            return False, "Error: la cantidad a reservar debe ser mayor a 0."
        elif cantidad > self.unidades:
            return False, f"Error: solo hay {self.unidades} unidades disponibles para reservar."
        else:
            self.unidades -= cantidad
            self.reservadas += cantidad
            return True, f"Reservadas {cantidad} unidades de {self.tipo}. Quedan {self.unidades} disponibles."

    def __str__(self):
        return f"{self.codigo:<8} {self.tipo:<15} ${self.precio:<9.2f} {self.unidades:<10} {self.reservadas:<10}"


class ListaPanes:
    def __init__(self):
        self.lista = []
        self.reservas = []
        self.cargar_datos()

    def cargar_datos(self):
        self.lista.append(Pan(1, "Enrollado", 0.15, 120))
        self.lista.append(Pan(2, "Integral", 0.25, 60))

    def agregar_pan(self, tipo, precio, unidades):
        nuevo_codigo = len(self.lista) + 1
        nuevo_pan = Pan(nuevo_codigo, tipo, precio, unidades)
        self.lista.append(nuevo_pan)
        return nuevo_codigo

    def buscar_por_codigo(self, codigo):
        for pan in self.lista:
            if pan.codigo == codigo:
                return pan
        return None

    def obtener_todos(self):
        return self.lista

    def registrar_reserva(self, pan, cliente, cantidad):
        ok, mensaje = pan.reservar(cantidad)
        if not ok:
            return False, mensaje

        folio = len(self.reservas) + 1
        total = pan.precio * cantidad
        reserva = {
            "folio": folio,
            "cliente": cliente,
            "codigo_pan": pan.codigo,
            "tipo_pan": pan.tipo,
            "cantidad": cantidad,
            "total": total,
        }
        self.reservas.append(reserva)
        return True, f"Reserva #{folio} confirmada para {cliente}. Total: ${total:.2f}."

    def obtener_reservas(self):
        return self.reservas