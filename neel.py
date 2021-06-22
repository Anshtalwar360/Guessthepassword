#aurumporteasest
import color
import lolneel
import time
import os


secret_word = lolneel.x
guess= " "
countb=0
countc=0
countg=0

while guess != secret_word:
    guess = input("Enter your guess: ")

    if len(guess)>len(secret_word):
    	print("the length of the guess is greater than that of the secret word")
    	continue
            
    elif len(guess)<len(secret_word):
       	 print("the length of the guess is less than that of the secret word")
       	 continue

    for i in range(0,len(guess)):
        
        if guess[i] == secret_word[i]:
            countb = countb+1


    for i in range(len(guess)):
      for j in range(len(guess)):
        if(guess[i] == secret_word[j] and j != i): countc+=1

    countg= countg+1   

    print(countc,'cows', countb, 'bulls')
    countc, countb = 0, 0
print(color.BOLD + 'You won in',countg,'guesses'+ color.END)
os.system("curl parrot.live")
sys.exit()




