#coding: utf-8

from produto import produto1


total = 0.0

class cadastrar1:
 def cadastrarProduto(self,listaproduto):

     while True:
         print "====Cadastros de Produtos====\n"
         nomeProduto = raw_input("Digite o nome do produto: ")
         precoProduto = float(raw_input("Digite o preço unitário do produto: "))
         if precoProduto <= 0:
             print "numero negativo é invalido"
             continue
         tipoProduto = raw_input("Digite o tipo do produto: ")
         quantidadeProduto = int(raw_input("Digite a quantidade no estoque: "))

         existe = False
         if len(listaproduto) == 0:
             produ = produto1(nomeProduto, precoProduto, tipoProduto, quantidadeProduto)
             listaproduto.append(produ)
             print "\n%i %s(s) cadastrado(s) com sucesso.\n" % (quantidadeProduto, nomeProduto)
         else:
             for i in range(len(listaproduto)):
                 if listaproduto[i].getNome() == nomeProduto:
                     existe = True
                     print "Produto ja cadastrado"

             if existe == False:
                 produ = produto1(nomeProduto, precoProduto, tipoProduto, quantidadeProduto)
                 listaproduto.append(produ)
                 print "\n%d %s cadastrado(s) com sucesso.\n"%(quantidadeProduto,nomeProduto)


         op1 = raw_input("Deseja cadastrar outro produto? ")

         if op1.upper() == "SIM":
             continue
         elif op1.upper() == "NAO":
             break
         else:
             print "Invalido!"

     return listaproduto