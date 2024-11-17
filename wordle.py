import random
from colorama import Fore
#replace the ... with correct file path
file_path = r'C:\Users\...\worldepy\words.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

wordnum = random.randint(0, len(lines) - 1)
word = lines[wordnum]

#print(Fore.WHITE + word)

good = False
def guess_word():
    global good
    valid = False
    guess = list(input())
    while not valid:
        if len(guess) == 5:
            valid = True
            print("\033[F\033[K", end="")  # Move up one line and clear the line
        else:
            print("Please enter a valid input")
            guess = list(input())
    real = list(word)[0:5]
    outcome = []
    result = []
    for i in range(5):
        if guess == real:
            print(Fore.LIGHTGREEN_EX + ''.join(guess))
            print(Fore.WHITE, end="")
            good = True
            return True
        if guess[i] == real[i]:
            outcome.append("G")
        elif guess[i] in real:
            outcome.append("Y")
        else:
            outcome.append("X")
    for i in range(5):
        if outcome[i] == "G":
            result.append(Fore.LIGHTGREEN_EX + str(guess[i]))
        elif outcome[i] == "Y":
            result.append(Fore.YELLOW + str(guess[i]))
        else:
            result.append(Fore.WHITE + str(guess[i]))
    print("\r" + ''.join(result))
    print(Fore.WHITE, end ="")
    

    

for i in range(6):
    if guess_word() == True:
        break
    
if good == False:
    print("The correct word was: " + word)
