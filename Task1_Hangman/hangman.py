import random
print("welcome to hangman game")

words = ["cat", "ball", "banana", "man", "gall"]
guessed_letter = []

word = random.choice(words)
remaining = 5


def validate(guess):
    guess = (guess.strip().lower())
    return guess


while True:
    guess = validate(input("guess the letter: "))
    if len(guess) == 1 and guess.isalpha():
        

        if guess in guessed_letter:
           print("You already guessed that letter. Try another!") 
        else:

            guessed_letter.append(guess)
            if guess in word:
                print("good guess")
            else:
                print("wrong guess")
                remaining -= 1
                print("remaining ⌛", remaining)
                if remaining == 0:
                    print(" \n ❌you lose!",
                        f"the word was {word}")
                    break
        for letter in word:
            if letter in guessed_letter:
                print(letter,  end="")
            else:
                print("_",  end="")
        if all(letter in guessed_letter for letter in word):
            print(" \n ✅You won!")
            break
    else:
        print(f"invalid guess : {guess}")