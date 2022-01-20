import random

# ---------Rock Paper Scissors----------r

def game(comp, you):

    if comp == you:
        return None


    elif comp == 'r':
        if you=='s':
            return False
        elif you=='p':
            return True
    

    elif comp == 's':
        if you=='p':
            return False
        elif you=='r':
            return True
    

    elif comp == 'p':
        if you=='r':
            return Falser
        elif you=='s':
            return True
plyrwc = 0
compwc = 0
for i in range (1,4):
   print(f"Round {i}")
   print("Computer's Turn: Rock(r) Paper(p) Scissors(s)-----")
   randNo = random.randint(1, 3) 
   if randNo == 1:
      comp = 'r'
   elif randNo == 2:
      comp = 's'
   elif randNo == 3:
      comp = 'p'

   you = input("Your Turn: Rock(r) Paper(p) Scissors(s)-----")
   a = game(comp, you)

   print(f"Computer chose {comp}")
   print(f"You chose {you}")

   if a == None:
      print("The game is a tie!")
   elif a:
      print("You Win!")
      plyrwc += 1
   else:
      print("You Lose!")
      compwc += 1
if plyrwc == compwc:
   print("The game is tie")
elif plyrwc > compwc:
   print("You Won the game")
else:
   print("Computer won the game")