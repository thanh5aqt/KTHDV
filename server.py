import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    print("is running")
    clientsocket, address = s.accept()
    with clientsocket:
        print(f"Connection from {address} has been established!")
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            print(data)
            clientsocket.sendall(data)
    
    
    
    
