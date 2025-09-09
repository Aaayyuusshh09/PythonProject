rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]
player = int(input("What do you choose ? type 0 for rock ,type 1 for paper , type 2 for scissors "))
if player<=2 and player>=0:
    print(game[player])
import random
computer = random.randint(0,2)
print("Computer choose:-")
print(game[computer])
if computer == 0 and player == 2:
    print("YOU LOOSE ")
elif computer == 2 and player == 0:
    print("YOU WIN ")
elif  player > 2 or player < 0 :
    print("in valid input ")
elif  computer > player:
    print("YOU LOOSE ")
elif computer < player:
    print("YOU WIN ")
elif computer == player:
    print("ITS A DRAW ")
else:
    print("in valid input ")
