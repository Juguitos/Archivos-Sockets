
import socket

# definimos el valor de las variables
IP = socket.gethostbyname(socket.gethostname()) 
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    # inicualizamos la conexion
    print("[+] Iniciando la conexion.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    # ponemos el archivo en escucha
    server.listen()
    print("[+] El servidor esta en escucha.")

    while True:
        # aceptamos la conexiones posibles
        conn, addr = server.accept()
        print(f"[+] {addr} se ha conectado.")
        
        # mandamos el archivo hacia el cliente
        filename = conn.recv(SIZE).decode(FORMAT)
        file = open(filename, "w")
        conn.send("Archivo recivido.".encode(FORMAT))
        data = conn.recv(SIZE).decode(FORMAT)
        file.write(data)
        conn.send("File data recivida".encode(FORMAT))

        file.close()

        conn.close()
        print(f"[+] {addr} se ha desconectado.")

if __name__ == "__main__":
    main()
