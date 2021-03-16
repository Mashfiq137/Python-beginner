secret_word = "giraffe"
guess = ""
life = 3
while(guess!=secret_word and life!=0):
    guess = input("Enter guess: ")
    life -=1

if life==0:
    print("Harso mama..abar try koro.")
else:
    print("You win!")