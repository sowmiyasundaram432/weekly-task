import random
def guessing_game(x:int)->str:


 while True:
     i=int(input("guess number:"))
     if x==i:
        print("correct")
        break
     elif x<i:
        print("Too High")
     else:
        print("Too Low")

guessing_game(x=random.randint(1,100))


    