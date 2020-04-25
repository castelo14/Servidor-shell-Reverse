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
    con.send('bem vido ao servidor TCP\n')
    con.send('>>>')
    msg = con.recv(1024)
    print 'conexao %s ' % msg
  except Exception as e:
    con.close()     
    break
s.close()
