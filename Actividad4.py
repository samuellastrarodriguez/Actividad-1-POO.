
def prueba_excepciones():
    # Primer bloque try
    try:
        print("Ingresando al primer try")
        cociente = 10000 / 0  # Lanza ZeroDivisionError
        print("Después de la división")  # Nunca se ejecuta
    except ZeroDivisionError:
        print("División por cero")
    finally:
        print("Ingresando al primer finally")

    # Segundo bloque try
    try:
        print("Ingresando al segundo try")
        objeto = None
        objeto.to_string()  # Lanza AttributeError (similar a NullPointerException)
        print("Imprimiendo objeto")
    except ZeroDivisionError:
        print("División por cero")
    except Exception:  # Captura excepción general
        print("Ocurrió una excepción")
    finally:
        print("Ingresando al segundo finally")

# Ejecución
prueba_excepciones()
 
class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def imprimir(self):
        print(f"Nombre del vendedor = {self.nombre}")
        print(f"Apellidos del vendedor = {self.apellidos}")
        print(f"Edad del vendedor = {self.edad}")

    def verificar_edad(self, edad):
        if 0 <= edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        elif 18 <= edad <= 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")

if __name__ == "__main__":
    try:
        nombre = input("Nombre del vendedor = ")
        apellidos = input("Apellidos del vendedor = ")
        vendedor = Vendedor(nombre, apellidos)
        
        edad = int(input("Edad del vendedor = "))
        vendedor.verificar_edad(edad)
        vendedor.imprimir()
    except ValueError as e:
        print(f"Excepción: {e}")
 

import math

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor_str):
        try:
            valor = float(valor_str)
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            resultado = math.log(valor)
            print(f"Resultado = {resultado}")
        except ArithmeticError:
            print("El valor debe ser un número positivo para calcular el logaritmo")
        except ValueError:
            print("El valor debe ser numérico para calcular el logaritmo")

    @staticmethod
    def calcular_raiz_cuadrada(valor_str):
        try:
            valor = float(valor_str)
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            resultado = math.sqrt(valor)
            print(f"Resultado = {resultado}")
        except ArithmeticError:
            print("El valor debe ser un número positivo para calcular la raíz cuadrada")
        except ValueError:
            print("El valor debe ser numérico para calcular la raíz cuadrada")

if __name__ == "__main__":
    valor_ingresado = input("Valor numérico = ")
    CalculosNumericos.calcular_logaritmo_neperiano(valor_ingresado)
    CalculosNumericos.calcular_raiz_cuadrada(valor_ingresado)
 
class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []
        self.tamano_equipo = 0
        self.capacidad_maxima = 3

    def esta_lleno(self):
        return self.tamano_equipo == self.capacidad_maxima

    def anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)
        self.tamano_equipo += 1

    @staticmethod
    def validar_campo(campo):
        for char in campo:
            if char.isdigit():
                raise Exception("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")

if __name__ == "__main__":
    try:
        nombre_eq = input("Nombre del equipo = ")
        universidad = input("Universidad = ")
        lenguaje = input("Lenguaje de programación = ")
        
        equipo = EquipoMaratonProgramacion(nombre_eq, universidad, lenguaje)
        
        print("Datos de los integrantes del equipo")
        for i in range(3):
            nombre_prog = input("Nombre del integrante = ")
            EquipoMaratonProgramacion.validar_campo(nombre_prog)
            
            apellidos_prog = input("Apellidos del integrante = ")
            EquipoMaratonProgramacion.validar_campo(apellidos_prog)
            
            programador = Programador(nombre_prog, apellidos_prog)
            equipo.anadir(programador)
    except Exception as e:
        print(f"Excepción: {e}")
 
class LeerArchivo:
    @staticmethod
    def main():
        nombre_archivo = "prueba.txt"  # Ajustar a la ruta deseada
        try:
            # open con 'r' lee texto y gestiona eficientemente el buffer
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    print(linea.strip())
        except IOError:
            print("No se pudo leer el archivo.")

if __name__ == "__main__":
    LeerArchivo.main()
