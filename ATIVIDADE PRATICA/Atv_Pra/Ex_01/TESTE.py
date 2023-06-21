#IMPORTAR DA CLASSE CALCULADORA
from calculadora import Calculadora

class Principal:

    #CONSTRUTOR DA CLASSE PRINCIPAL
    #INICIALIZA A INSTANCIA DA CLASSE CALCULADORA COMO UM ATRIBUTO DA CLASSE PRINCIPAL
    def __init__(self):
        self.calculadora = Calculadora()

    #METODO PARA REALIZAR OS CALCULOS
    def executar_calculos(self):

        # MENU INICIAL
        print("SEJA BEM VINDO A CALCULADORA!!!!!")
        print("1 - ADIÇÃO")
        print("2 - SUBTRAÇÃO")
        print("3 - MULTIPLICAÇÃO")
        print("4 - DIVISÃO")
        print("5 - POTENCIAÇÃO")
        print("6 - MÓDULO (RESTO)")
        print("7 - RAÍZ QUADRADA (SOMA DOS DOIS NÚMEROS)")
        print("0 - SAIR")

        # LAÇO DE REPETIÇÃO PARA A ESCOLHA DA OPÇÃO
        while True:
            op = input("ESCOLHA UMA DAS OPÇÕES PARA REALIZAR UMA OPERAÇÃO: ")

            if op == '1':

                #LAÇO DE REPETIÇÃO PARA NÚMERO VÁLIDO
                while True:
                    num1 = input("DIGITE O PRIMEIRO NÚMERO: ")
                    if num1.isdigit():
                        num1 = int(num1)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                while True:
                    num2 = input("DIGITE O SEGUNDO NÚMERO: ")
                    if num2.isdigit():
                        num2 = int(num2)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                resultado = self.calculadora.somar(n1=num1, n2=num2)
                print("RESULTADO DA SOMA:", resultado)

            if op == '2':

                # LAÇO DE REPETIÇÃO PARA NÚMERO VÁLIDO
                while True:
                    num1 = input("DIGITE O PRIMEIRO NÚMERO: ")
                    if num1.isdigit():
                        num1 = int(num1)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                while True:
                    num2 = input("DIGITE O SEGUNDO NÚMERO: ")
                    if num2.isdigit():
                        num2 = int(num2)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                resultado = self.calculadora.subtrair(n1=num1, n2=num2)
                print("RESULTADO DA SUBTRAÇÃO:", resultado)

            if op == '3':

                # LAÇO DE REPETIÇÃO PARA NÚMERO VÁLIDO
                while True:
                    num1 = input("DIGITE O PRIMEIRO NÚMERO: ")
                    if num1.isdigit():
                        num1 = int(num1)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                while True:
                    num2 = input("DIGITE O SEGUNDO NÚMERO: ")
                    if num2.isdigit():
                        num2 = int(num2)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                resultado = self.calculadora.multiplicar(n1=num1, n2=num2)
                print("RESULTADO DA MULTIPLICAÇÃO:", resultado)

            if op == '4':

                print("***DIGITE OS DOIS ÚLTIMOS NÚMEROS DO SEU RU***")
                # LAÇO DE REPETIÇÃO PARA NÚMERO VÁLIDO
                while True:
                    num1 = input("DIGITE O PRIMEIRO NÚMERO: ")
                    if num1.isdigit():
                        num1 = int(num1)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                while True:
                    num2 = input("DIGITE O SEGUNDO NÚMERO: ")
                    if num2.isdigit():
                        num2 = int(num2)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                resultado = self.calculadora.dividir(n1=num1, n2=num2)
                print("RESULTADO DA DIVISÃO:", resultado)

            if op == '5':

                print("***DIGITE OS DOIS ÚLTIMOS NÚMEROS DO SEU RU***")
                # LAÇO DE REPETIÇÃO PARA NÚMERO VÁLIDO
                while True:
                    num1 = input("DIGITE O PRIMEIRO NÚMERO: ")
                    if num1.isdigit():
                        num1 = int(num1)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                while True:
                    num2 = input("DIGITE O SEGUNDO NÚMERO: ")
                    if num2.isdigit():
                        num2 = int(num2)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                resultado = self.calculadora.expoente(n1=num1, n2=num2)
                print("RESULTADO DA POTENCIAÇÃO:", resultado)

            if op == '6':

                print("***DIGITE OS DOIS ÚLTIMOS NÚMEROS DO SEU RU***")
                # LAÇO DE REPETIÇÃO PARA NÚMERO VÁLIDO
                while True:
                    num1 = input("DIGITE O PRIMEIRO NÚMERO: ")
                    if num1.isdigit():
                        num1 = int(num1)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                while True:
                    num2 = input("DIGITE O SEGUNDO NÚMERO: ")
                    if num2.isdigit():
                        num2 = int(num2)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                resultado = self.calculadora.resto(n1=num1, n2=num2)
                print("RESULTADO DO MÓDULO(RESTO):", resultado)

            if op == '7':

                print("***DIGITE OS DOIS ÚLTIMOS NÚMEROS DO SEU RU***")
                # LAÇO DE REPETIÇÃO PARA NÚMERO VÁLIDO
                while True:
                    num1 = input("DIGITE O PRIMEIRO NÚMERO: ")
                    if num1.isdigit():
                        num1 = int(num1)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                while True:
                    num2 = input("DIGITE O SEGUNDO NÚMERO: ")
                    if num2.isdigit():
                        num2 = int(num2)
                        break
                    else:
                        print("Erro: Digite um número válido!")

                resultado = self.calculadora.raiz(n1=num1, n2=num2)
                print("RESULTADO DA RAIZ(SOMA DOS DOIS NÚMEROS DIGITADOS):", resultado)

            # OPÇÃO 0: ENCERRA O PROGRAMA
            elif op == '0':
                print('Encerrando Programa...')
                return

            # OPÇÃO INVÁLIDA
            elif not op.isdigit() or int(op) not in range(8):
                print('Erro: Digite uma opção válida!!')

# INSTANCIA DA CLASSE PRINCIPAL
p = Principal()

# EXECUÇÃO DOS CALCULOS
p.executar_calculos()
