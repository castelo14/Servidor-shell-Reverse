var = []
while True:
   msg = raw_input('escreva a sua mensagem: ')
   if msg:
      var.append(msg)
   else:
      break

#for valor in var:
 #   print var
  #  if valor == 'belo':
   #      print ("As musicas dele são ruis") 
    #      
     #    #ver se existe um item na lista

lista = [1,2,3,4,5,6,7,8]
lista2 = [5,6,8]

for i in range(8):
   if lista2 in lista:
      c+=1
      print 'existe o valor 3 na lista'
      print ("existem %d " % c)
