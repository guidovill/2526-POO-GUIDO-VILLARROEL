# clima_poo.py
"""
Tarea: Promedio semanal del clima (POO)
- Encapsulamiento (property), herencia y polimorfismo.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List

DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


@dataclass
class RegistroClima:
    dia: str

    def resumen(self) -> str:
        return f"Registro del día: {self.dia}"


class ClimaDiario(RegistroClima):
    def __init__(self, dia: str, temperatura: float) -> None:
        super().__init__(dia)
        self._temperatura: float = 0.0
        self.temperatura = temperatura

    @property
    def temperatura(self) -> float:
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor: float) -> None:
        if not isinstance(valor, (int, float)):
            raise TypeError("La temperatura debe ser numérica.")
        self._temperatura = float(valor)

    def resumen(self) -> str:
        return f"{self.dia}: {self.temperatura:.2f} °C"


class SemanaClimatica:
    def __init__(self) -> None:
        self._registros: List[ClimaDiario] = []

    def ingresar_datos(self) -> None:
        print("\n📌 Registro de temperaturas semanales (POO)\n")
        self._registros.clear()
        for dia in DIAS_SEMANA:
            temp = self._leer_temperatura(dia)
            self._registros.append(ClimaDiario(dia, temp))

    def _leer_temperatura(self, dia: str) -> float:
        while True:
            entrada = input(f"Ingrese la temperatura de {dia} (°C): ").strip().replace(",", ".")
            try:
                return float(entrada)
            except ValueError:
                print("⚠️ Entrada inválida. Ingrese un número (ej.: 23.5).")

    def calcular_promedio(self) -> float:
        if not self._registros:
            return 0.0
        return sum(r.temperatura for r in self._registros) / len(self._registros)

    def mostrar_resumen(self) -> None:
        print("\n🧾 Resumen semanal (POO)")
        for r in self._registros:
            print(f"- {r.resumen()}")
        print(f"\n✅ Promedio semanal: {self.calcular_promedio():.2f} °C")


def main() -> None:
    semana = SemanaClimatica()
    semana.ingresar_datos()
    semana.mostrar_resumen()


if __name__ == "__main__":
    main()
