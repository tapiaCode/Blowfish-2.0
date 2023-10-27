from colorama import Fore, init
from datetime import datetime
import tkinter as tk
import pyfiglet
import os
import platform
import ctypes
import time


# Inicializar colorama (esto solo es necesario una vez)
init(autoreset=True)

# Crear una instancia de la clase Figlet
custom_figlet = pyfiglet.Figlet(font='slant')

# Obtener el arte de texto
texto_personalizado = custom_figlet.renderText('    UPDS    ')

# Obtener la fecha actual
fecha_actual = datetime.now().strftime("%Y-%m-%d") #%H:%M:%S

# Cambiar el color del texto manteniendo el fondo constante
texto_coloreado = f"{Fore.LIGHTBLUE_EX}{texto_personalizado}"


def clear_screen():
    """
    Limpia la pantalla de la consola, función específica para Windows y sistemas Unix.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Función para establecer el título de la ventana
def set_window_title(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        print(f'\033]0;{title}\007')

# Establecer el título de la ventana
set_window_title("Algoritmo Blowfish  UPDS")

def main():
 
    welcome_shown = False
    
    while True:
        if not welcome_shown:
            clear_screen()
            # Imprimir el arte de texto
            print(f"{Fore.BLUE}-" * 50)
            print(texto_coloreado)
            # Imprimir la fecha actual
            print(f"{Fore.BLUE}Fecha actual: {fecha_actual}")
            print(f"{Fore.BLUE}-" * 50)

            welcome_shown = True

        print("Menú Princial")
        print("1. Programa 1 - Cifrado y Descifrado de Archivos Blowfish")
        print("2. Programa 2 - Interfaz de usuario para cifrado Blowfish")
        print("3. Salir")

        choice = input(f"{Fore.BLUE}Elija una opción (1-3): ")

        if choice == '1':
            print("\n")
            print("Inresando al programa...")
            time.sleep(2)  # Esperar 2 segundos antes de salir
            clear_screen()
            # Llamar al primer programa
            import Blowfish
            Blowfish.main_menu()
            welcome_shown = False
        elif choice == '2':
            print("\n")
            print("Inresando al programa...")
            time.sleep(2)  # Esperar 2 segundos antes de salir
            clear_screen()
            # Llamar al segundo programa
            import BlowfishTxt
            BlowfishTxt.main()
            welcome_shown = False
        elif choice == '3':
            print("\n")
            print("Saliendo del programa...")
            time.sleep(2)  # Esperar 2 segundos antes de salir
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
