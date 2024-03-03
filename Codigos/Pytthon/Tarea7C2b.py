#Definicion de la clase base 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"
    
#Definicion de la clase derivada
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        # Usa la función super() para llamar al __init__ de la clase base
        super().__init__(nombre, edad)
        # Atributo adicional de la clase Estudiante
        self.grado = grado

    # Extensión del método saludar
    def saludar(self):
        # Primero llama al método saludar de la clase base
        saludo_base = super().saludar()
        # Luego agrega información adicional
        return f"{saludo_base} Estoy estudiando {self.grado}."


#crea una instancia de la clase Estudiante
estudiante1 = Estudiante("Carlos", 24, "Electronica")

# llamar el metodo saludar
saludo = estudiante1.saludar()
print(saludo) # imprime "hola, mi nommbre es carlos y tengo 24 años. Estoy estudiando Electronica"