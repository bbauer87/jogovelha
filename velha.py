import random
import time

casa7=" "; casa8=" "; casa9=" "
casa4=" "; casa5=" "; casa6=" "
casa1=" "; casa2=" "; casa3=" "

fim=0      ## variável que indica para certos loops que o jogo está encerrado
quemjoga=0 ## == 1 jogador 1 ||| == 2 jogador 2
jogadas=1  ## contador de jogadas
temcpu=0   ## == 1 caso opção seja humano vs cpu ou cpu vs cpu
cpucpu=0   ## == 1 caso opção seja cpu vs cpu

def menu(): ## menu do jogo
    global temcpu,cpucpu
    while True:
        opcao=input("\nO jogo tem três opções:\n\n [[1]] - Humano VS Humano\n\n [[2]] - Humano VS CPU\n\n [[3]] - CPU VS CPU (modo tédio)\n\n [[4]] - Sair\n\nQual a opção?  ")
        if opcao.isdigit() is False:
            print("\nESCOLHA uma opção!\n")
            continue
        opcao=int(opcao)
        if opcao<1 or opcao>4:
            print("\nOpção inválida! Tente de novo!\n")
            continue
        if opcao==4:
            print("Adiós!")
            quit()
        if opcao==1:            temcpu=0; cpucpu=0
        if opcao==2:            temcpu=1; cpucpu=0
        if opcao==3:            temcpu=1; cpucpu=1            
        sorteio()
        return

def tabuleiro():
    print(f"""                  Posições
 {casa7} | {casa8} | {casa9}       7 | 8 | 9  
---+---+---     ---+---+---
 {casa4} | {casa5} | {casa6}       4 | 5 | 6 
---+---+---     ---+---+---
 {casa1} | {casa2} | {casa3}       1 | 2 | 3  
""")

def verifjogs(): ## verifica de quem é a vez de jogar e invoca respectiva função
    print(f"Jogadas: {jogadas-1}\n")
    if quemjoga==1: jogador1()
    else:           jogador2()
    return

def sorteio():
    global quemjoga
    
    ## gambiarras para verificar qual nomenclatura dos jogadores, humanos ou CPU's, a fim de indicar quem começa o jogo
    if temcpu==0:               pos2="Jogador 2"
    if temcpu==1 and cpucpu==0: pos2="CPU"
    if cpucpu==0:               pos="Jogador 1"
    if cpucpu==1:               pos="CPU 1"; pos2="CPU 2"
    #########################################################
    
    for cont in range(1234):
        quemjoga=random.randint(1,2)
    print("\n"+"#"*44)
    if quemjoga==1:        print(f"\nSorteio realizado! {pos} começa!\n")
    if quemjoga==2:        print(f"\nSorteio realizado! {pos2} começa!\n")
    print("#"*44+"\n")
    return

