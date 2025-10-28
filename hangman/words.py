import data 
import random
  

def choose_secret_word(words: list[str]) -> str:
    a = random.randint(0,len(words)-1)
    the_word = words[a]
    return(the_word)
