import sys
import os
from time import sleep
from solver import solver_newton, solver_lagrange
from utils import get_int


def indent(n_spaces: int) -> str:
    return " " * n_spaces


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def menu_main():

    while True:

        clear_screen()
        print_menu_main()
        print("")

        option = get_int("? ")

        if option == 0:
            print("\nAdiós...\n")
            sleep(1)
            sys.exit(0)

        elif option == 1:

            menu_newton()

        elif option == 2:

           menu_lagrange()

        else:
            print("\nOpción no válida, intente de nuevo...\n")
            sleep(1)


def menu_newton():

    while True:
        clear_screen()
        print_menu_newton()
        print("")
        option = get_int("? ")
        clear_screen()

        if option == 0:
            break

        elif option >= 1 and option <= 2:
            solver_newton(option)
            print("\nPresiona Enter para ir al menu anterior...")
            input()
            
        else:
            print("\nOpción no válida, intente de nuevo...\n")
            sleep(1)


def menu_lagrange():

    while True:
        clear_screen()
        print_menu_lagrange()
        print("")
        option = get_int("? ")
        clear_screen()

        if option == 0:
            break

        elif option >= 1 and option <= 2:
            solver_lagrange(option)
            print("\nPresiona Enter para ir al menu anterior...")
            input()

        else:
            print("\nOpción no válida, intente de nuevo...\n")
            sleep(1)


def print_menu_main():
    print(f"{indent(2)}== Menu ==")
    print("")

    print("• 1. INTERPOLACIÓN POLINOMIAL DE NEWTON EN DIFERENCIAS DIVIDIDAS")
    print("• 2. POLINOMIOS DE INTERPOLACIÓN DE LAGRANGE")
    print("• 0. SALIR")


def print_menu_newton():

    print(f"{indent(2)}== INTERPOLACIÓN POLINOMIAL DE NEWTON EN DIFERENCIAS DIVIDIDAS ==")
    print("")

    print("• INTERPOLACIÓN POLINOMIAL DE NEWTON EN DIFERENCIAS DIVIDIDAS")
    print(f"{indent(4)}• 1.  Interpolación Lineal")
    print(f"{indent(4)}• 2.  Interpolación Cuadrática")

    print("• 0. Volver")


def print_menu_lagrange():

    print(f"{indent(2)}== POLINOMIOS DE INTERPOLACIÓN DE LAGRANGE ==")
    print("")

    print("• 1. Versión de Primer Grado")
    print("• 2. Versión de Segundo Grado")

    print("• 0. Volver")