def jogador1():
    global quemjoga,jogadas
    global casa1,casa2,casa3,casa4,casa5,casa6,casa7,casa8,casa9

    ## gambiarras para verificar qual nomenclatura do jogador 1, humano ou CPU, a fim de indicar se jogou em posição válida ou ocupada
    if cpucpu==0:
        pos="Jogador 1 - X - tentou, mas";    pos1="Jogador 1 jogou na posição   "
    if cpucpu==1:
        pos="CPU 1 - X - tentou, mas";        pos1="CPU 1 - X - jogou na posição "
    #########################################################
        
    while True:
        if cpucpu==1: ## se o modo de jogo é CPU vs CPU, random decide a jogada
            casa=random.randint(1,9)
            
        if cpucpu==0:
            casa=input("Jogador 1 - X - Qual posição? ")
            if casa.isdigit() is False: ## impede o usuário de inserir apenas enter, espaço em branco, etc...
                print("\nESCOLHA uma posição!\n")
                continue
            casa=int(casa)
            if casa<1 or casa>9:
                print("\nPosição inválida! Tente de novo!\n")
                continue
            
        if casa==1:
            if casa1.isalpha(): ## verifica se a casa escolhida está ocupada
                print(f"\n{pos} Posição 1 está ocupada!\n")
                continue
            else:
                casa1="X"
                if cpucpu==1:                              
                    print("CPU 1 - X - está pensando . . . ")
                    velha(casa)
        elif casa==2:
            if casa2.isalpha():
                print(f"\n{pos} Posição 2 está ocupada!\n")
                continue
            else:
                casa2="X"
                if cpucpu==1:                                
                    print("CPU 1 - X - está pensando . . . ")
                    velha(casa)
        elif casa==3:
            if casa3.isalpha():
                print(f"\n{pos} Posição 3 está ocupada!\n")
                continue
            else:
                casa3="X"
                if cpucpu==1:                               
                    print("CPU 1 - X - está pensando . . . ")
                    velha(casa)
        elif casa==4:
            if casa4.isalpha():
                print(f"\n{pos} Posição 4 está ocupada!\n")
                continue
            else:
                casa4="X"
                if cpucpu==1:                              
                    print("CPU 1 - X - está pensando . . . ")
                    velha(casa)
        elif casa==5:
            if casa5.isalpha():
                print(f"\n{pos} Posição 5 está ocupada!\n")
                continue
            else:
                casa5="X"
                if cpucpu==1:                             
                    print("CPU 1 - X - está pensando . . . ")
                    velha(casa)
        elif casa==6:
            if casa6.isalpha():
                print(f"\n{pos} Posição 6 está ocupada!\n")
                continue
            else:
                casa6="X"
                if cpucpu==1:                              
                    print("CPU 1 - X - está pensando . . . ")
                    velha(casa)
        elif casa==7:
            if casa7.isalpha():
                print(f"\n{pos} Posição 7 está ocupada!\n")
                continue
            else:
                casa7="X"
                if cpucpu==1:                                
                    print("CPU 1 - X - está pensando . . . ")
                    velha(casa)
        elif casa==8:
            if casa8.isalpha():
                print(f"\n{pos} Posição 8 está ocupada!\n")
                continue
            else:
                casa8="X"
                if cpucpu==1:                              
                    print("CPU 1 - X - está pensando . . . ")
                    velha(casa)
        elif casa==9:
            if casa9.isalpha():
                print(f"\n{pos} Posição 9 está ocupada!\n")
                continue
            else:
                casa9="X"
                if cpucpu==1:                                
                    print("CPU 1 - X - está pensando . . . ")
                    velha(casa)
        print("-"*35);        print(pos1, casa);        print("-"*35+"\n")
        jogadas+=1
        quemjoga=2 ## passa a vez para o jogador 2
        tabuleiro()
        verif()
        return

def jogador2():
    global quemjoga,jogadas
    global casa1,casa2,casa3,casa4,casa5,casa6,casa7,casa8,casa9

    ## gambiarras para verificar qual nomenclatura do jogador 2, humano ou CPU, a fim de indicar se jogou em posição válida ou ocupada    
    if cpucpu==0: ## modo humano vs humano
        quem=0
        pos="Jogador 2 - O - tentou, mas"
        pos1="Jogador 2 jogou na posição   "
    if temcpu==1 and cpucpu==1: ## modo cpu vs cpu
        quem="CPU 2 - O -"
        pos="CPU 2 - O - tentou, mas"
        pos1="CPU 2 - O - jogou na posição   "
    if temcpu==1 and cpucpu==0: ## modo humano vs cpu
        quem="CPU - O -"
        pos="CPU - O - tentou, mas"
        pos1="CPU - O - jogou na posição   "
    #########################################################
        
    while True:
        if temcpu==1: ## se o modo de jogo é humano vs CPU ou CPU vs CPU, random decide a jogada
            casa=random.randint(1,9)
            
        if temcpu==0 and cpucpu==0:
            casa=input("Jogador 2 - O - Qual posição? ")
            if casa.isdigit() is False:
                print("\nESCOLHA uma posição!\n")
                continue
            casa=int(casa)
            if casa<1 or casa>9:
                print("\nPosição inválida! Tente de novo!\n")
                continue
            
        if casa==1:
            if casa1.isalpha():
                print(f"\n{pos} Posição 1 está ocupada!\n")
                continue
            else:
                casa1="O"
                if temcpu==1 or cpucpu==1:                                
                    print(f"{quem} está pensando . . . ")
                    velha(casa)
        elif casa==2:
            if casa2.isalpha():
                print(f"\n{pos} Posição 2 está ocupada!\n")
                continue
            else:
                casa2="O"
                if temcpu==1 or cpucpu==1:                                
                    print(f"{quem} está pensando . . . ")
                    velha(casa)
        elif casa==3:
            if casa3.isalpha():
                print(f"\n{pos} Posição 3 está ocupada!\n")
                continue
            else:
                casa3="O"
                if temcpu==1 or cpucpu==1:                                
                    print(f"{quem} está pensando . . . ")
                    velha(casa)
        elif casa==4:
            if casa4.isalpha():
                print(f"\n{pos} Posição 4 está ocupada!\n")
                continue
            else:
                casa4="O"
                if temcpu==1 or cpucpu==1:                                
                    print(f"{quem} está pensando . . . ")
                    velha(casa)
        elif casa==5:
            if casa5.isalpha():
                print(f"\n{pos} Posição 5 está ocupada!\n")
                continue
            else:
                casa5="O"                               
                if temcpu==1 or cpucpu==1:                                
                    print(f"{quem} está pensando . . . ")
                    velha(casa)
        elif casa==6:
            if casa6.isalpha():
                print(f"\n{pos} Posição 6 está ocupada!\n")
                continue
            else:
                casa6="O"
                if temcpu==1 or cpucpu==1:                                
                    print(f"{quem} está pensando . . . ")
                    velha(casa)
        elif casa==7:
            if casa7.isalpha():
                print(f"\n{pos} Posição 7 está ocupada!\n")
                continue
            else:
                casa7="O"
                if temcpu==1 or cpucpu==1:                                
                    print(f"{quem} está pensando . . . ")
                    velha(casa)
        elif casa==8:
            if casa8.isalpha():
                print(f"\n{pos} Posição 8 está ocupada!\n")
                continue
            else:
                casa8="O"
                if temcpu==1 or cpucpu==1:                                
                    print(f"{quem} está pensando . . . ")
                    velha(casa)
        elif casa==9:
            if casa9.isalpha():
                print(f"\n{pos} Posição 9 está ocupada!\n")
                continue
            else:
                casa9="O"
                if temcpu==1 or cpucpu==1:                                
                    print(f"{quem} está pensando . . . ")
                    velha(casa)
        print("-"*35);        print(pos1, casa);        print("-"*35+"\n")
        jogadas+=1
        quemjoga=1 ## passa a vez para o jogador 1
        tabuleiro()
        verif()
        return                
                    
