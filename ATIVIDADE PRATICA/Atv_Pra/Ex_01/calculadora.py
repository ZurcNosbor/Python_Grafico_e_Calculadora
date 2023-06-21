#CLASSE CALCULADORA
#IMPORT PARA REALIZAR OS CALCULOS MATEMATICOS
import math

#CLASSE CALCULADORA E SEUS METODOS COM AS OPERAÇOES MATEMATICAS
class Calculadora:

    #METODO DE INICIALIZAÇÃO DA CLASSE
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.res = 0

    def somar(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.res = self.n1 + self.n2
        return self.res

    def subtrair(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.res = self.n1 - self.n2
        return self.res

    def multiplicar(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.res = self.n1 * self.n2
        return self.res

    def dividir(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.res = self.n1 / self.n2
        return self.res

    def expoente(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.res = self.n1 ** self.n2
        return self.res

    def resto(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.res = self.n1 % self.n2
        return self.res

    def raiz(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.res = math.sqrt(self.n1 + self.n2)
        return self.res
