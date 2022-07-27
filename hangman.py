import random


name= input("Enter your name:")
print("Welcome!!!")
print("Good Luck",name,";-)")

words=["india","china","pakistan","iran","dubai"]
word=random.choice(words)
print(word)

print("Guess the character")

guesse= ""
turns=10

while turns > 0:
    failed=0
    for char in word:
        if char in guesse:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("Yoo,Congrates!!! You won ;-)")
        print("The word is",word)
        break
    
    guess= input ("Guess the character:")
    guesse += guess

    if guess not in word:
        turns -= 1
        print("wrong")
        print("you have",turns,"more guess")


    if turns==9:
        print("9 turns left!!!")
        print("--------------------------")
    if turns==8:
        print("8 turns left!!!")
        print("--------------------------")
        print("            O              ")

    if turns==7:
        print("7 turns left!!!")
        print("--------------------------")
        print("            O            ")
        print("            |              ")
    if turns==6:
        print("6 turns left!!!")
        print("--------------------------")
        print("            O            ")
        print("            |              ")
        print("           /               ")
    if turns==5:
        print("5 turns left!!!")
        print("--------------------------")
        print("            O            ")
        print("            |              ")
        print("           / \             ")
                
    if turns==4:
        print("4 turns left!!!")
        print("--------------------------")
        print("           \O            ")
        print("            |              ")
        print("           / \             ")
    if turns==3:
        print("3 turns left!!!")
        print("--------------------------")
        print("           \O/             ")
        print("            |              ")
        print("           / \             ")
    if turns==2:
        print("2 turns left!!!")
        print("--------------------------")
        print("           \O/             ")
        print("            |              ")
        print("           / \             ")
    if turns==1:
        print("only 1 turns left!!! Hangman on his last breath")
        print("--------------------------")
        print("           \O/             ")
        print("            |              ")
        print("           / \             ")
    if turns== 0:
            print("You loose :-]")
              


      
    




    # if turns ==9:
    #     print("Sorry!!",name,"You loose :-]")
    #     print("the word is",word)


