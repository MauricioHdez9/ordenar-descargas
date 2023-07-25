# import os  # ! //ver para que sirve estas inportaciones
# import sys  # ! //ver para que sirve estas inportaciones
# import shutil  # ? //libreria la cual se usa para mover y copiar archivos
# import time  # ! //ver para que sirve estas inportaciones
# from random import randint  # ! //ver para que sirve estas inportaciones
# let: a
# # todo: // regresar aterminar el codigo
# # ? //explicacion
# # ! //investigacion o alerta
# # * //notas a desarrolladores
# # -- comentario normal

# # ? //esta es la ruta la cual se ordenaran los archivos de esta carpeta
# ruta_descargas = "C:\\Users\\Bienvenido\\Downloads\\"
#+ c:\Users\zigas\Downloads nueva ruta 

# ext_text = ['.docx', '.doc', '.pptx', '.doc', '.odf', '.docm', '(.docx)']
# ext_pdf = ['.pdf', '(.pdf)']
# ext_exel = ['.xlsx']
# # ? //variables de forma  arreglo que expecifican el tipo de archivo que se va ordenar
# ext_txt = ['.txt']
# ext_foto = ['.jpg', '.png', '.jpeg', '.gif', '.tiff',
#             '.psd', '.bmp', '.ico', '.svg', '(.jpeg)', '(.JPEG)']
# ext_video = ['.mov', '.avi', '.mkv', '.mkv', '.flv', '.wmv']
# ext_music = ['.mp3', '.mp4', '.wma', '.wav', '.flac', '(.mp3)', '(.mp4)']
# ext_rar = ['.zip', '.rar', '.rar5', '.7z', '.ace', '.gz']
# ext_codigo = ['.java', '.c', '.cpp', '.py', '.c#', '.php',
#               '.html', '.js', '.css', '(.cpp)', '(.c)', '(.java)']
# ext_exe = ['.exe', 'msi', '(.exe)', '(.msi)']
# ext_diagrama = ['uml', '(.drawio)']


# def ordenar(archivo, ext):  # ? // funcion que tiene como parametros el archivo y su extencion  para ser ordenados

#     for i in ext_text:
#         if ext == i:
#             # ? //shutil.move(ruta en la que nos encontramos  + nombre del archivo,ruta a la que se movera el archivo )
#             shutil.move(ruta_descargas + archivo, ruta_descargas + 'word')
#     for i in ext_txt:
#         if ext == i:
#             # ! //shutil.move //investigar que hacen estas dos funciones
#             shutil.move(ruta_descargas + archivo,
#                         ruta_descargas + 'blocdenotas')
#     for i in ext_pdf:
#         if ext == i:
#             shutil.move(ruta_descargas + archivo, ruta_descargas + 'pdf')
#     for i in ext_exel:
#         if ext == i:
#             shutil.move(ruta_descargas + archivo, ruta_descargas + 'exel')
#     for i in ext_foto:
#         if ext == i:
#             shutil.move(ruta_descargas + archivo, ruta_descargas + 'imagenes')
#     for i in ext_video:
#         if ext == i:
#             shutil.move(ruta_descargas + archivo, ruta_descargas + 'video')
#     for i in ext_music:
#         if ext == i:
#             shutil.move(ruta_descargas + archivo, ruta_descargas + 'music')
#     for i in ext_rar:
#         if ext == i:
#             shutil.move(ruta_descargas + archivo, ruta_descargas + 'rar')
#     for i in ext_exe:
#         if ext == i:
#             shutil.move(ruta_descargas + archivo, ruta_descargas + "exe")
#     for i in ext_diagrama:
#         if ext == i:
#             shutil.move(ruta_descargas + archivo, ruta_descargas + 'diagramaP')
#     for i in ext_codigo:
#         if ext == i:
#             shutil.move(ruta_descargas + archivo,
#                         ruta_descargas + 'programacion')

#         # if ext != '':
#         #   shutil.move(ruta_descargas + archivo,ruta_descargas + 'otros')


# def main():
#     print("en ejecucion .....")
#     for archivo in os.listdir(ruta_descargas):
#         nombre_archivo, ext = os.path.splitext(archivo)
#         #print(nombre_archivo,"esto tiene que salir en  algun lado ")
#         print(archivo, "tipo de extencion", ext)
#         ordenar(archivo, ext)
#     print("FIN de la  ejecucion .....")


# main()

import os
import shutil

ext_carpetas = {
    '.docx': 'word',
    '.doc': 'word',
    '.pptx': 'word',
    '.odf': 'word',
    '.docm': 'word',
    '.xlsx': 'excel',
    '.txt': 'blocdenotas',
    '.pdf': 'pdf',
    '.jpg': 'imagenes',
    '.png': 'imagenes',
    '.jpeg': 'imagenes',
    '.gif': 'imagenes',
    '.tiff': 'imagenes',
    '.psd': 'imagenes',
    '.bmp': 'imagenes',
    '.ico': 'imagenes',
    '.svg': 'imagenes',
    '.mov': 'video',
    '.avi': 'video',
    '.mkv': 'video',
    '.flv': 'video',
    '.wmv': 'video',
    '.mp3': 'music',
    '.mp4': 'music',
    '.wma': 'music',
    '.wav': 'music',
    '.flac': 'music',
    '.zip': 'rar',
    '.rar': 'rar',
    '.rar5': 'rar',
    '.7z': 'rar',
    '.ace': 'rar',
    '.gz': 'rar',
    '.exe': 'exe',
    '.msi': 'exe',
    '.java': 'programacion',
    '.c': 'programacion',
    '.cpp': 'programacion',
    '.py': 'programacion',
    '.c#': 'programacion',
    '.php': 'programacion',
    '.html': 'programacion',
    '.js': 'programacion',
    '.css': 'programacion',
    'uml': 'diagramaP',
    '.drawio': 'diagramaP'
}

