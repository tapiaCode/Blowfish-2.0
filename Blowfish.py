from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto import Random
from tkinter import filedialog
from colorama import Fore, init
from datetime import datetime
import tkinter as tk
import pyfiglet
import os
import time
import ctypes
import platform
import secrets

# Inicializar colorama (esto solo es necesario una vez)
init(autoreset=True)

# Crear una instancia de la clase Figlet
custom_figlet = pyfiglet.Figlet(font='slant')

# Obtener el arte de texto
texto_personalizado = custom_figlet.renderText('    UPDS    ')

# Obtener la fecha actual
fecha_actual = datetime.now().strftime("%Y-%m-%d") #%H:%M:%S

# Cambiar el color del texto manteniendo el fondo constante
texto_coloreado = f"{Fore.BLUE}{texto_personalizado}"

def clear_screen():
    """
    Limpia la pantalla de la consola, función específica para Windows y sistemas Unix.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def generate_key():
    key_bytes = secrets.token_bytes(16)  # Genera 16 bytes de datos aleatorios seguros
    
    # Convierte los bytes en una cadena hexadecimal
    key_hex = key_bytes.hex()
    
    # Mapa los bytes a caracteres imprimibles
    key_characters = [chr(b % 94 + 33) for b in key_bytes]
    key_characters_str = ''.join(key_characters)
    
    print("Clave generada en formato hexadecimal:", key_hex)
    print("Clave generada en caracteres imprimibles:", key_characters_str)


def encrypt_file(input_file, output_file, key):
    bs = Blowfish.block_size
    key = key.encode('utf-8')
    iv = Random.new().read(bs)

    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)

    with open(input_file, 'rb') as in_file:
        with open(output_file, 'wb') as out_file:
            out_file.write(iv)
            while True:
                chunk = in_file.read(1024 * bs)
                if len(chunk) == 0:
                    break
                elif len(chunk) % bs != 0:
                    chunk += b' ' * (bs - len(chunk) % bs)
                out_file.write(cipher.encrypt(chunk))

def decrypt_file(input_file, output_file, key):
    bs = Blowfish.block_size
    key = key.encode('utf-8')

    with open(input_file, 'rb') as in_file:
        iv = in_file.read(bs)
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
        with open(output_file, 'wb') as out_file:
            while True:
                chunk = in_file.read(1024 * bs)
                if len(chunk) == 0:
                    break
                out_file.write(cipher.decrypt(chunk))

def main_menu():
     
    welcome_shown = False
    
    while True:
        if not welcome_shown:
            clear_screen()
            # Imprimir el arte de texto
            print(f"{Fore.BLUE}-" * 50)
            print(texto_coloreado)
            # Imprimir la fecha actual
            print(f"{Fore.GREEN}Fecha actual: {fecha_actual}")
            print(f"{Fore.BLUE}-" * 50)

            welcome_shown = True

        print("_" * 50+"\n")
        print("Menú:")
        print("1. Encriptar archivo")
        print("2. Desencriptar archivo")
        print("3. Generar clave segura")
        print("4. Salir")

        choice = input("Elija una opción (1-4): ")

        if choice == '1':
            
            input_file = get_file_path()
            if input_file:
                key = input("Ingrese la clave de cifrado: ")
                output_file = get_save_file_path()  # Solicitar la ubicación del archivo de salida
                encrypt_file(input_file, output_file, key)
                print(f"El archivo {input_file} se ha cifrado y guardado en {output_file}")
        elif choice == '2':
            input_file = get_file_path()
            if input_file:
                key = input("Ingrese la clave de descifrado: ")
                output_file = get_save_file_path()  # Solicitar la ubicación del archivo de salida
                decrypt_file(input_file, output_file, key)
                print(f"El archivo {input_file} se ha descifrado y guardado en {output_file}")
        elif choice == '3':
            print("_" * 50+"\n")
            generate_key()            
        elif choice == '4':
            print("\n")
            print("Saliendo del programa...")
            time.sleep(2)  # Esperar 2 segundos antes de salir
            
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def get_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def get_save_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename()
    return file_path

if __name__ == "__main__":
    main_menu()
