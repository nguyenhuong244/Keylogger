import socket

ip = '192.168.1.12'
port = 5678

print('Tao socket moi')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))
    print('May chu dang nghe...')
    s.listen(10)
    conn, addr = s.accept()
    print(f'Ket noi tu {addr} duoc thanh lap!!')
    with conn:
        i=1
        l = conn.recv(1024)
        while (l):
            with open('file'+ str(i)+".txt",'wb') as f:
                f.write(l)
            i=i+1
            l = conn.recv(1024)