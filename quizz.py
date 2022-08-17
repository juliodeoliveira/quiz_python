# import's necessários para o script
import Tools
import os
import random
import time
import archive

# pra falar a verdade eu não sei da necessidade dessa classe aqui, mas da pra fazer alguma coisa
class Exam:

    #Essas def's são meio q um objeto...
    def q1():
        time.sleep(3)
        asks.append(1)

        os.system("clear")

        Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m Quantos KM de vazos sanguíneos tem aproximadamente um ser humano?")
        p = Tools.quiz(["100m", "40 mil km", "55m", "19dm"], "97 mil km")


        if p == True:
            corrects.append(1)
        elif p == False:
            wrongs.append(1)

        input("Pressione ENTER para continuar...")
        print("Aguarde...")


    # Cada uma recebe um número...
    def q2():

        os.system("clear")

        asks.append(1)
        Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m Estima-se que o universo tem aproximadamente quantas galáxias:")
        p = Tools.quiz(["20 bilhões", "1", "13 bilhões"], "10 bilhões")

        if p == True:
            corrects.append(1)
        elif p == False:
            wrongs.append(1)

        input("Pressione ENTER para continuar...")
        print("Aguarde...")


    # E lá em baixo esse número é misturado...
    def q3():

        os.system("clear")


        asks.append(1)
        Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m Quanto tempo a luz do sol demora para chagar na Terra aproximadamente:")
        p = Tools.quiz(["20min", "40min", "10min"], "8min")

        if p == True:
            corrects.append(1)
        elif p == False:
            wrongs.append(1)

        input("Pressione ENTER para continuar...")
        print("Aguarde...")


    # Assim deixando a ordem das perguntas de forma aleatória.
    def q4():

        os.system("clear")

        asks.append(1)
        Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m Quantos metros tem a parte mais profunda do oceano:")
        p = Tools.quiz(["20 Mil metros", "14 Mil metros", "30 Mil metros"], "11 Mil metros")

        if p == True:
            corrects.append(1)
        elif p == False:
            wrongs.append(1)

        input("Pressione ENTER para continuar...")
        print("Aguarde...")



    def q5():

        os.system("clear")

        asks.append(1)
        Tools.Title(f"\033[33m{len(asks)}° Pergunta: \033[m Qual o único planeta do sistema solar que não tem nome de um deus:")
        p = Tools.quiz(["Júpiter", "Saturno", "Lua"], "Terra")

        if p == True:
            corrects.append(1)
        elif p == False:
            wrongs.append(1)

        input("Pressione ENTER para continuar...")
        print("Aguarde...")



    def q6():

        os.system("clear")

        asks.append(1)
        Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m A cada ano o monte Everest cresce aproximadamente...")
        p = Tools.quiz(["3 Metros", "15 Centímetros", "40 Metros"], "4 Milímetros")

        if p == True:
            corrects.append(1)
        elif p == False:
            wrongs.append(1)
        
        input("Pressione ENTER para continuar...")
        print("Aguarde...")



    def q7():
        os.system("clear")

        asks.append(1)
        Tools.Title(f"\033[33m{len(asks)}° Pergunta:\033[m Qual foi o primeiro jogo a ir ao espaço?")
        p = Tools.quiz(["Mario Bros.", "Donkey Kong", "Space Invaders"], "Tetris")

        if p == True:
            corrects.append(1)
        elif p == False:
            wrongs.append(1)

        input("Pressione ENTER para continuar...")
        print("Aguarde...")
        
    
os.system("clear")

print("-------------------------------------------------------------------")
print("Bem-vindo(a) a meu quiz, são assuntos aleatórios então, se divirta!")
print("-------------------------------------------------------------------")
time.sleep(3)

os.system("clear")

questions = [1, 2, 3, 4, 5, 6, 7, 8]

# Toda vez que eu precisar saber, por exemplo, quantas perguntas o usuário acertou, eu uso len(corrects)

corrects = []

asks = []

wrongs = []

# Aqui ele cria uma ordem de números
#r = 1
#while 1:
#    questions.append(r)
#    r += 1
#
#    if r == 8:
#        break

# Essa ordem será misturada
random.shuffle(questions)
for q in questions:

    # E cada if chama uma função, assim deixa mais aleatório (Reclama pro programador reduzir isso dps kkkkkk)
    if q == 1:
        Exam.q1()

    elif q == 2:
        Exam.q2()
    
    elif q == 3:
        Exam.q3()
    
    elif q == 4:
        Exam.q4()
    
    elif q == 5:
        Exam.q5()
    
    elif q == 6:
        Exam.q6()

    elif q == 7:
        Exam.q7()

os.system("clear")

print()
print("-"*30)
print(f"Você \033[32mACERTOU\033[m: \t\t\033[4m{len(corrects)}\033[m")
print(f"e \033[31mERROU\033[m: \t\t\033[4m{len(wrongs)}\033[m")
print(f"Total de \033[33mperguntas\033[m: \t\033[4m{len(asks)}\033[m")
print("-"*30)
print()

champion = str(input("Digite seu nome: "))

fileName = "Leaderboard.txt"

# Loop para verificar input do usuário, se ele digitar algo errado, simplesmente volta o loop.
while True:
    try:
        Leader = int(input("Pressione 0 para sair, e 1 para ver o mural de participantes: "))
        if Leader == 0:
            break

        if Leader == 1:
            if not archive.FileExists(fileName):
                archive.CreateFile(fileName)

            if len(corrects) > 0:
                archive.WriteFile(fileName, f"\n{champion} ------------ {len(corrects)}")
                first = archive.ReadFile(fileName)
    except:
        continue

#🦆