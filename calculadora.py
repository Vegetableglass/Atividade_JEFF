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
        
        def hist():
            if len(Historico) > 0:
                print(Historico)
            else:
                print(f"{50*"-"}\nHistorico vazio.")    
            
        operacao = (int(input(f"{50*"-"}\nEscolha uma operação:\n1:Soma\n2:Subtração\n3:Multiplicação\n4:Para ver historico\n5:Para sair dessa calculadora\nDigite aqui:")))
        if operacao in [1,2,3]:
                a = (float(input("Escolha um número para realizar a operações(Digite números decimais com . ao inves de ,):")))
                b = (float(input("Escolha outro número para realizar a operações(Digite números decimais com . ao inves de ,):")))
            
                if operacao == 1:
                    soma(a,b)
                
                elif operacao == 2:
                    sub(a,b)
                
                elif operacao == 3:
                    mult(a,b)    
                
        elif operacao == 4:
            hist()

        elif operacao == 5:
            rodar = False
            print(f"{50*"-"}\nPrograma encerrado.\n{50*"-"}")

    except ValueError:
        print(f"{50*"-"}\nPorfavor pare de tentar quebrar o codigo, tente novamente.")