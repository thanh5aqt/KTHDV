import socket


HOST=socket.gethostname()
PORT=1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        
        temp=input()
        
        s.sendall(b"send thu")
        data = s.recv(1024)
        print('DA nhan', repr(data))






        