def verif(): ## verifica se alguém ganhou após cada jogada

    ## gambiarra para nomenclaturas
    if cpucpu==0:        jog="Jogador X"
    if cpucpu==1:        jog="CPU 1 - X -"
    if temcpu==0:        cpu="Jogador O"
    if temcpu==1:        cpu="CPU 2 - O -"
    #########################################
    
    while True:
        if fim==1:
            break
        while fim==0:
            if (casa7=="X" and casa8=="X" and casa9=="X") or (casa4=="X" and casa5=="X" and casa6=="X") or (casa1=="X" and casa2=="X" and casa3=="X"):
                print(f"{jog} venceu formando uma linha!")
                novojogo()
            elif (casa7=="O" and casa8=="O" and casa9=="O") or (casa4=="O" and casa5=="O" and casa6=="O") or (casa1=="O" and casa2=="O" and casa3=="O"):
                print(f"{cpu} venceu formando uma linha!")
                novojogo()
            elif (casa7=="X" and casa4=="X" and casa1=="X") or (casa8=="X" and casa5=="X" and casa2=="X") or (casa9=="X" and casa6=="X" and casa3=="X"):
                print(f"{jog} venceu formando uma coluna!")
                novojogo()
            elif (casa7=="O" and casa4=="O" and casa1=="O") or (casa8=="O" and casa5=="O" and casa2=="O") or (casa9=="O" and casa6=="O" and casa3=="O"):
                print(f"{cpu} venceu formando uma coluna!")
                novojogo()
            elif (casa7=="X" and casa5=="X" and casa3=="X") or (casa9=="X" and casa5=="X" and casa1=="X"):
                print(f"{jog} venceu formando uma diagonal!")
                novojogo()
            elif (casa7=="O" and casa5=="O" and casa3=="O") or (casa9=="O" and casa5=="O" and casa1=="O"):
                print(f"{cpu} venceu formando uma diagonal!")
                novojogo()
                
            elif jogadas>9: ## ninguém formou um jogo, portanto resulta em empate
                print("Velhou!!!")
                novojogo()
            else:           ## ninguém ganhou após a rodada, verifica de quem é a vez de jogar
                verifjogs()
                    
def novojogo(): ## caso o jogador queira um novo jogo, as variáveis são resetadas
    global fim
    while True:
        if fim==1:
            break
        if fim==0:
            print("\n"+"#"*44)
            novo=input("\nDeseja jogar novamente?\n\nS ou N: ").upper()
            print("\n"+"#"*44+"\n")
            if novo=="S" or novo=="N":
                if novo=="N":
                   print("\nTchau!"); fim=1
                   continue              
                if novo=="S":
                    global casa1,casa2,casa3,casa4,casa5,casa6,casa7,casa8,casa9
                    global jogadas,quemjoga,temcpu,cpucpu
                    casa7=" "; casa8=" "; casa9=" "
                    casa4=" "; casa5=" "; casa6=" "
                    casa1=" "; casa2=" "; casa3=" "
                    fim=0; quemjoga=0; jogadas=1; temcpu=0; cpucpu=0
                    menu()
                    tabuleiro()
                    verifjogs()
            else:
                print("\nS OU N\n")
                continue

