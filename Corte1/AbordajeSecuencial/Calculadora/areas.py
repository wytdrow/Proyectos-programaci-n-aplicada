from typing import Union, Tuple, Optional

Number = Union[int, float]


class Areas:
    """
    Clase para áreas con estado y propiedades.
    Atributos:
      - pi (float): constante PI configurable.
      - ultimo_area (float|None): último cálculo realizado (solo lectura).
    """
    def __init__(self, pi: float = 3.141592653589793) -> None:
        self._pi: float = 3.141592653589793
        self._ultimo_area: Optional[float] = None
        self.pi = pi  # usa setter

    # --- pi ---
    @property
    def pi(self) -> float:
        return self._pi

    @pi.setter
    def pi(self, value: float) -> None:
        try:
            v = float(value)
        except Exception as e:
            raise TypeError("pi debe ser numérico.") from e
        if v <= 0:
            raise ValueError("pi debe ser positivo.")
        self._pi = v

    # --- ultimo_area (solo lectura) ---
    @property
    def ultimo_area(self) -> Optional[float]:
        return self._ultimo_area

    # --- utilidades ---
    @staticmethod
    def _validar_no_negativos(valores: Tuple[Number, ...]) -> None:
        for v in valores:
            if v < 0:
                raise ValueError("Las dimensiones no pueden ser negativas.")

    # --- áreas ---
    def cuadrado(self, lado: Number) -> Number:
        self._validar_no_negativos((lado,))
        area = lado * lado
        self._ultimo_area = float(area)
        return area

    def rectangulo(self, base: Number, altura: Number) -> Number:
        self._validar_no_negativos((base, altura))
        area = base * altura
        self._ultimo_area = float(area)
        return area

    def circunferencia(self, radio: Number) -> float:
        self._validar_no_negativos((radio,))
        area = self.pi * radio * radio
        self._ultimo_area = float(area)
        return area

    def triangulo_rectangulo(self, cateto_a: Number, cateto_b: Number) -> Number:
        self._validar_no_negativos((cateto_a, cateto_b))
        area = (cateto_a * cateto_b) / 2
        self._ultimo_area = float(area)
        return area
