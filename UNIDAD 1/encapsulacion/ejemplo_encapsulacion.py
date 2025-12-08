"""
Ejemplo de ENCAPSULACIÓN en POO.

Idea principal:
    Proteger los datos internos de la clase y controlar
    cómo se accede o modifica esa información.

En este archivo nos enfocamos en la ENCAPSULACIÓN:
    - El saldo de la cuenta no se puede modificar directamente.
    - Solo se cambia usando depositar() y retirar().
"""


class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        # Atributo "protegido/privado" por convención (un guion bajo)
        self._saldo = saldo_inicial

    # --- ENCAPSULACIÓN mediante propiedades (getters y setters) ---

    @property
    def saldo(self) -> float:
        """Devuelve el saldo actual (solo lectura)."""
        return self._saldo

    def depositar(self, monto: float) -> None:
        """Aumenta el saldo si el monto es válido."""
        if monto <= 0:
            print("❌ El monto a depositar debe ser positivo.")
            return
        self._saldo += monto
        print(f"✅ Depósito de {monto:.2f} realizado. Saldo actual: {self._saldo:.2f}")

    def retirar(self, monto: float) -> None:
        """Disminuye el saldo si hay suficiente dinero."""
        if monto <= 0:
            print("❌ El monto a retirar debe ser positivo.")
            return

        if monto > self._saldo:
            print("❌ Fondos insuficientes.")
            return

        self._saldo -= monto
        print(f"✅ Retiro de {monto:.2f} realizado. Saldo actual: {self._saldo:.2f}")


if __name__ == "__main__":
    cuenta = CuentaBancaria("Guido Villarroel", saldo_inicial=100.0)

    # No accedemos directamente a _saldo, usamos los métodos públicos.
    print(f"Saldo inicial: {cuenta.saldo:.2f}")
    cuenta.depositar(50)
    cuenta.retirar(30)
    cuenta.retirar(500)  # Este retiro no se permite por falta de fondos
