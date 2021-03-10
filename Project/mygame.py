#Sam Maltby
# CS 021
# Final Project

# Program that plays word shuffle game with user
# Uses a created text file of 115 words
# Each game shuffles one word and asks user for their guess
# User has the option for a hint for a point deduction

# function extracts a word from a text file and shuffles the letters
def word_shuffle():
    import random  # allows random. method to be used

    try:    # try suite
        words_file = open('words.txt', 'r')  # opens text file
    except IOError:    # excepts error opening file
        print('Error opening file')

    else:
        all_words = words_file.read()        # reads entire file
        words_file.close()                   # closes file

        all_words = all_words.split('\n')    # makes list of each word separated by \n character

        word = random.choice(all_words)      # selects a random word from list
        shuffle = list(word)                 # makes list of each letter in selected word
        random.shuffle(shuffle)              # shuffles list of letters
        shuffle = ''.join(shuffle)           # combines the shuffled letters
        answer = word
        return shuffle, answer               # returns original word and shuffled

# function runs the rest of the game after getting shuffled word
def main():
    import sys                               # allows sys.exit() to terminate program

    user = input('Enter your username: ')    # asks user for their name

    user_file = str(user + '.txt')           # adds .txt to username

    user_score = open(user_file, 'a')        # creates a file to add scores to
    user_scores = open(user_file, 'r')       # allows user_score file to be read

    first_line = user_scores.readline()      # reads first line in file
    if first_line == '':                     # checks if first line is empty
        user_score.write('Username: ')       # if empty add Username:
        user_score.write(str(user) + '\n')   # add user
    user_score.close()                       # close file
    user_scores.close()                      # close file


    print("")
    print('\t', '\t', 'Welcome to Word Shuffle:')
    print("")
    print('\t', '\t', "User: ", user)
    print("")                                # setup game start page
    print('How To Play:')
    print("- Find the word in the scrambled letters.")
    print("- You get 5 tries.")
    print("- Each correct answer is worth 150 points.")
    print("- Each incorrect guess deducts 15 points from your score.")
    print("- Enter 'HINT' for the first letter of the word.")
    print("- You get 3 Hints each will deduct 50 points from your score.")
    print("")

    tries = 5    # number of attempts
    score = 0    # starting score
    hints = 3    # number of hints


    shuffled, correct = word_shuffle()        # runs word_shuffle function
    print('The shuffled word is:', shuffled)  # prints the shuffled word
    guess = input('Your guess: ')             # asks user for guess
    if guess == "":                           # checks to make sure answer entered
        print('Please enter a valid guess')   # if blank prints message
        guess = input('Your guess: ')         # asks for guess

    while guess != correct and guess != "":   # checks if 'HINT' is entered
        while guess == "HINT":

            score -= 50  # deducts 50 points
            hints -= 1   # deducts 1 hint from total

            if hints == 2:
                print('The word starts with: ', correct[0])  # prints first letter
                print('You have', hints, 'hints left')       # prints remaining hints
                guess = input('Your guess: ')                # asks again
            if hints == 1:
                print('The word starts with: ', correct[0] + correct[1])  # prints first two letters
                print('You have', hints, 'hint left')        # prints remaining hints
                guess = input('Your guess: ')                # asks again
            if hints == 0:
                print('The word starts with: ', correct[0] + correct[1] + correct[2])  # prints first three letters
                print('You are out of hints')
                guess = input('Your guess: ')                # asks again
            if hints < 0:
                score += 50                             # stops deducting points if 'HINT' entered more than 3 times
                print('You are out of hints')
                guess = input('Your guess: ')

        while guess != correct and guess != "" and guess != "HINT":  # checks if incorrect answer
            print('Your guess is incorrect')
            tries -= 1                                        # deducts 1 from total tries
            score -= 15                                       # deducts 15 points for each incorrect answer
            if tries > 1:
                print('You have', tries, 'attempts left')     # prints remaining # of guesses
                guess = input('Your guess: ')                 # asks again
            if tries == 1:
                print('You have', tries, 'attempt left')      # prints remaining # of guesses
                guess = input('Your guess: ')                 # asks again
            if tries <= 0:
                print('You are out of attempts')
                print('The correct answer was: ', correct)    # prints correct answer
                print('Your score is: ', score)               # prints final score
                top = 0   # sets top score
                user_scores = open(user_file, 'r')            # opens file of scores
                next(user_scores)                             # skips first line
                for line in user_scores.readlines():          # reads all lines after first
                    num = int(line)                           # sets num equal to the value on each line
                    if line != '' and (top < num):            # checks for largest value
                        top = num                             # sets top equal to greatest value
                user_score = open(user_file, 'a')             # opens file to append score
                user_score.write(str(score) + '\n')           # adds score to file
                user_scores.close()                           # closes file
                user_score.close()                            # closes file
                MAX = top                                     # declares greatest value outside of loop
                if score > MAX:                               # compares score to greatest value
                    print('New High Score!')
                if score == MAX:                              # compares score to greatest value
                    print('You tied your high score.')
                again = input('Play again? (enter y or n): ')  # asks to run program again

                while again != 'n' and again != 'y':
                    print("Enter 'y' or 'n'")  # warning message
                    again = input('Continue playing? (enter y or n): ')  # asks if user wants another word
                if again == 'y':
                    main()  # if 'y' program runs again
                elif again == 'n':
                    print('Thank you for playing.')
                    sys.exit()  # program terminates
                else:  # check if correct response:
                    print("Enter 'y' or 'n'")  # warning message



    if guess == correct:  # check if answer is correct
        score += 150                                    # adds 150 to score
        print("You guessed it!")
        print('Your score is: ', score)                 # prints  total score
        response = input('Continue playing? (enter y or n): ')  # asks if user wants another word

        while response != 'y' and response != 'n':
            print("Enter 'y' or 'n'")  # warning message
            response = input('Continue playing? (enter y or n): ')  # asks if user wants another word


        while response == 'y':
                        # following will run if 'y' entered
            print("")
            tries = 5  # resets number of attempts
            hints = 3  # resets number of hints

            shuffled, correct = word_shuffle()          # runs word_shuffle function
            print('The shuffled word is:', shuffled)    # prints the shuffled word
            guess = input('Your guess: ')               # asks user for guess
            if guess == "":                             # checks to make sure answer entered
                print('Please enter a valid guess')     # if blank prints message
                guess = input('Your guess: ')           # asks for guess

            while guess != correct and guess != "":     # checks if 'HINT' is entered
                while guess == "HINT":

                    score -= 50  # deducts 50 points
                    hints -= 1  # deducts 1 hint from total

                    if hints == 2:
                        print('The word starts with: ', correct[0])  # prints first letter
                        print('You have', hints, 'hints left')       # prints remaining hints
                        guess = input('Your guess: ')                # asks again
                    if hints == 1:
                        print('The word starts with: ', correct[0] + correct[1])  # prints first two letters
                        print('You have', hints, 'hint left')        # prints remaining hints
                        guess = input('Your guess: ')                # asks again
                    if hints == 0:
                        print('The word starts with: ',
                              correct[0] + correct[1] + correct[2])  # prints first three letters
                        print('You are out of hints')
                        guess = input('Your guess: ')                # asks again
                    if hints < 0:
                        score += 50  # stops deducting points if 'HINT' entered more than 3 times
                        print('You are out of hints')
                        guess = input('Your guess: ')                # asks again

                while guess != correct and guess != "" and guess != "HINT":  # checks if incorrect answer
                    print('Your guess is incorrect')
                    tries -= 1  # deducts 1 from total tries
                    score -= 15  # deducts 15 points for each incorrect answer
                    if tries > 1:
                        print('You have', tries, 'attempts left')  # prints remaining # of guesses
                        guess = input('Your guess: ')              # asks again
                    if tries == 1:
                        print('You have', tries, 'attempt left')   # prints remaining # of guesses
                        guess = input('Your guess: ')              # asks again
                    if tries <= 0:
                        print('You are out of attempts')
                        print('The correct answer was: ', correct)  # prints correct answer
                        print('Your score is: ', score)           # prints final score
                        top = 0  # sets top score
                        user_scores = open(user_file, 'r')        # opens file of scores
                        next(user_scores)                         # skips first line
                        for line in user_scores.readlines():      # reads all lines after first
                            num = int(line)                 # sets num equal to the value on each line
                            if line != '' and (top < num):  # checks for largest value
                                top = num                   # sets top equal to greatest value
                        user_score = open(user_file, 'a')   # opens file to append score
                        user_score.write(str(score) + '\n')  # adds score to file
                        user_scores.close()                 # closes file
                        user_score.close()                  # closes file
                        MAX = top                           # declares greatest value outside of loop
                        if score > MAX:                     # compares score to greatest value
                            print('New High Score!')
                        if score == MAX:                    # compares score to greatest value
                            print('You tied your high score.')
                        again = input('Play again? (enter y or n): ')  # asks to run program again
                        while again != 'n' and again != 'y':
                            print("Enter 'y' or 'n'")  # warning message
                            again = input('Continue playing? (enter y or n): ')  # asks if user wants another word
                        if again == 'y':
                            main()  # if 'y' program runs again
                        elif again == 'n':
                            print('Thank you for playing.')
                            sys.exit()  # program terminates
                        else:  # check if correct response:
                            print("Enter 'y' or 'n'")  # warning message

            if guess == correct:  # check if answer is correct
                score += 150  # adds 150 to score
                print("You guessed it!")
                print('Your score is: ', score)             # prints  total score
                response = input('Continue playing? (enter y or n): ')  # asks if user wants another word
                while response != 'n' and response != 'y':  # check if correct response
                    print("Enter 'y' or 'n'")  # warning message
                    response = input('Continue playing? (enter y or n): ')  # asks if user wants another word

        if response == 'n':  # user enters 'n'
            highscore = score

            top = 0  # sets top score
            user_scores = open(user_file, 'r')              # opens file of scores
            next(user_scores)                               # skips first line
            for line in user_scores.readlines():            # reads all lines after first
                num = int(line)                             # sets num equal to the value on each line
                if line != '' and (top < num):              # checks for largest value
                    top = num                               # sets top equal to greatest value
            user_score = open(user_file, 'a')               # opens file to append score
            user_score.write(str(score) + '\n')             # adds score to file
            user_scores.close()                             # closes file
            user_score.close()                              # closes file
            MAX = top                   # declares greatest value outside of loop


            user_scores = open(user_file, 'r')              # opens file of scores
            next(user_scores)                               # skips first line
            for line in user_scores:                        # reads data line by line
                num = int(line)                             # sets num equal to the value on each line

                if num > highscore:                         # checks for largest value
                    highscore = num                         # sets highscore equal to greatest value

            user_scores.close()                             # closes file

            print('High Score: ', highscore)                # prints user's high score

            if score > MAX:                                 # compares score to greatest value
                print('New High Score!')

            if score == MAX:                                # compares score to greatest value
                print('You tied your high score.')

            print('Thank you for playing.')                     # prints when done playing




main()  # runs entire program

