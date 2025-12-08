"""
Ejemplo de POLIMORFISMO en POO.

Idea principal:
    Objetos de distintas clases responden al mismo mensaje (método)
    de maneras diferentes, pero se pueden tratar de forma uniforme.

En este archivo nos enfocamos en el POLIMORFISMO:
    - Todos los animales tienen el método hablar().
    - Cada animal implementa hablar() a su manera.
"""


class Animal:
    def hablar(self) -> str:
        """Método genérico. Se espera que las subclases lo redefinan."""
        raise NotImplementedError("Este método debe ser implementado por las subclases.")


class Perro(Animal):
    def hablar(self) -> str:
        return "Guau 🐶"


class Gato(Animal):
    def hablar(self) -> str:
        return "Miau 🐱"


class Loro(Animal):
    def hablar(self) -> str:
        return "¡Hola, Guido! 🦜"


def hacer_hablar_animales(animales: list[Animal]) -> None:
    """
    Función que demuestra el POLIMORFISMO:
    Recorre una lista de animales y llama al mismo método hablar()
    sin importar de qué clase específica sea cada objeto.
    """
    for animal in animales:
        # POLIMORFISMO: mismo método, diferentes comportamientos.
        print(animal.hablar())


if __name__ == "__main__":
    perro = Perro()
    gato = Gato()
    loro = Loro()

    lista_animales = [perro, gato, loro]
    hacer_hablar_animales(lista_animales)
