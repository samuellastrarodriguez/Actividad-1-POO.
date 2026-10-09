class Persona:
    def __init__(self, nombre, apellido, documento, anio_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.anio_nacimiento = anio_nacimiento

    def imprimir_datos(self):
        print(f"Persona: {self.nombre} {self.apellido}")
        print(f"Documento: {self.documento} | Año de nacimiento: {self.anio_nacimiento}\n")

if __name__ == '__main__':
    # Método main
    persona1 = Persona("Juan", "Pérez", "10203040", 1995)
    persona2 = Persona("María", "Gómez", "50607080", 1998)
    
    persona1.imprimir_datos()
    persona2.imprimir_datos()

from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:
    def __init__(self, nombre=None, satelites=0, masa=0.0, volumen=0.0, 
                 diametro=0, distancia_sol=0, tipo=TipoPlaneta.TERRESTRE, observable=False):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol # En millones de km
        self.tipo = tipo
        self.observable = observable

    def imprimir_datos(self):
        print(f"--- Planeta: {self.nombre} ---")
        print(f"Tipo: {self.tipo.value} | Satélites: {self.satelites} | Observable: {self.observable}")
        print(f"Masa: {self.masa} kg | Volumen: {self.volumen} km3 | Distancia al Sol: {self.distancia_sol} M km")

    def calcular_densidad(self):
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    def es_exterior(self):
        
        distancia_en_ua = self.distancia_sol / 149.59787
        return distancia_en_ua > 3.4

if __name__ == '__main__':
    tierra = Planeta("Tierra", 1, 5.972e24, 1.083e12, 12742, 149.6, TipoPlaneta.TERRESTRE, True)
    jupiter = Planeta("Júpiter", 79, 1.898e27, 1.431e15, 139820, 778.5, TipoPlaneta.GASEOSO, True)

    for p in [tierra, jupiter]:
        p.imprimir_datos()
        print(f"Densidad: {p.calcular_densidad():.2f} kg/km3")
        print(f"¿Es exterior?: {'Sí' if p.es_exterior() else 'No'}\n")

class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_auto, puertas, asientos, vel_max, color, automatico):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_auto = tipo_auto
        self.puertas = puertas
        self.asientos = asientos
        self.vel_max = vel_max
        self.color = color
        self.__automatico = automatico  
        self.vel_actual = 0
        
        self.cantidad_multas = 0
        self.valor_total_multas = 0


    def get_automatico(self):
        return self.__automatico

    def set_automatico(self, estado):
        self.__automatico = estado

    def acelerar(self, incremento):
        if self.vel_actual + incremento > self.vel_max:
            print(f"¡ADVERTENCIA! Has superado la velocidad máxima de {self.vel_max} km/h.")
            self.cantidad_multas += 1
            self.valor_total_multas += 50000 
            self.vel_actual = self.vel_max
        else:
            self.vel_actual += incremento

    def desacelerar(self, decremento):
        if self.vel_actual - decremento < 0:
            print("No se puede desacelerar a una velocidad negativa.")
            self.vel_actual = 0
        else:
            self.vel_actual -= decremento

    def frenar(self):
        self.vel_actual = 0

    def calcular_tiempo_llegada(self, distancia_km):
        if self.vel_actual == 0:
            return "El vehículo está detenido."
        return distancia_km / self.vel_actual

    def tiene_multas(self):
        return self.cantidad_multas > 0

    def obtener_total_multas(self):
        return self.valor_total_multas

    def mostrar_velocidad(self):
        print(f"Velocidad actual: {self.vel_actual} km/h")

if __name__ == '__main__':
    auto = Automovil("Toyota", 2023, 2.0, "Gasolina", "SUV", 5, 5, 180, "Rojo", True)
    
    auto.vel_actual = 100
    auto.mostrar_velocidad()
    
    auto.acelerar(20)  
    auto.mostrar_velocidad()
    
    auto.desacelerar(50)  
    auto.mostrar_velocidad()
    
    auto.frenar()  
    auto.mostrar_velocidad()
    
   
    auto.acelerar(200) 
    print(f"¿Tiene multas? {'Sí' if auto.tiene_multas() else 'No'} | Total a pagar: ${auto.obtener_total_multas()}")

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
        
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
        
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_area(self):
        return self.lado ** 2
        
    def calcular_perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return (self.base * self.altura) / 2
        
    def calcular_hipotenusa(self):
        
        return math.sqrt(self.base**2 + self.altura**2)
        
    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()
        
    def determinar_tipo(self):
        hipotenusa = self.calcular_hipotenusa()
        
        
        if self.base == self.altura and self.base == hipotenusa:
            return "Equilátero"
        # Si la base, la altura y la hipotenusa son diferentes entre sí
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            return "Escaleno"
        else:
            return "Isósceles"


if __name__ == '__main__':
     
    mi_circulo = Circulo(2)
    mi_rectangulo = Rectangulo(1, 2)
    mi_cuadrado = Cuadrado(3)
    mi_triangulo = TrianguloRectangulo(3, 5)
    
    # Pruebas del Círculo
    print("--- CÍRCULO ---")
    print(f"Área: {mi_circulo.calcular_area():.2f} cm2")
    print(f"Perímetro: {mi_circulo.calcular_perimetro():.2f} cm\n")
    
    # Pruebas del Rectángulo
    print("--- RECTÁNGULO ---")
    print(f"Área: {mi_rectangulo.calcular_area():.2f} cm2")
    print(f"Perímetro: {mi_rectangulo.calcular_perimetro():.2f} cm\n")
    
    # Pruebas del Cuadrado
    print("--- CUADRADO ---")
    print(f"Área: {mi_cuadrado.calcular_area():.2f} cm2")
    print(f"Perímetro: {mi_cuadrado.calcular_perimetro():.2f} cm\n")
    
    # Pruebas del Triángulo Rectángulo
    print("--- TRIÁNGULO RECTÁNGULO ---")
    print(f"Área: {mi_triangulo.calcular_area():.2f} cm2")
    print(f"Hipotenusa: {mi_triangulo.calcular_hipotenusa():.2f} cm")
    print(f"Perímetro: {mi_triangulo.calcular_perimetro():.2f} cm")
    print(f"Tipo de triángulo: {mi_triangulo.determinar_tipo()}")


class CuentaBancaria:
    def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0 # Saldo inicial en cero

    def imprimir_datos(self):
        print(f"Titular: {self.nombres} {self.apellidos}")
        print(f"Cuenta {self.tipo_cuenta} No. {self.numero_cuenta}")

    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo:,.2f}")
        return self.saldo

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Consignación exitosa. Nuevo saldo: ${self.saldo:,.2f}")
        else:
            print("El valor a consignar debe ser mayor a cero.")

    def retirar(self, valor):
        if valor > self.saldo:
            print("Error: Fondos insuficientes para este retiro.")
        elif valor <= 0:
            print("El valor a retirar debe ser mayor a cero.")
        else:
            self.saldo -= valor
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:,.2f}")

if __name__ == '__main__':
    cuenta = CuentaBancaria("Carlos", "Ramírez", "987654321", "Ahorros")
    cuenta.imprimir_datos()
    cuenta.consignar(150000)
    cuenta.retirar(50000)
    cuenta.retirar(200000)  