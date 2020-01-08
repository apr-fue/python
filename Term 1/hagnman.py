#hangman game
#april fuentes
#10/19

#just a game of hangman
#computer picks a word
#player guesses it one letter at a time
#cant guess the word in time
#the stick figure dies

#imports
import random

#constants
HANGMAN = ['''
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
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \  |
      |
=========''']

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("BRUH", "YEET", "JELLYFISH", "JOE")

#initialize variables
word = random.choice(WORDS) 
so_far = "-" * len(word)
wrong = 0
used = []

print("Welcome to Hangman.")

while wrong < MAX_WRONG and  so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\nEnter your guess: ")
    guess = guess.upper()
    
    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("\nEnter your guess: ")
        guess = guess.upper()

    used.append(guess)
    if guess in word:
        print("\nYes!", guess, "is in the word!")

        new = " "
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[1]
        so_far = new
    else:
        print("\nSorry,",guess, "isn't in the word")
        wrong +=1


            
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\You've been hanged!")
else:
    print("nYou guessed it!")
print("\nThe word was", word)
input("\n\nPress the enter key to exit")















                












    
