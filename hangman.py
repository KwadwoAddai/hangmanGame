import random
from hangman_art import stages,logo
from hangman_wordlist import word_list

lives = 6
end_game = False
print(logo)
chosen_word = random.choice(word_list)
display=['_' for _ in chosen_word]
print(f"There are {len(display)} letters to guess \n{display}")

while end_game == False:

    guess = input("Guess a letter: ")

    if guess in display:
            print(f"You have already tried {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
            print(f"{lives} after correct")
        
    if guess not in chosen_word:
        lives -=1
        print(f"Your guess {guess} not in word\n{lives} more lives left")
        if lives == 0:
            end_game = True
            print("out of lives")

    print(display)

    if "_" not in display:
        print("You won")
        end_game = True
    print(stages[lives])
