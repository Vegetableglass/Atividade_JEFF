rodar = True
Historico = []  
while rodar == True: 
    try:
        def soma(a,b):
            resultado = a + b
            print(f"{50*"-"}\nO resultado da soma entre {a} e {b} é {resultado}")
            Historico.append(f"{resultado} = {a} + {b}")

        def sub(a,b):
            resultado = a - b
            print(f"{50*"-"}\nO resultado da subtração entre {a} e {b} é {resultado}")
            Historico.append(f"{resultado} = {a} - {b}")

        def mult(a,b):
            resultado = a * b
            print(f"{50*"-"}\nO resultado da multiplicação entre {a} e {b} é {resultado}")
            Historico.append(f"{resultado} = {a} * {b}")

        def div(a,b):
            if b == 0 :
                print(f"{50*"-"}\nNão é possível dividir por zero, tente novamente.")
            else:
                resultado = a / b 
                Historico.append(f"{resultado} = {a} / {b}")
                print(f"{50*"-"}\nO resultado da divisão entre {a} e {b} é {resultado}")
        
        def pot(a,b):
            resultado = a ** b
            Historico.append(f"{resultado} = {a} ** {b}")
            print(f"{50*"-"}\nO resultado de {a} elevado a {b} é {resultado}")

        def rest(a,b):
            if b == 0:
                print(f"{50*"-"}\nNão é possível dividir por zero, tente novamente.")
            else:
                resultado = a % b
                Historico.append(f"{resultado} = {a} % {b}")
                print(f"{50*"-"}\nO resto da divisão entre {a} e {b} é {resultado}")
        
        def hist():
            if len(Historico) > 0:
                print(Historico)
            else:
                print(f"{50*"-"}\nHistorico vazio.")   

        def cl():
            Historico.clear()
            print(f"{50*"-"}\nHistorico limpo.") 
            
        operacao = (int(input(f"{50*"-"}\nEscolha uma operação:\n1:Soma\n2:Subtração\n3:Multiplicação\n4:Divisão\n5:Potência\n6:Resto da Divisão\n7:Historico\n8:Limpar historico\n9:Para sair dessa calculadora\nDigite aqui:")))
        if operacao in [1,2,3,4,5,6]:
                a = (float(input("Escolha um número para realizar a operações(Digite números decimais com . ao inves de ,):")))
                b = (float(input("Escolha outro número para realizar a operações(Digite números decimais com . ao inves de ,):")))
            
                if operacao == 1:
                    soma(a,b)
                
                elif operacao == 2:
                    sub(a,b)
                
                elif operacao == 3:
                    mult(a,b)

                elif operacao == 4:
                    div(a,b)
                
                elif operacao == 5:
                    pot(a,b)

                elif operacao == 6:
                    rest(a,b)
        
        elif operacao == 7:
            hist()

        elif operacao == 8:
            cl()       

        elif operacao == 9:
            c = float(input("Digite o resultado aqui:"))

        elif operacao == 10:
            rodar = False
            print(f"{50*"-"}\nPrograma encerrado.\n{50*"-"}")

    except ValueError:
        print(f"{50*"-"}\nPorfavor pare de tentar quebrar o codigo, tente novamente.")