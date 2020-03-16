import socket

class Student:
    def __init__(self, ten, mssv, email, lop, ns, que):
        self.ten = ten
        self.mssv = mssv
        self.email = email
        self.lop = lop
        self.ns = ns
        self.que = que

studentlist = []
studentlist.append(Student("Thanh", 17021016, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Thang", 17021017, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Thinh", 17021018, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Tung", 17021019, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Diep", 17021020, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Hanh", 17021021, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Tuan", 17021022, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Khanh", 17021023, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Quang", 17021024, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Quan", 17021025, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Van Anh", 17021026, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Thinh", 17021027, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Thanh", 17021028, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Thang", 17021029, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))
studentlist.append(Student("Thinh", 17021030, "123@gmail.com", "IE3", "20/07/1999", "HaNoi"))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

count = 0;

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    msg = clientsocket.recv(1024)
    try:
        t = int(msg)
        for st in studentlist:
            if t == st.mssv:
                count+=1
                clientsocket.send(bytes("Ho va ten:","utf-8"))
                clientsocket.send(bytes(st.ten,"utf-8"))
                clientsocket.send(bytes(" Email:","utf-8"))
                clientsocket.send(bytes(st.email,"utf-8"))
                clientsocket.send(bytes(" Lop:","utf-8"))
                clientsocket.send(bytes(st.lop,"utf-8"))
                clientsocket.send(bytes(" Ngay Sinh:","utf-8"))
                clientsocket.send(bytes(st.ns,"utf-8"))
                clientsocket.send(bytes(" Que:","utf-8"))
                clientsocket.send(bytes(st.que,"utf-8"))
        if count == 0:
            clientsocket.send(bytes("Khong tim thay sinh vien", "utf-8"))
    except ValueError:
        clientsocket.send(bytes("Mssv vua nhap khong dung moi nhap lai", "utf-8"))
