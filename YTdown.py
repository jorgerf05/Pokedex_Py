from pytube import YouTube
import os

def downloadAudio(url):

    salida = YouTube(url).streams.get_audio_only().download()
    base, ext = os.path.splitext(salida)
    nombre = base + ".mp3"
    os.rename (salida, nombre)
    print("\n¡Descargado!\nNombre del archivo: ",os.path.basename(salida))

def downloadVideo(url):
    salida = YouTube(url).streams.get_highest_resolution().download()
    nombre = os.path.basename(salida)
    print("\n¡Descargado!\nNombre del archivo: "+nombre)

#Inicio

print ("-----Bienvenido a YTdown!-----\n")

while (True):

    print("1) Descargar audio\n2) Descargar audio y video\n")
    opc = int(input("Introduce una opción: "))
    
    match opc:
        case 1:
            downloadAudio(input("Introduce la URL del video: "))

        case 2:
            downloadVideo(input("Introduce la URL del video: "))

    loop = input("\nPresione enter para descargar otro archivo, o introduzca 0 para salir: ")
    if (loop == "0"):
        break
