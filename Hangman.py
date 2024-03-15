import random

words = ["office", "panda", "cabin", "ginger"]
computer = random.choice(words)
#Get The number of space
word_space = ["_"] * len(computer)
print(' '.join(word_space))

#Hangman Pictures
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
n = 0
hangman = HANGMANPICS[n]

#Guessing Letters
tries = 6
while "_" in word_space and tries > 0:
    guessed = input("Please guess a letter: ").lower()
    if guessed not in computer or guessed == "":
        tries -= 1
        n += 1
        hangman = HANGMANPICS[n]
    if guessed in word_space:
            print("You already guessed that. Try again.")
            print(f"You have {tries} more tries")
            continue
    count = 0
    for x in computer:
        if x == guessed:
            word_space[count] = guessed
        count += 1
    print(' '.join(word_space))
    print(f"You have {tries} more tries")
    print(hangman)

if "_" not in word_space:
    print("""
        ***********
          YOU WIN
        ***********
    """)
else:
    print("You lose!")
