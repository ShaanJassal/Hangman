import random

# the words that can possibly be used in game
def wordsToChooseFrom():
    words = [
    "apple", "banana", "orange", "strawberry", "kiwi",
    "python", "javascript", "algorithm", "programming", "variable",
    "google", "microsoft", "apple", "amazon", "facebook",
    "pear", "grape", "watermelon", "pineapple", "mango",
    "java", "ruby", "html", "css", "database",
    "yahoo", "ibm", "intel", "adobe", "twitter",
    "peach", "plum", "blueberry", "blackberry", "apricot",
    "c++", "php", "sql", "node", "server",
    "oracle", "linkedin", "netflix", "uber", "tesla",
    "cherry", "melon", "avocado", "coconut", "guava"
]
    return random.choice(words)

# the hangman art
def hangman_ascii(tries):
    stages = [
        # No person
        '''
           --------
           |      
           |     
           |     
           |      
           |     
        ------------
        ''',
        # Head
        '''
           --------
           |      |
           |      O
           |     
           |      
           |     
        ------------
        ''',
        # Head and body
        '''
           --------
           |      |
           |      O
           |      |
           |      
           |     
        ------------
        ''',
        # Head, body, and one arm
        '''
           --------
           |      |
           |      O
           |     \|
           |      
           |     
        ------------
        ''',
        # Head, body, both arms
        '''
           --------
           |      |
           |      O
           |     \|/
           |      
           |     
        ------------
        ''',
        # Head, body, both arms, one leg
        '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     | 
        ------------
        ''',
        # Full hangman
        '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     | |
        ------------
        '''
    ]
    return stages[tries]

def play_hangman():
    word = wordsToChooseFrom()
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    while tries > 0:
        # displays current state of word with underscores for letters that are yet to be guessed
        display = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print(display)

        if display == word:
            print("Congratulations! The word was:", word)
            break


        # displays hangman figure
        print(hangman_ascii(6 - tries))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            print("Correct!")
            guessed_letters.append(guess)
        else:
            print("Incorrect!")
            guessed_letters.append(guess)
            tries -= 1

    if tries == 0:
        print("You ran out of tries! The word was:", word)

    replay = input("Do you want to play again? (yes/no): ")
    if replay.lower() == "yes":
        play_hangman()
    else:
        print("Thanks for playing! Created by Shaan Jassal")

play_hangman()
