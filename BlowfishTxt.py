from Crypto.Cipher import Blowfish
import binascii
import os
import platform
import time
import ctypes
import random
import secrets


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


def pad(data):
    """
    Aplica relleno PKCS7 a los datos para que tengan un tamaño múltiplo del tamaño del bloque.
    """
    block_size = Blowfish.block_size
    padding_len = block_size - (len(data) % block_size)
    padding = bytes([padding_len] * padding_len)
    return data + padding

def unpad(data):
    """
    Elimina el relleno PKCS7 de los datos descifrados.
    """
    padding_len = data[-1]
    return data[:-padding_len]

def encrypt_blowfish_ecb(key, data):
    """
    Encripta los datos en modo ECB utilizando la clave proporcionada.
    """
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data))
    return ciphertext

def decrypt_blowfish_ecb(key, ciphertext):
    """
    Desencripta los datos en modo ECB utilizando la clave proporcionada.
    """
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    data = unpad(cipher.decrypt(ciphertext))
    return data

def encrypt_blowfish_cbc(key, iv, data):
    """
    Encripta los datos en modo CBC utilizando la clave y el IV proporcionados.
    """
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data))
    return ciphertext

def decrypt_blowfish_cbc(key, iv, ciphertext):
    """
    Desencripta los datos en modo CBC utilizando la clave y el IV proporcionados.
    """
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    data = unpad(cipher.decrypt(ciphertext))
    return data


def generate_key():
    key_bytes = secrets.token_bytes(16)  # Genera 16 bytes de datos aleatorios seguros
    
    # Convierte los bytes en una cadena hexadecimal
    key_hex = key_bytes.hex()
    
    # Mapa los bytes a caracteres imprimibles
    key_characters = [chr(b % 94 + 33) for b in key_bytes]
    key_characters_str = ''.join(key_characters)
    
    print("Clave generada en formato hexadecimal:", key_hex)
    print("Clave generada en caracteres imprimibles:", key_characters_str)

   

import os
import binascii

def generate_iv():
    """
    Genera un IV aleatorio de 8 dígitos y lo muestra en formato decimal y hexadecimal.
    """
    iv = ''.join([str(random.randint(0, 9)) for _ in range(8)])  # Genera 8 números aleatorios en formato decimal
    iv_hex = hex(int(iv))[2:]  # Convierte a hexadecimal sin ceros adicionales
    ##print("IV generado (hexadecimal):", iv_hex)
    print("IV generado:", iv)
    return iv_hex

def print_ecb_menu():
    """
    Imprime el menú del modo ECB en la consola.
    """
    print("_" * 36)
    print("           Modo Actual: ECB \n")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Generar Nueva Clave")
    print("4. Cambiar a Modo CBC")
    print("5. Salir")

def print_cbc_menu():
    """
    Imprime el menú del modo CBC en la consola.
    """
    print("_" * 36)
    print("           Modo Actual: CBC \n")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Generar Nueva Clave")
    print("4. Generar Nuevo IV")
    print("5. Cambiar a Modo ECB")
    print("6. Salir")

def main():
    key = None
    iv = None
    mode = "ECB"
    welcome_shown = False
    
    while True:
        if not welcome_shown:
            clear_screen()
            print("=" * 36)
            print("| Bienvenido al algoritmo Blowfish |")
            print("=" * 36)
            welcome_shown = True
        
        if mode == "ECB":
            print_ecb_menu()
        elif mode == "CBC":
            print_cbc_menu()
        
        choice = input("Seleccione una opción: ")
        
        if mode == "ECB":
            if choice == "1":
                print("_" * 36+"\n")
                key = input("Ingrese la clave: ").encode()
                key = key + b'\0' * (16 - len(key))
                data = input("Ingrese los datos a cifrar: ").encode()
                ciphertext = encrypt_blowfish_ecb(key, data)
                print("Texto cifrado (en hexadecimal):", binascii.hexlify(ciphertext).decode())
            elif choice == "2":
                print("_" * 36+"\n")
                key = input("Ingrese la clave: ").encode()
                key = key + b'\0' * (16 - len(key))
                data = input("Ingrese los datos a descifrar (en hexadecimal): ")
                data = bytes.fromhex(data)
                decrypted_data = decrypt_blowfish_ecb(key, data)
                print("Texto descifrado:", decrypted_data.decode())
            elif choice == "3":
                print("_" * 36+"\n")
                key = generate_key()
            elif choice == "4":
                print("\n")
                print("Cambiando de Modo...")
                time.sleep(2)  # Esperar 2 segundos antes de salir
                clear_screen()
                mode = "CBC"
                welcome_shown = False  # Restablecer la variable para mostrar el mensaje de bienvenida
            elif choice == "5":
                print("\n")
                print("Saliendo del programa...")
                time.sleep(2)  # Esperar 2 segundos antes de salir
                break
            else:
                print("Selección no válida.")
        
        elif mode == "CBC":
            if choice == "1":
                print("_" * 36+"\n")
                key = input("Ingrese la clave: ").encode()
                key = key + b'\0' * (16 - len(key))
                iv = input("Ingrese el IV: ").encode()
                iv = iv + b'\0' * (8 - len(iv))
                data = input("Ingrese los datos a cifrar: ").encode()
                ciphertext = encrypt_blowfish_cbc(key, iv, data)
                print("Texto cifrado (en hexadecimal):", binascii.hexlify(ciphertext).decode())
            elif choice == "2":
                print("_" * 36+"\n")
                key = input("Ingrese la clave: ").encode()
                key = key + b'\0' * (16 - len(key))
                iv = input("Ingrese el IV: ").encode()
                iv = iv + b'\0' * (8 - len(iv))
                data = input("Ingrese los datos a descifrar (en hexadecimal): ")
                data = bytes.fromhex(data)
                decrypted_data = decrypt_blowfish_cbc(key, iv, data)
                print("Texto descifrado:", decrypted_data.decode())
            elif choice == "3":
                print("_" * 36+"\n")
                key = generate_key()
            elif choice == "4":
                print("_" * 36+"\n")
                iv = generate_iv()
            elif choice == "5":
                print("\n")
                print("Cambiando de Modo...")
                time.sleep(2)  # Esperar 2 segundos antes de salir
                clear_screen()
                mode = "ECB"
                welcome_shown = False  # Restablecer la variable para mostrar el mensaje de bienvenida
            elif choice == "6":
                print("\n")
                print("Saliendo del programa...")
                time.sleep(2)  # Esperar 2 segundos antes de salir
                break
            else:
                print("Selección no válida.")

if __name__ == "__main__":
    main()
