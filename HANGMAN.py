import random
word_list=["elephant","giraffe","camel","command","python","password","signal","express","distinct","meaning","speech","write","something"]

#Select a random word from list
chosen_word=random.choice(word_list)
end_of_game=False

from  Hangman_art import stages,logo
print(logo)

display=[]
for letter in chosen_word:
     display+="_"
lives=6
print(f"{' '.join(display)}")

while not end_of_game:
     guess=input("Guess a letter: ").lower()

     if guess in display:
          print(f"You have already guessed {guess}")
     #Check if the letter guesssed by the user exist in the choosen_word
     for i in range(len(chosen_word)):
          letter=chosen_word[i]
          #print(f"Current position:{i}\n Current ;etter:{letter}\nGuessed letter:{guess}")
          if letter == guess:
               display[i]=letter

     if guess not in chosen_word:
          print(f"You have guessed {guess},It's not in the word, You lose a life ")
          lives -= 1
          if lives==0:
               end_of_game=True
               print("The word was",chosen_word)
               print("***You lost***")   

     print(f"{' '.join(display)}")

     if "_" not in display:
          end_of_game=True
          print("***YOU WON***")
     else:
          print(stages[lives])
     
