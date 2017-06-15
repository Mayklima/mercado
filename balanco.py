#coding: utf-8

total = 0.0

class balanco1:
 def imprimirBalanco(self, listaproduto):

     total_arrecadado = 0.0

     print "==== Impressao de Balanco ====\n"
     print "Produtos cadastrados: \n"
     for i in range(len(listaproduto)):
         print "%d) %s(%s): R$%.2f" %(i+1,listaproduto[i].getNome(), listaproduto[i].getTipo(), listaproduto[i].getPreco())
         print"\tRestante: %d" %(listaproduto[i].getQuantidade())
         total_arrecadado += listaproduto[i].getPreco() * listaproduto[i].getQuantidade()
     print "Total arrecadado em vendas: R$%.2f\n" %(total)
     print "Total que pode ser arrecadado : R$ %.2f" %(total_arrecadado)

     return listaproduto