class Edades:
    def __init__(self, edadjuan):
        self.edadjuan = edadjuan
        self.edadalberto = 2/3*edadjuan
        self.edadana = 4/3*edadjuan
        self.edadmama = self.edadjuan + self.edadalberto + self.edadana

    def mostrar_edades(self):
        print(f"Edad de Juan: {self.edadjuan}")
        print(f"Edad de Alberto: {self.edadalberto}")
        print(f"Edad de Ana: {self.edadana}")
        print(f"Edad de la mamá: {self.edadmama}")

edad_juan = int(input("Ingrese la edad de Juan: "))

familia = Edades(edad_juan)
familia.mostrar_edades()

class Calculos:
    def __init__(self):
        self.suma = 0
        self.x = 20
        self.y = 40
        self.suma = self.suma + self.x
        self.x = self.x + self.y**2
        self.suma = self.suma + self.x / self.y

    def mostrar_suma(self):
        print(f"EL VALOR DE LA SUMA ES: {self.suma}")



calculo = Calculos()
calculo.mostrar_suma()


class Salario:
    def __init__(self, horas_trabajadas, precio_hora, retencion):
        self.horas_trabajadas = horas_trabajadas
        self.precio_hora = precio_hora
        self.salario_bruto = self.horas_trabajadas * self.precio_hora 
        self.retencion_total = self.salario_bruto * retencion/100
        self.salario_neto = self.salario_bruto - self.retencion_total

    def mostrar_salario(self):
        print(f"Salario bruto: {self.salario_bruto}")
        print(f"Retención total: {self.retencion_total}")
        print(f"Salario neto: {self.salario_neto}")

horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
precio_hora = int(input("Ingrese el precio por hora: "))
retencion = float(input("Ingrese el porcentaje de retención (en decimal): "))

trabajador = Salario(horas_trabajadas, precio_hora, retencion)
trabajador.mostrar_salario()

class Algebra:
    def __init__(self, x):
        self.x = x
        self.cuadrado = self.x**2
        self.cubo = self.x**3
    def mostrar_calculos(self):
        print(f"El cuadrado de {self.x} es: {self.cuadrado}")
        print(f"El cubo de {self.x} es: {self.cubo}")

numero = int(input("Ingrese un número: "))
numero_algebra = Algebra(numero)
numero_algebra.mostrar_calculos()

import math

class Geometria:
    def __init__(self, radio):
        self.radio = radio
        self.area = math.pi * self.radio**2
        self.perimetro = 2 * math.pi * self.radio
    def mostrar_resultados(self):
        print(f"El área del círculo con radio {self.radio} es: {self.area}")
        print(f"El perímetro del círculo con radio {self.radio} es: {self.perimetro}")

radio = float(input("Ingrese el radio del círculo: "))
circunferencia = Geometria(radio)
circunferencia.mostrar_resultados()