def velha(casa): ## "animação" feita quando CPU joga
    if casa==1:
        if casa1=="X":
            b="""
                     #    #   
                 ##############
                  \/ #    #    """

            c="""   
                  /\ #    #

                              """
        elif casa1=="O":
            b="""
                     #    #   
                 ##############
                  /\ #    #    """

            c="""   
                  \/ #    #

                              """
        a="""          
                     #    #
                     #    #
                 ##############
                     #    #    """            
    if casa==2:
        if casa2=="X":
            b="""
                     #    #   
                 ##############
                     # \/ #    """

            c="""   
                     # /\ #

                              """
        elif casa2=="O":

            b="""
                     #    #   
                 ##############
                     # /\ #    """

            c="""   
                     # \/ #

                              """
        a="""          
                     #    #
                     #    #
                 ##############
                     #    #    """
    if casa==3:            
        if casa3=="X":
            b="""
                     #    #   
                 ##############
                     #    # \/ """

            c="""   
                     #    # /\ 

                              """
        elif casa3=="O":

            b="""
                     #    #   
                 ##############
                     #    # /\ """

            c="""   
                     #    # \/ 

                              """
        a="""          
                     #    #
                     #    #
                 ##############
                     #    #    """
    if casa==4:            
        if casa4=="X":
            b="""
                     #    #
                 ##############
                  \/ #    #   """

            c="""
                  /\ #    #   
                 ##############
                     #    #    
                     #    #

                              """ 
        elif casa4=="O":
            b="""
                     #    #
                 ##############
                  /\ #    #   """

            c="""
                  \/ #    #   
                 ##############
                     #    #    
                     #    #

                              """
        a="""          
                     #    #    """
    if casa==5:
        if casa5=="X":
            b="""
                     #    #
                 ##############
                     # \/ #   """

            c="""
                     # /\ #   
                 ##############
                     #    #    
                     #    #

                              """
        elif casa5=="O":
            b="""
                     #    #
                 ##############
                     # /\ #   """

            c="""
                     # \/ #   
                 ##############
                     #    #    
                     #    #

                              """            
        a="""          
                     #    #    """
    if casa==6:
        if casa6=="X":
            b="""
                     #    #
                 ##############
                     #    # \/ """

            c="""
                     #    # /\ 
                 ##############
                     #    #    
                     #    #

                              """
        elif casa6=="O":
            b="""
                     #    #
                 ##############
                     #    # /\ """

            c="""
                     #    # \/
                 ##############
                     #    #    
                     #    #

                              """
        a="""          
                     #    #    """
    if casa==7:        
        if casa7=="X":
            a="""          
                  \/ #    #"""

            b="""    
                  /\ #    #     
                 ##############
                     #    #    
                     #    #
                 ##############"""

        elif casa7=="O":
            a="""          
                  /\ #    #"""

            b="""    
                  \/ #    #     
                 ##############
                     #    #    
                     #    #
                 ##############"""

        c="""
                     #    #    
                     #    #

                              """
    if casa==8:
        if casa8=="X":
            a="""          
                     # \/ #    """

            b="""    
                     # /\ #     
                 ##############
                     #    #    
                     #    #
                 ##############"""

        elif casa8=="O":
            a="""          
                     # /\ #    """

            b="""    
                     # \/ #     
                 ##############
                     #    #    
                     #    #
                 ##############"""

        c="""
                     #    #    
                     #    #

                              """            
    if casa==9:
        if casa9=="X":
            a="""          
                     #    # \/ """

            b="""    
                     #    # /\  
                 ##############
                     #    #    
                     #    #
                 ##############"""
            
        elif casa9=="O":           
            a="""          
                     #    # /\ """

            b="""    
                     #    # \/  
                 ##############
                     #    #    
                     #    #
                 ##############"""
        c="""
                     #    #    
                     #    #

                              """            
    print(f"{a}", end=" "); time.sleep(1)
    print(f"{b}", end=" "); time.sleep(1)
    print(f"{c}", end=" "); time.sleep(1)
    print()
    return           

print("\n\n"+" "*22,"Seja bem-vindo ao Jogo da Velha")
print(" "*16, "#"*43)
print(" "*22, "Desenvolvido por Bruno S. Bauer")
print(" "*16, "#"*43)
print("\n\n")
menu()
tabuleiro()
verifjogs()
