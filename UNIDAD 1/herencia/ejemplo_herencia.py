"""
Ejemplo de HERENCIA en POO.

Idea principal:
    Crear una clase base (Persona) con atributos y métodos
    comunes, y a partir de ella definir clases hijas (Estudiante
    y Profesor) que reutilizan y amplían ese comportamiento.

En este archivo nos enfocamos en la HERENCIA:
    - Las clases hijas heredan nombre y edad.
    - Cada una agrega su propia información.
"""


class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self) -> str:
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."


class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, carrera: str):
        # Reutilizamos el constructor de Persona (HERENCIA)
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentarse(self) -> str:
        base = super().presentarse()
        return f"{base} Soy estudiante de {self.carrera}."


class Profesor(Persona):
    def __init__(self, nombre: str, edad: int, asignatura: str):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def presentarse(self) -> str:
        base = super().presentarse()
        return f"{base} Soy profesor de {self.asignatura}."


if __name__ == "__main__":
    estudiante = Estudiante("Guido", 20, "Tecnologías de la Información")
    profesor = Profesor("Ing. Nogales", 35, "Programación Orientada a Objetos")

    print(estudiante.presentarse())
    print(profesor.presentarse())
