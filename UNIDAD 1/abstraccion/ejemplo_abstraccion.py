"""
Ejemplo de ABSTRACCIÓN en POO.

Idea principal:
    Definimos una clase "abstracta" (FiguraGeometrica) que representa
    el concepto general de figura, sin entrar en detalles de cómo se
    calcula el área. Las clases hijas (Rectangulo y Circulo) se
    encargan de implementar los detalles.

En este archivo nos enfocamos en la ABSTRACCIÓN:
    - Nos interesa la idea de "calcular_area", no la fórmula interna.
"""

from math import pi


class FiguraGeometrica:
    """
    Esta clase representa la ABSTRACCIÓN de una figura.
    No sabemos qué tipo de figura es, pero sabemos que debe
    poder calcular su área.
    """

    def calcular_area(self):
        """
        Método genérico que debería ser redefinido por las clases hijas.
        Aquí solo definimos la idea general.
        """
        raise NotImplementedError(
            "Este método debe ser implementado por las subclases."
        )


class Rectangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        # Implementamos el detalle específico para un rectángulo
        return self.base * self.altura


class Circulo(FiguraGeometrica):
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        # Implementamos el detalle específico para un círculo
        return pi * (self.radio ** 2)


if __name__ == "__main__":
    # Demostración rápida
    figuras: list[FiguraGeometrica] = [
        Rectangulo(base=4, altura=3),
        Circulo(radio=2)
    ]

    for figura in figuras:
        # Aquí usamos la ABSTRACCIÓN: no nos importa qué figura es,
        # solo sabemos que tiene un método calcular_area().
        print(f"Área de la figura: {figura.calcular_area():.2f}")
