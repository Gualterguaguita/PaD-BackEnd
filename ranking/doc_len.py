# Genera 'doclen.txt' en la carpeta 'data', esta es usada en answer_server.py

import os
import re

def check_word(palabra):
    if re.search("^[a-z0-9]+$", palabra):
        return palabra
    else:
        return ""

def main():
    path = r"indexacion/data/all_content.txt"
    output_path = r"ranking/data/doclen.txt"

    try: 
        with open(path, "r",encoding='utf-8') as archivo:
            with open(output_path, "w",encoding='utf-8') as output_file:
                for num_linea, linea in enumerate(archivo, start=1):
                    palabras = linea.lower().split()
                    document_len = sum(1 for palabra in palabras if len(check_word(palabra)) > 0)
                    
                    # Escribir la longitud de la línea en el archivo "doclen.txt"
                    output_file.write(f"{document_len}\n")

        print("Archivo 'doclen.txt' creado con exito")

    except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
