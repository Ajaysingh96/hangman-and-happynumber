import sys
import random
class Game():

    listofwords = ['hi','hlo',"evaporate","beautiful","data","sabudh","mohali",'india',"class"]
    s = random.choice(listofwords)
    word = s.lower()
    wordlist1 = list(word)
    wordlist = list(word)
    guesswords = list(word)
    ts=list()


    def __init__(self, name,cout):
        self.name = name
        self.cout=cout

    def game(self):
        print("______________WELCOME TO THE GAME {}___________".format(self.name))
        self.ts = ["_" for x in range(len(self.word))]
        print(self.ts)

        while  self.cout > 0:
            ourword = input("enter letter: \n ")
            p = ourword.lower()

            if (p in self.wordlist) == True:
                print("match")
                tt = [i for i, e in enumerate(self.wordlist1) if e == p]
                #print(tt)
                for i in range(self.wordlist.count(p)):
                    self.wordlist.remove(p)
                #print(self.wordlist)
                for i in range(len(tt)):
                    self.ts[tt[i]] = p
                print(self.ts)
                self.guesswords.append(p)
                if self.ts == self.wordlist1:
                    print("WORD FOUND")
                    print("".join(self.ts))

                    break



            elif (p in self.guesswords) == True:
                print("Already guessed")
                continue


            else:
                print("no match try again")
                self.cout=self.cout - 1
                print("{} chances left".format(self.cout))

    def guessword(self):
        print(self.guesswords)
    def our_status(self):
        print("".join(self.ts))
    def quit():
        sys.exit(0)

def mains():
    global cout
    player=input("ENTER PLAYER NAME:")

    gamestart= Game(name=player,cout = 6)
    gamestart.game()

if __name__ == "__main__":
    mains()