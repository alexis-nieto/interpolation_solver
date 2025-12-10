import sympy as sp
import sys
from utils import get_float, get_int

sig_fig = 8

############################################

def solver_newton(option: int):

    try:
        f = input("\nFunción? ")
        x = get_float("x? ")
        x0 = get_float("x0? ")
        x1 = get_float("x1? ")

        real_value = solver_real_value(f, x)

        if option == 1:

            # Lineal Interpolation
            
            estimated_value = solver_estimated_value_newton_1(f, x, x0, x1)

        elif option == 2:

            x2 = get_float("x2? ") # Include also x2 if 

            # Quadratic Interpolation
            estimated_value = solver_estimated_value_newton_2(f, x, x0, x1, x2)
        
        error = solver_error(real_value, estimated_value)

        print("\nValor real:", real_value)
        print("Valor estimado:", estimated_value)
        print("Error:", round(error, 2),"%")

    except Exception as e:
        print(f"\nError al procesar la función o los datos: {e}\n")


def solver_lagrange(option: int):

    try:
        f = input("\nFunción? ")
        x = get_float("x? ")
        x0 = get_float("x0? ")
        x1 = get_float("x1? ")

        real_value = solver_real_value(f, x)

        if option == 1:

            # Lineal Interpolation
            
            estimated_value = solver_estimated_value_lagrange_1(f, x, x0, x1)

        elif option == 2:

            x2 = get_float("x2? ") # Include also x2 if 

            # Quadratic Interpolation
            estimated_value = solver_estimated_value_lagrange_2(f, x, x0, x1, x2)
        
        error = solver_error(real_value, estimated_value)

        print("\nValor real:", real_value)
        print("Valor estimado:", estimated_value)
        print("Error:", round(error, 2),"%")

    except Exception as e:
        print(f"\nError al procesar la función o los datos: {e}\n")


def solver_real_value(function: str, x: float):

    sy_x = sp.symbols('x')
    f = sp.sympify(function, locals={'e': sp.E, 'pi': sp.pi})

    evaluation = f.subs(sy_x, x)

    return round(evaluation.evalf(), sig_fig)


def solver_error(real_value: float, estimated_value: float):

    error = abs((real_value - estimated_value)*(100)/real_value)

    return round(error, sig_fig)


def solver_estimated_value_newton_1(f: str, x: float, x0: float, x1: float):

    sy_x = sp.symbols('x')
    f = sp.sympify(f, locals={'e': sp.E, 'pi': sp.pi})

    f_x0 = f.subs(sy_x, x0)
    f_x1 = f.subs(sy_x, x1)

    print("\n=== Proceso ===")

    print("")
    print("x: ", round(x, sig_fig))
    print("x0: ", round(x0, sig_fig))
    print("x1: ", round(x1, sig_fig))

    print("")
    print("f(x0): ", round(f_x0.evalf(), sig_fig))
    print("f(x1): ", round(f_x1.evalf(), sig_fig))

    print("\n====================")

    formula_result = f_x1 + ((f_x1 - f_x0)/(x1 - x0))*(x - x1)

    return round(formula_result.evalf(), sig_fig)


def solver_estimated_value_newton_2(f: str, x: float, x0: float, x1: float, x2: float):

    sy_x = sp.symbols('x')
    f = sp.sympify(f, locals={'e': sp.E, 'pi': sp.pi})

    f_x0 = f.subs(sy_x, x0)
    f_x1 = f.subs(sy_x, x1)
    f_x2 = f.subs(sy_x, x2)

    # Define b0, b1, b2
    b0 = f_x0
    b1 = (f_x1 - f_x0)/(x1 - x0)
    b2 = ((f_x2 - f_x1)/(x2 - x1) - (f_x1 - f_x0)/(x1 - x0))/(x2 - x0)

    print("\n=== Proceso ===")

    print("")
    print("x: ", round(x, sig_fig))
    print("x0: ", round(x0, sig_fig))
    print("x1: ", round(x1, sig_fig))
    print("x2: ", round(x2, sig_fig))

    print("")
    print("f(x0): ", round(f_x0.evalf(), sig_fig))
    print("f(x1): ", round(f_x1.evalf(), sig_fig))
    print("f(x2): ", round(f_x2.evalf(), sig_fig))

    print("")
    print("b0: ", round(b0.evalf(), sig_fig))
    print("b1: ", round(b1.evalf(), sig_fig))
    print("b2: ", round(b2.evalf(), sig_fig))

    print("\n====================")

    # Inject into the Newton's formula
    formula_result = b0 + b1*(x - x0) + b2*(x - x0)*(x - x1)

    return round(formula_result.evalf(), sig_fig)

def solver_estimated_value_lagrange_1(f: str, x: float, x0: float, x1: float):

    sy_x = sp.symbols('x')
    f = sp.sympify(f, locals={'e': sp.E, 'pi': sp.pi})

    f_x0 = f.subs(sy_x, x0)
    f_x1 = f.subs(sy_x, x1)

    print("\n=== Proceso ===")

    print("")
    print("x: ", round(x, sig_fig))
    print("x0: ", round(x0, sig_fig))
    print("x1: ", round(x1, sig_fig))

    print("")
    print("f(x0): ", round(f_x0.evalf(), sig_fig))
    print("f(x1): ", round(f_x1.evalf(), sig_fig))

    print("\n====================")

    # Linear Lagrange interpolation
    formula_result = ((x - x1)/(x0 - x1))*f_x0 + ((x - x0)/(x1 - x0))*f_x1

    return round(formula_result.evalf(), sig_fig)


def solver_estimated_value_lagrange_2(f: str, x: float, x0: float, x1: float, x2: float):

    sy_x = sp.symbols('x')
    f = sp.sympify(f, locals={'e': sp.E, 'pi': sp.pi})

    f_x0 = f.subs(sy_x, x0)
    f_x1 = f.subs(sy_x, x1)
    f_x2 = f.subs(sy_x, x2)

    print("\n=== Proceso ===")

    print("")
    print("x: ", round(x, sig_fig))
    print("x0: ", round(x0, sig_fig))
    print("x1: ", round(x1, sig_fig))
    print("x2: ", round(x2, sig_fig))

    print("")
    print("f(x0): ", round(f_x0.evalf(), sig_fig))
    print("f(x1): ", round(f_x1.evalf(), sig_fig))
    print("f(x2): ", round(f_x2.evalf(), sig_fig))

    print("\n====================")

    # Second degree Lagrange interpolation
    formula_result = ((x - x1)*(x - x2))/((x0 - x1)*(x0 - x2))*f_x0 + \
                     ((x - x0)*(x - x2))/((x1 - x0)*(x1 - x2))*f_x1 + \
                     ((x - x0)*(x - x1))/((x2 - x0)*(x2 - x1))*f_x2

    return round(formula_result.evalf(), sig_fig)