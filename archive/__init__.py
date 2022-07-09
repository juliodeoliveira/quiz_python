#import cadastro


def WriteFile(name, nick="N/A", years=0):
    try:
        n = open(name, "at")
    except:
        print("An error occoured.")
    else:
        try:
            n.write(nick)
            #n.write(f"{nick};{years}\n")
            n.close()
        except:
            print("Error when I try to write in archive")
        

def FileExists(name):
    try:
        n = open(name, "rt")
        n.close()
    except FileNotFoundError:
        return False

    else:
        return True


def CreateFile(name):
    try:
        n = open(name, "wt+")
        n.close()
    except:
        print("Something just failed")

    else:
        print(f"File with name: {name} have been created.")


def ReadFile(name):
    try:
        n = open(name, "rt")
    except:
        print("A error occoured when I try to open the file.")

    else:
        for line in n:
            #dice = line.split(";")
            #dice[1] = dice[1].replace("\n","")
            #print(f"{dice[0]:<30}{dice[1]:>3} anos")
            print(line)
    finally:
        n.close()
