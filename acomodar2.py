import os
import shutil

def organizar_archivos_descargas():
    descargas_folder = "C:\\Users\\Usuario\\Descargas"  # Ruta de la carpeta de descargas
    carpetas_ext = {
        ".docx": "word",
        ".xlsx": "excel",
        ".pptx": "powerpoint",
        ".jpg": "imagenes",
        ".png": "imagenes",
        ".mp4": "videos",
        ".py": "programacion",
        ".zip": "otros",
        ".mp3": "musica",
        ".exe": "ejecutables"
    }

    for archivo in os.listdir(descargas_folder):
        archivo_path = os.path.join(descargas_folder, archivo)

        if os.path.isfile(archivo_path):
            nombre, extension = os.path.splitext(archivo)
            extension = extension.lower()

            if extension in carpetas_ext:
                carpeta_destino = os.path.join(descargas_folder, carpetas_ext[extension])

                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)

                archivo_destino = os.path.join(carpeta_destino, archivo)

                if os.path.exists(archivo_destino):
                    opcion = input(f"El archivo '{archivo}' ya existe en la carpeta '{carpetas_ext[extension]}'. ¿Deseas reemplazarlo? (S/N): ")
                    if opcion.lower() == "s":
                        shutil.move(archivo_path, archivo_destino)
                        print(f"Archivo '{archivo}' movido a la carpeta '{carpetas_ext[extension]}'")
                else:
                    shutil.move(archivo_path, archivo_destino)
                    print(f"Archivo '{archivo}' movido a la carpeta '{carpetas_ext[extension]}'")
            else:
                carpeta_destino = os.path.join(descargas_folder, "otros")

                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)

                archivo_destino = os.path.join(carpeta_destino, archivo)
                shutil.move(archivo_path, archivo_destino)
                print(f"Archivo '{archivo}' movido a la carpeta 'otros'")

organizar_archivos_descargas()