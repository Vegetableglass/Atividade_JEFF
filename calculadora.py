import random, operator
rodar = True
Historico = []
Pontos = [0]
Partidas_jogadas = [0]
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
                print(f"{50*"-"}\n{Historico}")
            else:
                print(f"{50*"-"}\nHistorico vazio.")   

        def cl():
            Historico.clear()
            print(f"{50*"-"}\nHistorico limpo.")

        def ci():
            op = random.choice(["+","-","*","/","**","%"])
            if op == "**":
                va = random.randint(-100, 100)
                vb = random.randint(-10, 10)

            elif op in ["/","%"]:
                va =  random.randint(-1000000, 1000000)
                vb = random.randint(-1000000, 1000000)

            else:
                va = round(random.uniform(-1000000, 1000000),2)
                vb = round(random.uniform(-1000000, 1000000),2)
                
            opf = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv,
                "**": operator.pow,
                "%": operator.mod,
            }
            resposta = float(input(f"{50*"-"}\nResolva: {va} {op} {vb}\n{50*"-"}\nDigite aqui(Apenas 2 casas decimais serão consideradas após o ponto, e é necessário arredondar):"))
            resposta_certa = round(opf[op](va,vb),2)
            if resposta == resposta_certa:
                print(f"{50*"-"}\nVocê acertou e ganhou 1 ponto!")
                Pontos[0] += 1
                Partidas_jogadas[0] += 1
            else:
                print(f"{50*"-"}\nVocê errou e não ganhou nenhum ponto...O resultado era {resposta_certa}.")
                Partidas_jogadas[0] += 1

        def verp():
            pontos = Pontos[0]
            partidas = Partidas_jogadas[0]
            print(f"{50*"-"}\nVocê tem {pontos} ponto(s) e {partidas} partida(s) jogada(s).")
            
        operacao = int(input(f"{50*"-"}\nEscolha uma operação:\n1:Soma\n2:Subtração\n3:Multiplicação\n4:Divisão\n5:Potência\n6:Resto da Divisão\n7:Historico\n8:Limpar historico\n9:Jogo da calculadora inversa!\n10:Ver pontos da calculadora inversa\n11:Para sair da calculadora\nDigite aqui:"))
        if operacao in [1,2,3,4,5,6]:
                a = float(input("Escolha um número para realizar a operações(Digite números decimais com . ao inves de ,):"))
                b = float(input("Escolha outro número para realizar a operações(Digite números decimais com . ao inves de ,):"))
            
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
            ci()

        elif operacao == 10:
            verp()

        elif operacao == 11:
            rodar = False
            print(f"{50*"-"}\nPrograma encerrado.\n{50*"-"}")

    except ValueError:
        print(f"{50*"-"}\nPorfavor pare de tentar quebrar o codigo, tente novamente.")
    except OverflowError:
        print(f"{50*"-"}\nNúmero digitado é grande demais para ser processado.")