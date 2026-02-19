#Função para números específicos
def primo_Sem_Intervalo():
    #Estrutura de repetição para o usuário inserir um número válido
    while True:

        #Caso o usuário insira algo que não seja um número
        try:
            numero = int(input("Qual número você gostaria de saber se primo? "))
            
        except ValueError:
            print("Insira um valor válido!!")
            continue
        
        #Verificador se o número é menor ou o mesmo que o número "1"
        if numero <= 1:
            print(f"O número '{numero}', não é primo!!")
            
        else:
            primo = True
            
            #Laço de repetição para 
            for d in range(2, numero):
                if numero % d == 0:
                    primo = False
                    break
                    
            if primo:
                print(f"O número '{numero}' é primo")
            
            else:
                print(f"O número '{numero}' não é primo")
                    
            
        print("")
        break


def primo_intervalo():
    intervalo = int(input("Até qual número você quer saber se é número primo? "))

    listaNumeros = range(1, intervalo +1)

    for numero in listaNumeros:
        lista = []
            
        if numero <= 1:
            print(f"O número '{numero}' não é primo!!")
                
        else:
            for n in listaNumeros:
                if numero % n == 0:
                    lista.append(n)
                                
                    if len(lista) > 2 and n == numero:
                        print(f"O número '{numero}' não é primo")
                                            
                    elif len(lista) <= 2 and n == numero:
                        print(f"O número '{numero}' é primo")
            
    print("")
            
def menu():
    while True:
        try:
            escolha = int(input("Escolha entre [1] e [2]\n[1]Número específico\n[2]Com intervalo de números\n-> "))
            
        except ValueError:
            print("Insira um valor válido!!\n")
            continue

        if escolha == 1:
            primo_Sem_Intervalo()
            
        elif escolha == 2:
            primo_intervalo()

        else:
            print("Insira um valor válido!!")
            
        
        sair = input("Quer continuar?\n[S]Sim\n[N]Não\n-> ").lower()
        
        if sair == 's' or sair == 'sim':
            menu()

        elif sair == 'n' or sair == 'não':
            break
            
        else:
            print("Insira 'S'/'Sim' ou 'N'/'Não'")
            
        
menu()