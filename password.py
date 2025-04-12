import random
import string

def generar_contrasena_avanzada(longitud=16, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True, excluir_similares=False):

    caracteres_posibles = ""
    if incluir_mayusculas:
        caracteres_posibles += string.ascii_uppercase
    if incluir_minusculas:
        caracteres_posibles += string.ascii_lowercase
    if incluir_numeros:
        caracteres_posibles += string.digits
    if incluir_simbolos:
        caracteres_posibles += string.punctuation

    if not caracteres_posibles:
        raise ValueError("Debes seleccionar al menos un tipo de caracter para incluir en la contraseña.")

    if excluir_similares:
        similares = "lI1oO0"
        caracteres_posibles = "".join(char for char in caracteres_posibles if char not in similares)
        if not caracteres_posibles:
            raise ValueError("Después de excluir caracteres similares, no quedan suficientes caracteres posibles.")

    contrasena = ''.join(random.choice(caracteres_posibles) for _ in range(longitud))
    return contrasena

if __name__ == "__main__":
    try:
        longitud_deseada = int(input("\nIngrese la longitud deseada de la contraseña (por defecto: 16): ") or 16)
        incluir_mayus = input("\n¿Incluir mayúsculas? (s/n): ").lower() == 's'
        incluir_minus = input("\n¿Incluir minúsculas? (s/n): ").lower() == 's'
        incluir_nums = input("\n¿Incluir números? (s/n): ").lower() == 's'
        incluir_simb = input("\n¿Incluir símbolos? (s/n): ").lower() == 's'
        excluir_simil = input("\n¿Excluir caracteres similares? (s/n): ").lower() == 's'

        contrasena_generada = generar_contrasena_avanzada(
            longitud=longitud_deseada,
            incluir_mayusculas=incluir_mayus,
            incluir_minusculas=incluir_minus,
            incluir_numeros=incluir_nums,
            incluir_simbolos=incluir_simb,
            excluir_similares=excluir_simil
        )
        print(f"\nContraseña generada: {contrasena_generada}")

    except ValueError as e:
        print(f"Error: {e}")
