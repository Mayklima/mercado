#coding: utf-8

from cadastrar import cadastrar1
from vender import vender1
from  balanco import balanco1

class menu1:
    def menuPrincipal(self):
        self.lista = []
        cadastro = cadastrar1()
        venda = vender1()
        balanc = balanco1()

        while True:
            print "==== Bem vindo(a) ao mercado====\n"
            print "Cadastrar um Produto: 1"
            print "Vender um Produto: 2"
            print "Imprimir Balanço: 3"
            print "Sair: 4"
            op = raw_input("\nOpcao: ")

            if op == "1":
                '''Cadastro dos produtos'''
                self.lista = cadastro.cadastrarProduto(self.lista)
            elif op == "2":
                '''Vender os produtos'''
                self.lista = venda.venderProduto(self.lista)
            elif op == "3":
                '''Imprimir Balanço'''
                self.lista = balanc.imprimirBalanco(self.lista)
            elif op == "4":
                print "\nObrigado!\nVolte Sempre!"
                break
            else:
                print "\nOpcao Invalida!!!\n"


me = menu1()
me.menuPrincipal()