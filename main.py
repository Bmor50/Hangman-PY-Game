import random
from pictures import stages
word_list = ["orange", "pickle", "lemon", "watermelon", "pear"]
lives = 6
index = 0
pic_index = 6




# Generate a random word
rand_word = random.choice(word_list)




#Ask the user to guess a letter
user_word = []


# Generate as many random blanks as letters in word
for x in range(len(rand_word)):
 user_word.append("_")




def word_loop():
  global index, safe, lives
  for i in rand_word:
   index += 1
   if i == user_guess:
     user_word[index - 1] = user_guess




# check if userinput is in the random word
while lives !=0:
 user_guess = input("Enter a letter: ").lower()
 word_loop()
 index = 0
 if user_guess in user_word:
   print("NICE JOB")
   print(stages[pic_index])
   print(user_word)
   print(f"CURRENT LIVES: {lives}")


 else:
   pic_index -= 1
   print(stages[pic_index])
   print("TRY AGIAN")
   print(user_word)
   lives -= 1
   print(f"CURRENT LIVES: {lives} ")
  
 my_string = "".join(user_word)
 if my_string == rand_word:
   print(f"YOU WON YOUR WORD WAS: {rand_word}")
   break





print("GAME OVER!")


 # compare the the input value to the randomword
