import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choises = [rock, paper, scissors]

print('rock(0) / paper(1) / scissors(2)')

x = int(input('please choose one of the options above(enter the number):\n'))
player = choises[x]
pc = random.choice(choises)

print(f'you chose:\n {player}')
print(f'computer chose:\n {pc}')

if player == scissors and pc == rock or player == rock and pc == paper or player == paper and pc == scissors:
    print('computer won!')
if pc == scissors and player == rock or pc == rock and player == paper or pc == paper and player == scissors:
    print('player won!')
if player == pc:
    print('The match is even')
