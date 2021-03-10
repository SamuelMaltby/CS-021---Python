            shuffled, correct = word_shuffle()
            print('The shuffled word is:', shuffled)
            guess = input('Your guess: ')
            if guess == "":
                print('Please enter a valid guess')
                guess = input('Your guess: ')

            while guess != correct and guess != "":
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
                        print('Your score is: ', score)
                        top = 0
                        user_scores = open(user_file, 'r')
                        next(user_scores)
                        for line in user_scores.readlines():
                            num = int(line)
                            if line != '' and (top < num):
                                top = num
                        user_score = open(user_file, 'a')
                        user_score.write(str(score) + '\n')
                        user_scores.close()
                        user_score.close()
                        MAX = top
                        if score > MAX:
                            print('New High Score!')
                        if score == MAX:
                            print('You tied your high score.')
                        again = input('Play again? (enter y or n): ')
                        if again == 'y':
                            main()
                        else:
                            print('Thank you for playing.')
                            sys.exit()

            if guess == correct:
                score += 150
                print("You guessed it!")
                print('Your score is: ', score)
                response = input('Continue playing? (enter y or n): ')
