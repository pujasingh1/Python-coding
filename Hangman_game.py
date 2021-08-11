import random
from os import system

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    system('cls')
    
    if guess in display:
        print(f"You already guessed a letter {guess}")
        
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word:
        print(f"You guessed a letter {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives <= 0:
            end_of_game = True
            print("You Lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    print(stages[lives])
