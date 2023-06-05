# echo-server.py

import socket

HOST = "192.168.1.100"  # Standard loopback interface address (localhost)
PORT = 9001  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        print(data.decode("utf-8"))
        conn.sendall(bytes("¿Estas de broma no? Ya te la mande otra vez la semana pasada\n", "utf-8"))
        data = conn.recv(1024)
        print(data.decode("utf-8"))
        conn.sendall(bytes("Lo que hay que ver, encima por un canal no seguro... Ahí la llevas: cobra{st41king_thr0ugh_th3_w1r3}\n", "utf-8"))
        data = conn.recv(1024)
        print(data.decode("utf-8"))
        conn.sendall(bytes("Si... Pero como alguien pille esto, te vas a la calle.\n", "utf-8"))
    s.close()