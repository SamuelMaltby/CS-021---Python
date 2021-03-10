def main():
    shuffled, correct = word_shuffle()
    print(shuffled)
    print(correct)

def word_shuffle():
    words_file = open('words.txt', 'r')
    all_words = words_file.read()
    words_file.close()

    all_words = all_words.split('\n')

    import random
    word = random.choice(all_words)
    shuffle = list(word)
    random.shuffle(shuffle)  # Stack Overflow
    shuffle = ''.join(shuffle)  # Stack Overflow
    answer = word
    return shuffle, answer





words_file = open('words.txt', 'r')
all_words = words_file.read()
words_file.close()

all_words = all_words.split('\n')


import random
word = random.choice(all_words)
shuffled = list(word)
random.shuffle(shuffled)  #Stack Overflow
shuffled = ''.join(shuffled)  #Stack Overflow
correct = word




print(all_words)
print(shuffled)
width = 24
print(correct)
print(correct[0])
print("")
print('\t','\t','Welcome to Word Shuffle:')
print("")
print("User: ", '\t',"User High Score: ")
print("")
print('How To Play:')
print("- Find the word in the scrambled letters.")
print("- You get 5 tries.")
print("- Each correct answer is worth 150 points.")
print("- Each incorrect guess deducts 15 points from your score.")
print("- Enter 'HINT' for the first letter of the word.")
print("- You get 3 Hints each will deduct 50 points from your score.")
print("")

tries = 5
score = 0
hints = 3
import sys
print('The shuffled word is:', shuffled)
guess = input('Your guess: ')
if guess == "":
    print('Please enter a valid guess')
    guess = input('Your guess: ')


while guess == "HINT":

    score -= 50
    hints -= 1


    if hints == 2:
        print('The word starts with: ', correct[0])
        print('You have', hints, 'hints left')
        guess = input('Your guess: ')
    if hints == 1:
        print('The word starts with: ', correct[0] + correct[1])
        print('You have', hints, 'hint left')
        guess = input('Your guess: ')
    if hints == 0:
        print('The word starts with: ', correct[0] + correct[1] + correct[2])
        print('You are out of hints')
        guess = input('Your guess: ')
    if hints < 0:
        score += 50
        print('You are out of hints')
        guess = input('Your guess: ')

while guess != correct and guess != "" and guess != "HINT":
    print('Your guess is incorrect')
    print('poop')
    tries -= 1
    score -= 15
    if tries > 1:
        print('You have', tries, 'attempts left')
        guess = input('Your guess: ')
    if tries == 1:
        print('You have', tries, 'attempt left')
        guess = input('Your guess: ')
    if tries <= 0:
        print('You are out of attempts')
        print('The correct answer was: ', correct)
        print(print('Your score is: ', score))
        sys.exit()



if guess == correct:
    score += 150
    print("You guessed it!")
    print('Your score is: ', score)
    response = input('Continue playing? (enter y or n): ')


    while response == 'y' :
        print("")
        tries = 5
        hints = 3
        word = random.choice(all_words)
        shuffled = list(word)
        random.shuffle(shuffled)
        shuffled = ''.join(shuffled)
        correct = word



        if guess == correct:
            score += 150
            print("You guessed it!")
            print('Your score is: ', score)
            response = input('Continue playing? (enter y or n): ')



    if response == 'n' :
        print('Thank you for playing')