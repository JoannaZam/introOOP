class Persona:
    # Constructor de la clase
    def __init__(self, nombre, edad, genero, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion

    # Metodo para saludar
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")

    # Metodo para indicar la ocupación
    def mostrar_ocupacion(self):
        print(f"Soy {self.ocupacion} de profesión.")

    # Metodo para mostrar la edad
    def mostrar_edad(self):
        print(f"Tengo {self.edad} años.")

    # Metodo para actualizar la ocupación
    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        print(f"Ahora soy {self.ocupacion}.")

    # Metodo para cumpleaños (incrementar la edad)
    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños! Ahora tienes {self.edad} años.")

    # Metodo para pasar saludo
    def saludarA(self, nombreOtraPersona):
        return f"Hola, {self.nombre}, te manda saludar {nombreOtraPersona}!"


# Crear una instancia de la clase Persona
persona1 = Persona("Nathan", 30, "Masculino", "Ingeniero")
persona2 = Persona("Juan", 19, "Masculino", "Estudiante")
persona3 = Persona("Victor", 10, "Masculino", "Docente")
persona4 = Persona("Brenda", 21, "Femenino", "Secretaria")

print(persona1.saludarA(persona2.nombre))

# Llamar a los métodos de la instancia
persona1.saludar()  # Hola, mi nombre es Nathan.
persona1.mostrar_ocupacion()  # Soy Ingeniero de profesión.
persona1.mostrar_edad()  # Tengo 30 años.
persona1.cambiar_ocupacion("Desarrollador de juegos")  # Ahora soy Desarrollador de juegos.
persona1.cumplir_anios()  # ¡Feliz cumpleaños! Ahora tienes 31 años.
