import random
import time
import os

def Title(text):
    size = len(text) - 4
    print("-" * size)
    print(" ", text)
    print("-" * size)



def quiz(alt=[], correct=""):

    """
    -> alt = confere as alternativas, certo ou errado.
    -> correct = recebe a alternativa correta.
    """

    #palavras = ["Amanhã", "Hoje", "140 mil", "Talvez"]

    alter = []

    count = 1
            
    while count <= len(alt):
        pick = random.choice(alt)

        if pick not in alter:
            alter.append(pick)

        else:
            continue

        count += 1

    alter.append(correct)

    random.shuffle(alter)

    right = alter.index(correct) + 1
    
    #print(f"Resposta: {right}")
    
    time.sleep(3)
    x = 1
    for a in alter:
        print(f"{x}. {a}")
        time.sleep(1)
        x += 1

    print("-"* 15)
    timer(5)
    os.system("clear")

    answer = input("Sua resposta: ")

    correto = str(right)

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

def timer(sec):
    for s in range(sec, 0, -1):
        print(s, "...", end=" ", flush=True)
        time.sleep(1)