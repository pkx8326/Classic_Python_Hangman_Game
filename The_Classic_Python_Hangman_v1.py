#!/usr/bin/env python
# coding: utf-8

# In[73]:


#The classic hanng man game (simple version)

import random

#constants
word_repo = ['mouse', 'cat', 'dog', 'chicken']
blanks_list = []
rights = 0
wrongs = 0

#Begin the game program

#Get a random word from the word_repo list (word repository)
word_random = word_repo[random.randint(0,len(word_repo)-1)]

#Create blanks
for i in range(len(word_random)):
    blanks_list.append("_")
blanks = "".join(blanks_list)

#Hints the player about thhe length of the word and shows blank spaces
print(f"{blanks} (This word has {len(word_random)} characters.)")

#This loop keeps the player guessing until he/she guesses wrong 6 times or he/she gets everything right
while rights < len(word_random) and wrongs < 6:
    guess = input("Guess a character: ").lower()
    if guess in word_random:
        for i in range(len(word_random)):
            if word_random[i] == guess:
                blanks_list[i] = guess
                blanks = "".join(blanks_list)
                rights += 1
        print(blanks)
    else:
        print("Wrong")
        wrongs += 1

#Ending messages
if wrongs == 6:
    print("Game Over!")
else:
    print("Well donne!")


# In[ ]:




