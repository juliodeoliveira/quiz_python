import random
import time
import os

#Enfeite para títulos.
def Title(text):
    size = len(text) - 4
    print("-" * size)
    print(" ", text)
    print("-" * size)


#Precisa de algo para seu quiz?
def quiz(alt=[], correct=""):

    """
    -> alt = confere as alternativas, certo ou errado.
    -> correct = recebe a alternativa correta.
    """

    #palavras = ["Amanhã", "Hoje", "140 mil", "Talvez"]

    alter = []

    count = 1

    #Loop lê e coloca as palavras dentro de alter, até ter todas lá.     
    while count <= len(alt):
        pick = random.choice(alt)

        if pick not in alter:
            alter.append(pick)

        else:
            continue

        count += 1
    #-

    #Adiciona a palavra correta para a lista alter
    alter.append(correct)
    #-

    #Mistura a lista alter.
    random.shuffle(alter)

    #Pega o index da palavra correta, e coloca na variável right. (int)
    right = alter.index(correct) + 1
    
    #Print para debug
    #print(f"Resposta: {right}")
    
    #Esse loop cria uma "tabela" para o usuário decidir qual alternativar escolher
    time.sleep(3)
    x = 1
    for a in alter:
        print(f"{x}. {a}")
        time.sleep(1)
        x += 1
    #-

    print("-"* 15)

    #Aqui corre o tempo que o usuário tem para memorizar cada alternativa.
    timer(5)

    os.system("clear")

    #Loop que verifica adequadamente se o usuário digitou ou número.
    while True:
        try:
            answer = int(input("Sua resposta: "))
            break
        except (ValueError):
            print("\033[31mValor inválido\033[m...")
            continue      
    
    answer = str(answer)


    #Transforma o número em string
    correto = str(right)

    #Por fim, verifica se o usuário acertou.
    if answer in correto:
        print("Você \033[32mACERTOU\033[m!")
        return True
    else:
        print("Você \033[31mERROU\033[m...")
        return False

    #if alt == True:
        #print("Você acertou!")
    #elif alt == False:
     #   print("Você Errou :(")

#Timer regressivo
def timer(sec):
    for s in range(sec, 0, -1):
        print(s, "...", end=" ", flush=True)
        time.sleep(1)