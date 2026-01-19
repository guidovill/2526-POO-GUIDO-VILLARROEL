"""
Tarea Semana 6 - POO en Python
Funcionalidad:
Sistema simple de empleados para demostrar:
- Clase base y clase derivada (Herencia)
- Encapsulación (atributos privados con getters/setters)
- Polimorfismo (método sobrescrito en la clase derivada)
"""

class Empleado:
    # Clase base
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.__salario_base = salario_base  # Encapsulación: atributo privado

    # Getter (leer)
    def get_salario_base(self) -> float:
        return self.__salario_base

    # Setter (modificar con validación)
    def set_salario_base(self, nuevo_salario: float) -> None:
        if nuevo_salario <= 0:
            raise ValueError("El salario debe ser mayor que 0.")
        self.__salario_base = nuevo_salario

    def calcular_pago(self) -> float:
        """
        Método que luego será sobrescrito (polimorfismo).
        En la clase base devuelve el salario base.
        """
        return self.__salario_base

    def mostrar_info(self) -> None:
        print(f"Empleado: {self.nombre} | Salario base: ${self.get_salario_base():.2f}")


class EmpleadoPorHoras(Empleado):
    # Clase derivada (Herencia)
    def __init__(self, nombre: str, salario_base: float, horas_trabajadas: int, pago_por_hora: float):
        super().__init__(nombre, salario_base)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    # Polimorfismo: sobrescritura del método calcular_pago
    def calcular_pago(self) -> float:
        """
        En esta clase, el pago total incluye:
        salario base + (horas_trabajadas * pago_por_hora)
        """
        return self.get_salario_base() + (self.horas_trabajadas * self.pago_por_hora)

    def mostrar_info(self) -> None:
        print(
            f"Empleado por horas: {self.nombre} | Base: ${self.get_salario_base():.2f} | "
            f"Horas: {self.horas_trabajadas} | Pago/hora: ${self.pago_por_hora:.2f}"
        )


def main() -> None:
    # Crear instancias (objetos)
    empleado_1 = Empleado("Ana Torres", 500.00)
    empleado_2 = EmpleadoPorHoras("Carlos Ruiz", 300.00, horas_trabajadas=20, pago_por_hora=5.50)

    # Demostrar encapsulación: modificar salario usando setter
    empleado_1.set_salario_base(550.00)

    # Mostrar información
    print("\n--- INFORMACIÓN DE EMPLEADOS ---")
    empleado_1.mostrar_info()
    empleado_2.mostrar_info()

    # Demostrar polimorfismo:
    # Ambos objetos responden a calcular_pago(), pero cada uno lo calcula diferente.
    print("\n--- PAGOS (POLIMORFISMO) ---")
    empleados = [empleado_1, empleado_2]
    for emp in empleados:
        print(f"{emp.nombre} cobrará: ${emp.calcular_pago():.2f}")


if __name__ == "__main__":
    main()
