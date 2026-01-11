"""
Tarea: Tipos de datos e Identificadores (Python)
Funcionalidad:
- Registra datos básicos de una persona.
- Calcula el IMC (Índice de Masa Corporal).
- Indica si el IMC está en rango saludable (aprox. 18.5 a 24.9).
"""

def calcular_imc(peso_kg: float, estatura_m: float) -> float:
    """Calcula el IMC con la fórmula: peso / estatura^2."""
    return peso_kg / (estatura_m ** 2)


def esta_en_rango_saludable(imc: float) -> bool:
    """Retorna True si el IMC está en un rango saludable aproximado."""
    return 18.5 <= imc <= 24.9


def main() -> None:
    # string
    nombre_completo: str = input("Ingrese su nombre completo: ").strip()

    # integer
    edad: int = int(input("Ingrese su edad (años): "))

    # float
    estatura_m: float = float(input("Ingrese su estatura en metros (ej. 1.74): "))
    peso_kg: float = float(input("Ingrese su peso en kg (ej. 70.5): "))

    # boolean (ejemplo: condición simple basada en edad)
    es_mayor_de_edad: bool = edad >= 18

    imc: float = calcular_imc(peso_kg, estatura_m)
    saludable: bool = esta_en_rango_saludable(imc)

    # Salida (claridad)
    print("\n--- RESULTADOS ---")
    print(f"Nombre: {nombre_completo}")
    print(f"Edad: {edad} años")
    print(f"Mayor de edad: {es_mayor_de_edad}")
    print(f"Estatura: {estatura_m} m")
    print(f"Peso: {peso_kg} kg")
    print(f"IMC: {imc:.2f}")
    print(f"IMC en rango saludable: {saludable}")

    # Comentario de lógica:
    # Si 'saludable' es False, no significa diagnóstico médico, solo guía general.
    if not saludable:
        print("Observación: El IMC está fuera del rango saludable aproximado.")


if __name__ == "__main__":
    main()
