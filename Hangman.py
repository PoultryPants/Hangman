# This program selects a random word from the word Library and asks the player to guess it letter-by-letter, much like in Hang Man


# This part imports modules and contains the HANGMAN_PICS
import random

HANGMAN_PICS = ['''
 +---+
     |
     |
     |
     |
    ===''', '''
 +---+
 0   |
     |
     |
     |
    ===''', '''
 +---+
 0   |
 |   |
     |
     |
    ===''', '''
 +---+
 0   |
/|   |
     |
     |
    ===''', '''
 +---+
 0   |
/|\  |
     |
     |
    ===''', '''
 +---+
 0   |
/|\  |
 |   |
     |
    ===''', '''
 +---+
 0   |
/|\  |
 |   |
/    |
    ===''', '''
 +---+
 0   |
/|\  |
 |   |
/ \  |
    ===''']

words = 'house goal soccer school ball stop building sunflower bear buffalo coding random hang basket computer book sock helmet paper binder phone smartphone cleats minecraft game eraser apple orange lemon train smoke cup bowl plug wire desk dog save safe flashlight headlamp zebra giraffe elephant coat sweatshirt pants shirt jeans shoes headphones rock why horse horror plum plus butterfly owl lamp bat cow pig chicken holder tower fireplace mantlepiece couch sofa pillow pijama bread loaf television tv shoe furniture run running walk walking mysterious mystery drawer computer mouse football defender attacker attacking press tab window door floor ground ceiling teacher book paper write writing rocket dad mom cloth'.split()


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print('H A N G M A N')
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')

    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # Replaces the blanks with the corectly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print()
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Chose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess


def playAgain():
    # Returns true if the player wants to play again, otherwise it returns false
    print('Do you want to play again?')
    return input().lower().startswith('y')


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Checks if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You won in ' + str(len(missedLetters)
                                                                                    ) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Checks if the player has guessed too many times and lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\n\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '".')
            gameIsDone = True

    # Asks the player if they want to play again (But only if the game is over)
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
