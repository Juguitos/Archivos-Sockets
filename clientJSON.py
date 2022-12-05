
import socket
import os
import pathlib
import json

# definimos el valor de las variables
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():

    # vemos el contenido del directorio actual...
    print("El contenido actual del directorio es:")
    directorio2 = pathlib.Path("/home/luisda/Protocolos/ProyectoArchivos/")
    for fichero2 in directorio2.iterdir():
        print(fichero2.name)
    print("*********************************")

    # pedimos por teclado el nombre del usuario y la contraseña
    usuario_tec = input("Ingresa nombre del usuario: ")
    pass_tec = input("Ingresa la contraseña del usuario: ")

    # creamos una bandera para saber si existe el usuario
    exist = False
    
    # abrimos el archivo json
    f = open('cuentas.json')
    datos = json.load(f)

    # recorremos el los datos del archivo json
    for i in datos['usuarios']:
        # verificamos si el nombre del usuario mas la contraseña es valida
        if i["usuario"] == usuario_tec and i["pass"] == pass_tec:
            exist = True
            dire = i["dir"]
            print("El directorio del usuario es:" , dire)
    print()
    print("***********************************")
    # activamos la bandera
    if exist:
        print("Usuario y contraseña correctos")
    else:
        print("Usuario y/o contraseña incorrectos")


    # recorremos el directorio para poder mostrar el contenido
    directorio = pathlib.Path(dire)
    for fichero in directorio.iterdir():
        print(fichero.name)

    # pedimos en pantalla el archivo
    print("***********************************")
    print()
    archivo_tec = input("Que archivo quieres: ")
    # concatenamos el directorio con el archivo
    dire_archivo = dire + archivo_tec



    # inicualizamos el socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    
    # recibios el archivo
    file = open(dire_archivo , "r")
    data = file.read()
    client.send(archivo_tec.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    file.close()
    f.close()
    client.close()

    # verificamos que en el directorio actual se pasara el archivo
    print("\n\n\n")
    directorio3 = pathlib.Path("/home/luisda/Protocolos/ProyectoArchivos/")
    for fichero3 in directorio3.iterdir():
        print(fichero3.name)


if __name__ == "__main__":
    main()
