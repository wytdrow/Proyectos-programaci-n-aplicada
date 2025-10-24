"Menu donde se juntan todas las clases"
from calculadora import Calculadora
from areas import Areas


# Instancias con valores por defecto (usa constructores)
calc = Calculadora(nombre="Calculadora-h", precision=1e-10, max_iter=10000)
geo = Areas(pi=3.141592653589793)


def leer_float(mensaje: str) -> float:
    while True:
        dato = input(mensaje).strip()
        try:
            return float(dato)
        except ValueError:
            print("Entrada inválida. Intente de nuevo con un número (use punto decimal si es necesario).")


def leer_int(mensaje: str) -> int:
    while True:
        dato = input(mensaje).strip()
        try:
            return int(dato)
        except ValueError:
            print("Entrada inválida. Debe ser un entero. Intente de nuevo.")


def menu_principal() -> None:
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print(f"[Info] Nombre: {calc.nombre}")
        print("1) Operaciones básicas ( +  -  *  / )")
        print("2) Operaciones avanzadas (potencia, raíz, factorial)")
        print("3) Áreas (cuadrado, rectángulo, circunferencia, triángulo rectángulo)")
        print("4) Ver últimos resultados")
        print("0) Salir")


        op = input("Elija una opción: ").strip()
        if op == "1":
            menu_basicas()
        elif op == "2":
            menu_avanzadas()
        elif op == "3":
            menu_areas()
        elif op == "4":
            mostrar_ultimos()
        elif op == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, inténtelo de nuevo.")


def menu_basicas() -> None:
    while True:
        print("\n-- Operaciones básicas --")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("0) Volver")

        op = input("Elija una opción: ").strip()
        if op == "0":
            return

        a = leer_float("Ingrese a: ")
        b = leer_float("Ingrese b: ")

        try:
            if op == "1":
                print("Resultado:", calc.sumar(a, b))
            elif op == "2":
                print("Resultado:", calc.restar(a, b))
            elif op == "3":
                print("Resultado:", calc.multiplicar(a, b))
            elif op == "4":
                print("Resultado:", calc.dividir(a, b))
            else:
                print("Opción no válida.")
        except Exception as e:
            print("Error:", e)


def menu_avanzadas() -> None:
    while True:
        print("\n-- Operaciones avanzadas --")
        print("1) Potenciación base^exponente (exponente entero)")
        print("2) Raíz cuadrada")
        print("3) Factorial (entero >= 0)")
        print("0) Volver")

        op = input("Elija una opción: ").strip()
        if op == "0":
            return

        try:
            if op == "1":
                base = leer_float("Base: ")
                exp = leer_int("Exponente entero (puede ser negativo): ")
                print("Resultado:", calc.potencia(base, exp))
            elif op == "2":
                x = leer_float("Número (>= 0): ")
                print("Resultado:", calc.raiz_cuadrada(x))
            elif op == "3":
                n = leer_int("n entero (>= 0): ")
                print("Resultado:", calc.factorial(n))
            else:
                print("Opción no válida.")
        except Exception as e:
            print("Error:", e)


def menu_areas() -> None:
    while True:
        print("\n-- Áreas de figuras --")
        print("1) Cuadrado (lado)")
        print("2) Rectángulo (base, altura)")
        print("3) Circunferencia (radio)")
        print("4) Triángulo rectángulo (cateto a, cateto b)")
        print("0) Volver")

        op = input("Elija una opción: ").strip()
        if op == "0":
            return

        try:
            if op == "1":
                lado = leer_float("Lado: ")
                print("Área:", geo.cuadrado(lado))
            elif op == "2":
                base = leer_float("Base: ")
                altura = leer_float("Altura: ")
                print("Área:", geo.rectangulo(base, altura))
            elif op == "3":
                radio = leer_float("Radio: ")
                print("Área:", geo.circunferencia(radio))
            elif op == "4":
                a = leer_float("Cateto a: ")
                b = leer_float("Cateto b: ")
                print("Área:", geo.triangulo_rectangulo(a, b))
            else:
                print("Opción no válida.")
        except Exception as e:
            print("Error:", e)

def mostrar_ultimos() -> None:
    print("\n-- Últimos resultados --")
    print("Calculadora.ultimo_resultado:", calc.ultimo_resultado)
    print("Areas.ultimo_area:", geo.ultimo_area)


if __name__ == "__main__":
    menu_principal()