ruta_descargas = "C:\\Users\\zigas\\Downloads\\"

def mover_archivo(origen, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)
    shutil.move(origen, destino)

def ordenar_archivos():
    print("En ejecución...")
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, ext = os.path.splitext(archivo)
        if ext.lower() in ext_carpetas:
            carpeta_destino = ext_carpetas[ext.lower()]
            ruta_destino = os.path.join(ruta_descargas, carpeta_destino)
            archivo_destino = os.path.join(ruta_destino, archivo)
            if os.path.exists(archivo_destino):
                print(f"El archivo {archivo} ya existe en la carpeta {carpeta_destino}")
                respuesta = input("¿Desea reemplazarlo? (s/n): ")
                if respuesta.lower() == "s":
                    os.remove(archivo_destino)
                    mover_archivo(os.path.join(ruta_descargas, archivo), ruta_destino)
            else:
                mover_archivo(os.path.join(ruta_descargas, archivo), ruta_destino)
    print("Fin de la ejecución.")

ordenar_archivos()



"""
import os
import glob
import shutil

while(True):
        
        if os.path.exists("documentos") == True:
            pass
        else: 
            os.mkdir("documentos")
            continue
        
        if os.path.exists("fotos") == True:
            pass
        else:
            os.mkdir("fotos")
            continue
            
        if os.path.exists("videos") == True:
            pass
        else:
            os.mkdir("videos")
            continue
        
        if os.path.exists("otros") == True:
            pass
        else:
            os.mkdir("otros")
            continue
            
        if os.path.exists("musica") == True:
            pass
        else:
            os.mkdir("musica")
        break



# Extensiones de fotos:

png = glob.glob("*.png")
jpg = glob.glob("*.jpg")
jpeg = glob.glob("*.jpeg")

# Extensiones de vídeos:

mp4 = glob.glob("*.mp4")
mkv = glob.glob("*.mkv")
avi = glob.glob("*.avi")
mov = glob.glob("*.mov")
divx = glob.glob("*.divx")

# Extensiones de audios:

wav = glob.glob("*.wav")
mp3 = glob.glob("*.mp3")
aac = glob.glob("*.aac")
aiff = glob.glob("*.aiff")
wma = glob.glob("*.wma")
flv = glob.glob("*.flv")

# Extensiones de documentos:

pdf = glob.glob("*.pdf")
doc = glob.glob("*.doc")
docx = glob.glob("*.docx")
odt = glob.glob("*.odt")
txt = glob.glob("*.txt")

# Extensiones de otros:

py = glob.glob("*.py")
rar = glob.glob("*.rar")
zip = glob.glob("*.zip")
exe = glob.glob("*.exe")
html = glob.glob("*.html")
ppt = glob.glob("*.ppt")
pptx = glob.glob("*.pptx")
tmp = glob.glob("*.tmp")
xlsx = glob.glob("*.xlsx")
xls = glob.glob("*.xls")
dat = glob.glob("*.dat")


#############################################################

# Mover archivos (fotos)
for i in (png):
    shutil.move(i, "fotos")
for i in (jpg):
    shutil.move(i, "fotos")
for i in (jpeg):
    shutil.move(i, "fotos")


# Mover archivos (videos)
for i in (mp4):
    shutil.move(i, "videos")
for i in (mkv):
    shutil.move(i, "videos")
for i in (avi):
    shutil.move(i, "videos")
for i in (mov):
    shutil.move(i, "videos")
for i in (flv):
    shutil.move(i, "videos")
for i in (divx):
    shutil.move(i, "videos")

# Mover archivos (audios)
for i in (mp3):
    shutil.move(i, "musica")
for i in (aac):
    shutil.move(i, "musica")
for i in (wav):
    shutil.move(i, "musica")
for i in (aiff):
    shutil.move(i, "musica")
for i in (wma):
    shutil.move(i, "musica")

# Mover archivos (documentos)
for i in (pdf):
    shutil.move(i, "documentos")
for i in (doc):
    shutil.move(i, "documentos")
for i in (docx):
    shutil.move(i, "documentos")
for i in (txt):
    shutil.move(i, "documentos")
for i in (odt):
    shutil.move(i, "documentos")
for i in (xlsx):
    shutil.move(i, "documentos")
for i in (xls):
    shutil.move(i, "documentos")

# Mover archivos (otros)
for i in (py):
    shutil.move(i, "otros")
for i in (rar):
    shutil.move(i, "otros")
for i in (zip):
    shutil.move(i, "otros")
for i in (html):
    shutil.move(i, "otros")
for i in (ppt):
    shutil.move(i, "otros")
for i in (pptx):
    shutil.move(i, "otros")
for i in (tmp):
    shutil.move(i, "otros")
for i in (dat):
    shutil.move(i, "otros")
"""
