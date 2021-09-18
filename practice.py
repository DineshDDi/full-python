# importing time module
import time


name = input('what is your name? :')

print("hello, ",name, "Time to play hangman!")

print('')

time.sleep(1)

print()
time.sleep(0.5)

word = "secret"

guesses = ""

turn = 10

while turn>0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
         print("you win")
    break

guess = input("guess a character : ")

guesses += guess

if guess not in word:
    turn = turn-1
    print("wrong")

print("you have", turn, 'more guesses')

if turn == 0:
    print("you loose")






