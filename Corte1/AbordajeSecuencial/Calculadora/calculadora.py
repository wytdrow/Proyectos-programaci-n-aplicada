from typing import Union
from operaciones_basicas import OperacionesBasicas

Number = Union[int, float]


class Calculadora(OperacionesBasicas):
    """
    Calculadora que hereda de OperacionesBasicas e incorpora operaciones avanzadas.
    Atributos adicionales:
      - max_iter (int): tope de iteraciones para métodos iterativos (raíz).
    """
    def __init__(self, nombre: str = "Calculadora", precision: float = 1e-10, max_iter: int = 10_000) -> None:
        super().__init__(nombre=nombre, precision=precision)
        self._max_iter: int = 10_000
        self.max_iter = max_iter  # usa setter

    # --- max_iter ---
    @property
    def max_iter(self) -> int:
        return self._max_iter

    @max_iter.setter
    def max_iter(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("max_iter debe ser un entero positivo.")
        self._max_iter = value

    # --- Operaciones avanzadas ---
    def potencia(self, base: Number, exponente: int) -> Number:
        if not isinstance(exponente, int):
            raise TypeError("El exponente debe ser entero (int).")

        if exponente == 0:
            res = 1
            self._ultimo_resultado = float(res)
            return res

        if exponente < 0:
            if base == 0:
                raise ZeroDivisionError("0 elevado a exponente negativo no está definido.")
            res = 1 / self.potencia(base, -exponente)
            self._ultimo_resultado = float(res)
            return res

        resultado = 1
        factor = base
        n = exponente
        while n > 0:
            if n & 1:
                resultado *= factor
            factor *= factor
            n >>= 1

        self._ultimo_resultado = float(resultado)
        return resultado

    def raiz_cuadrada(self, x: Number) -> float:
        if x < 0:
            raise ValueError("La raíz cuadrada de un número negativo no es real.")
        if x == 0:
            self._ultimo_resultado = 0.0
            return 0.0

        y = x if x >= 1 else 1.0
        for _ in range(self.max_iter):
            prev = y
            y = 0.5 * (y + x / y)
            if abs(y - prev) <= self.precision:
                break

        self._ultimo_resultado = float(y)
        return y

    def factorial(self, n: int) -> int:
        if not isinstance(n, int):
            raise TypeError("n debe ser entero (int).")
        if n < 0:
            raise ValueError("El factorial no está definido para enteros negativos.")
        resultado = 1
        for k in range(2, n + 1):
            resultado *= k
        self._ultimo_resultado = float(resultado)
        return resultado
