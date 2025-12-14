import random

easy_word = ["cat", "dog", "sun", "pen", "book"]
medium_word = ["garden", "teacher", "computer", "picture", "holiday"]
hard_word = ["environment", "development", "information", "programming", "communication"]

print("Welcome To Password Guessing Game")
print("Choose a difficulty level : Easy, Hard, Medium ")

level = input("Enter Difficulty : ").lower()
if level == "easy":
    secret = random.choice(easy_word)
elif level == "medium":
    secret = random.choice(medium_word)

elif level == "hard":
    secret = random.choice(hard_word)

else:
    print("Invalid Choice . Defulting to easy level")
    secret = random.choice(easy_word)

attempts = 0
print("\n Guess The password")

while True:
    guess = input("Enter Your Guess : ").lower()
    attempts += 1

    if guess == secret:
        print(f'Congratulations! You Guess it {attempts} Attempts')
        break

    hints = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i]==secret[i]:
            hints += guess[i]
        else:
            hints += "_"
        
    print("Hint :" , hints)

print("Game Over")