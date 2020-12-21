class Ventas:
    
    def __init__(self):ventas
        self.v1=short(input("Introduzca su primera venta del dia:"))

        self.v2=short(input("Introduzca su segunda venta del dia:"))

        self.v3=short(input("Introduzca su tercera venta del dia:"))

    
    def equivalente (self):
        total= self.v1 + self.v2 + self.v3
        print("comisison mensual", total)

        comision= total * 2.65
        print("Total del mes:", comision)
