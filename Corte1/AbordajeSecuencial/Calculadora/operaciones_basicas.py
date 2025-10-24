from typing import Union, Optional

Number = Union[int, float]


class OperacionesBasicas:
    """
    Clase base con estado y propiedades (getters/setters estilo Python con @property).
    Atributos:
      - nombre (str): nombre lógico de la instancia.
      - precision (float): tolerancia para métodos numéricos.
      - ultimo_resultado (float): último resultado calculado (solo lectura).
    """
    def __init__(self, nombre: str = "Calculadora", precision: float = 1e-10) -> None:
        self._nombre: str = ""
        self._precision: float = 1e-10
        self._ultimo_resultado: Optional[float] = None
        # Usar setters para validar
        self.nombre = nombre
        self.precision = precision

    # --- nombre ---
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("nombre debe ser una cadena no vacía.")
        self._nombre = value.strip()

    # --- precision ---
    @property
    def precision(self) -> float:
        return self._precision

    @precision.setter
    def precision(self, value: float) -> None:
        try:
            v = float(value)
        except Exception as e:
            raise TypeError("precision debe ser un número.") from e
        if v <= 0:
            raise ValueError("precision debe ser positiva.")
        self._precision = v

    # --- ultimo_resultado (solo lectura) ---
    @property
    def ultimo_resultado(self) -> Optional[float]:
        return self._ultimo_resultado

    # --- Operaciones básicas ---
    def sumar(self, a: Number, b: Number) -> Number:
        res = a + b
        self._ultimo_resultado = float(res)
        return res

    def restar(self, a: Number, b: Number) -> Number:
        res = a - b
        self._ultimo_resultado = float(res)
        return res

    def multiplicar(self, a: Number, b: Number) -> Number:
        res = a * b
        self._ultimo_resultado = float(res)
        return res

    def dividir(self, a: Number, b: Number) -> Number:
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        res = a / b
        self._ultimo_resultado = float(res)
        return res
