# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return(False)
    return(True)
    
# secret_word = "apple"
# letters_guessed = ["a", "p", "l", "e"]    
# print(is_word_guessed("apple", letters_guessed))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for char in secret_word:
        if char in letters_guessed:
            guessed_word += char
        else:
            guessed_word += "_ "
    return guessed_word

# secret_word = "apple"
# letters_guessed = ["p", "e"]    
# print(get_guessed_word("apple", letters_guessed))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ""
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char
    return available_letters

# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']   
# print(get_available_letters(letters_guessed))
    
def warn_user(warnings_remaining, guesses_remaining):
    if warnings_remaining > 0:
        warnings_remaining -= 1
        if warnings_remaining != 1:
            warning_text = "You have " + str(warnings_remaining) + " warnings left:"
        else:
            warning_text = "You have 1 warning left:"
    else:
        warning_text = "You have no warnings left so you lose one guess:"
        guesses_remaining -= 1
    return warning_text, warnings_remaining, guesses_remaining
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings_remaining, "warnings left.")
    while guesses_remaining > 0:
        print("-" * 14) # 13 is unlucky, changed from example
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            print("Congratulations, you won!")
            print("Your total score for this game is",
                  len(secret_word) * guesses_remaining)
            break
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        user_input = input("Please guess a letter: ")
        if len(user_input) == 1 and str.isalpha(user_input):
            new_guess = str.lower(user_input)
            if new_guess not in letters_guessed:
                letters_guessed += [new_guess]
                if new_guess in secret_word:
                    result_text = "Good guess:"
                else:
                    result_text = "Oops! That letter is not in my word:"
                    if new_guess in "aeiou":
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
            else:
                warning_text, warnings_remaining, guesses_remaining = warn_user(
                    warnings_remaining, guesses_remaining)
                result_text = "Oops! You've already guessed that letter. " + warning_text
        elif len(user_input) > 1 and str.isalpha(user_input[0]):
            warning_text, warnings_remaining, guesses_remaining = warn_user(
                warnings_remaining, guesses_remaining)
            result_text = "Please input only 1 letter at a time. " + warning_text
        else:
            warning_text, warnings_remaining, guesses_remaining = warn_user(
                warnings_remaining, guesses_remaining)
            result_text ="Oops! That is not a valid letter. "  + warning_text
        print(result_text, get_guessed_word(secret_word, letters_guessed))
    if guesses_remaining == 0:
        print("-" * 14)
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
 

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_gapless = ""
    # So bad to do this over and over! But the function names...
    for char in my_word:
        if char != " ":
            my_word_gapless += char
    if len(my_word_gapless) != len(other_word):
        return False
    for index in range(len(my_word_gapless)):
        if my_word_gapless[index] != "_" and my_word_gapless[index] != \
            other_word[index] or my_word_gapless[index] == "_" and \
            other_word[index] in letters_guessed:
            return False
    return True


def show_possible_matches(my_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word, letters_guessed):
            possible_matches += [word]
    return " ".join(possible_matches)
    

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings_remaining, "warnings left.")
    while guesses_remaining > 0:
        print("-" * 14) # 13 is unlucky, changed from example
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            print("Congratulations, you won!")
            print("Your total score for this game is",
                  len(secret_word) * guesses_remaining)
            break
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        user_input = input("Please guess a letter: ")
        if user_input == "*":
            print("Possible word matches are: ")
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed),
                                        letters_guessed))
        elif len(user_input) == 1 and str.isalpha(user_input):
            new_guess = str.lower(user_input)
            if new_guess not in letters_guessed:
                letters_guessed += [new_guess]
                if new_guess in secret_word:
                    result_text = "Good guess:"
                else:
                    result_text = "Oops! That letter is not in my word:"
                    if new_guess in "aeiou":
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
            else:
                warning_text, warnings_remaining, guesses_remaining = warn_user(
                    warnings_remaining, guesses_remaining)
                result_text = "Oops! You've already guessed that letter. " + warning_text
            print(result_text, get_guessed_word(secret_word, letters_guessed))
        elif len(user_input) > 1 and str.isalpha(user_input[0]):
            warning_text, warnings_remaining, guesses_remaining = warn_user(
                warnings_remaining, guesses_remaining)
            result_text = "Please input only 1 letter at a time. " + warning_text
            print(result_text, get_guessed_word(secret_word, letters_guessed))
        else:
            warning_text, warnings_remaining, guesses_remaining = warn_user(
                warnings_remaining, guesses_remaining)
            result_text ="Oops! That is not a valid letter. "  + warning_text
            print(result_text, get_guessed_word(secret_word, letters_guessed))
    if guesses_remaining == 0:
        print("-" * 14)
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass
    
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
