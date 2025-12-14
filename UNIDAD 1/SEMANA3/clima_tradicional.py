# clima_tradicional.py
"""
Tarea: Promedio semanal del clima (Programación Tradicional)
- Solicita 7 temperaturas (una por día) usando funciones.
- Calcula y muestra el promedio semanal.
"""

from typing import List

DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def leer_temperatura(dia: str) -> float:
    while True:
        entrada = input(f"Ingrese la temperatura de {dia} (°C): ").strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("⚠️ Entrada inválida. Ingrese un número (ej.: 23.5).")


def ingresar_temperaturas_semana() -> List[float]:
    temperaturas: List[float] = []
    print("\n📌 Registro de temperaturas semanales\n")
    for dia in DIAS_SEMANA:
        temperaturas.append(leer_temperatura(dia))
    return temperaturas


def calcular_promedio(temperaturas: List[float]) -> float:
    return sum(temperaturas) / len(temperaturas) if temperaturas else 0.0


def mostrar_resumen(temperaturas: List[float]) -> None:
    print("\n🧾 Resumen semanal")
    for dia, temp in zip(DIAS_SEMANA, temperaturas):
        print(f"- {dia}: {temp:.2f} °C")

    promedio = calcular_promedio(temperaturas)
    print(f"\n✅ Promedio semanal: {promedio:.2f} °C")


def main() -> None:
    temperaturas = ingresar_temperaturas_semana()
    mostrar_resumen(temperaturas)


if __name__ == "__main__":
    main()
