import socket

HOST = "" #Server address
PORT = 9001 #Server port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(bytes("Sé que no es el canal mas seguro, pero con todo el jaleo que llevamos he perdido la contraseña del servidor... ¿Puedes mandarmela?\n", "utf-8"))
	data = s.recv(1024)
	print(data.decode("utf-8"))

	s.sendall(bytes("La tenía guardada en otro ordenador. Mandamela por aquí mismo.\n", "utf-8"))
	data = s.recv(1024)
	print(data.decode("utf-8"))

	s.sendall(bytes("Gracias, ¿nos vemos el martes como siempre, no?\n", "utf-8"))
	data = s.recv(1024)
	print(data.decode("utf-8"))