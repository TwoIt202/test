import socket

ip = socket.gethostbyname(socket.gethostname())
port = 8000

server = socket.socket()

server.bind((ip, port))
server.listen(0)
conn, add = server.accept()

client = conn.recv(1024).decode()
name = input("Enter your name: ")
server.send(name.encode())
print(f"{client} connected to server!")

while True:
  message = input("You: ")
  message_send = f"{name}: {message}"
  server.send(message_send.encode())
  
  message = conn.recv(1024).decode()
  print(f"{client}: {message}")
