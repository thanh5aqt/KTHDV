import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
t = input("Moi nhap mssv:")
s.send(bytes(t, "utf-8"))
msg = s.recv(1024)
print(msg.decode("utf-8"))
