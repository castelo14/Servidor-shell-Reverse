import socket
import subprocess

ip = '127.0.0.1'
port = 2222

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conex = (ip,port)
s.bind(conex)

s.listen(5)

while(True):
  try:
    con,addr = s.accept()
    con.send('Bem vindo ao servidor tcp\n')
    con.send('\nshell:')
    log = open('log.txt','a')
   while True: 
     term = subprocess.Popen(str(con.recv(1024)),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
     m = term.communicate()
     log.write(str(con.recv(1024)))
     log.close()
     con.send(m[0]+'\n')
  except Exception as e:
    break     
s.close()
