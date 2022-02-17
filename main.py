import random
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

#Write your code below this line 👇
q_value = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. " + "\n")
my_value = int(q_value)
if my_value >=3:
  print("Invalid value. Please refresh and type it again")
else:
  #my value
  if my_value == 0:
    my_asii = rock
  elif my_value == 1:
    my_asii = paper
  elif my_value == 2:
    my_asii = scissors

  #computer value
  computer_value = random.randint(0, 2)
  if computer_value == 0:
      com_asii = rock
  elif computer_value == 1:
      com_asii =paper
  elif computer_value == 2:
      com_asii =scissors

  #rule
  if my_value == computer_value:
      result = ("Draw")
  elif my_value != computer_value:
      if my_value == 0 and computer_value == 2:
          result = ("You win")
      elif my_value == 0 and computer_value == 1:
          result = ("You lose")
      elif my_value == 1 and computer_value == 0:
          result = ("You win")
      elif my_value == 1 and computer_value == 2:
          result = ("You lose")
      elif my_value == 2 and computer_value == 0:
          result = ("You lose")
      elif my_value == 2 and computer_value == 1:
          result = ("You win")
      

  print("Your chose:" + my_asii)
  print("Computer chose:" + com_asii + "\n")

  #End_result = result + Emoticon
  if result == "Draw":
      END_result = result + " :|"
  elif result == "You win":
      END_result = result + " :D"
  elif result == "You lose":
      END_result = result + " :("
  else:
    END_result = "Invalid value. You are lose."

  print(END_result)

