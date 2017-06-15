#coding: utf-8

total = 0.0

class vender1:
 def venderProduto(self, listaproduto):

     global total
     global restante
     while True:
         print "====Venda de Produtos====\n"
         nomeProduto = raw_input("Digite o nome do produto: ")
         existe = False
         for i in range(len(listaproduto)):
             if listaproduto[i].getNome() == nomeProduto:
                 existe = True
                 print "%s(%s): R$%.2f" % (listaproduto[i].getNome(), listaproduto[i].getTipo(), listaproduto[i].getPreco())
                 quantidade = int(raw_input("\ndigite a quantidade que deseja vender: "))
                 if quantidade <= 0:
                     print("\nnumero negativo é invalido")
                     continue
                 if listaproduto[i].getQuantidade()>= quantidade:
                     listaproduto[i].setQuantidade(listaproduto[i].getQuantidade() - quantidade)
                     r = listaproduto[i].getPreco() * quantidade
                     total += r
                     print("\ntotal arrecadado: R$%.2f" % (r))
                 else:
                     print "\nNão é possível vender pois não há %s suficiente" %(nomeProduto)

         if existe == False:
             print "%s nao cadastrado no sistema" % (nomeProduto)
             break

         op = raw_input("Deseja vender outro Produto? ")
         if op.upper() == "SIM":
             continue
         elif op.upper() == "NAO":
             break
         else:
             print "Invalido"

     return listaproduto