# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 6

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "ps3_words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print(len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    lower_word = word.lower()
    letter_sum = 0
    for i in lower_word:
        letter_sum += SCRABBLE_LETTER_VALUES[i]
    usage_score = max((7 * len(word) - 3 * (n - len(word))), 1)
    return letter_sum * usage_score


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    hand["*"] = 1
    num_vowels -= 1
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = {}
    lower_word = word.lower()
    for letter in hand:
        new_hand[letter] = hand[letter]
    for letter in lower_word:
        value = new_hand.get(letter, 0)
        if value == 1:
            del(new_hand[letter])
        elif value > 1:
            new_hand[letter] = new_hand[letter] - 1
    return new_hand


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    lower_word = word.lower()
    if lower_word not in word_list:
        if "*" in lower_word:
            wildcard_word_match = False
            wildcard_index = lower_word.find("*")
            for vowel in 'aeiou':
                replaced_word = lower_word[0:wildcard_index] + vowel + \
                    lower_word[wildcard_index+1:len(lower_word)]
                if replaced_word in word_list:
                    wildcard_word_match = True
            if wildcard_word_match == False:
                return False
        else:
            return False
    hand_dict = {}
    for letter in hand:
        hand_dict[letter] = hand[letter]
    for letter in lower_word:
        hd_value = hand_dict.get(letter, 0)
        if hd_value == 0:
            return False
        else:
            hand_dict[letter] -= 1
    return True


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handlen = 0
    for letter in hand:
        handlen += hand[letter]
    return handlen

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    total_score = 0
    word_count = 0
    hand_length = calculate_handlen(hand)
    while hand_length > 0:
        hand_display = " "
        for letter in hand:
            hand_display += (letter + " ") * hand[letter]
        print("Current Hand:", hand_display.strip())
        if word_count == 0:
            hand = sub_prompt(hand)
        word = input("Enter word, or \"!!\" to indicate that you are finished: ")
        if word == "!!":
            print("Total score for this hand:", total_score, "points")
            break
        else:
            if is_valid_word(word, hand, word_list):
                word_score = get_word_score(word, hand_length)
                total_score += word_score
                word_count += 1
                print('"' + str(word) + '"' + " earned " + str(word_score) + \
                      " points. Total: " + str(total_score) + " points")
                hand = update_hand(hand, word)
                hand_length = calculate_handlen(hand)
            else:
                print("That is not a valid word. Please choose another word.")
            print("")
    if hand_length == 0:
        print("Ran out of letters. Total score for this hand:", total_score, "points")
    
    return total_score


def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    if letter in hand.keys():
        new_hand = {}
        old_letter = letter
        replacement_letter = ""
        letters = VOWELS + CONSONANTS
        while replacement_letter == "":
            new_letter = random.choice(letters)
            if new_letter not in hand.keys():
                for letter in hand:
                    if letter != old_letter:
                        new_hand[letter] = hand[letter]
                new_hand[new_letter] = hand[old_letter]
                replacement_letter = new_letter
        return new_hand
    else:
        return hand
    
def sub_prompt(hand):
    sub = ""
    while sub not in ["y", "n", "yes", "no"]:
        sub = input("Would you like to substitute a letter? ")
        if sub == "y" or sub == "yes":
            while True:
                replace = input("Which letter would you like to replace: ")
                letters = VOWELS + CONSONANTS
                if len(replace) == 1 and replace in letters:
                    if replace not in hand.keys():
                        print("Letter not in hand.")
                    else:
                        hand = substitute_hand(hand, replace)
                        break
                else:
                    print("Invalid letter input")
            hand_display = " "
            for letter in hand:
                hand_display += (letter + " ") * hand[letter]
        elif sub == "n" or sub == "no":
            pass
        else:
            print("Please enter yes or no.")
    hand_display = " "
    for letter in hand:
        hand_display += (letter + " ") * hand[letter]
    print("")
    print("Current Hand:", hand_display.strip())
    return hand

def get_num_hands():
    while True:
        try:
            num_hands = int(input("Enter total number of hands: "))
            if num_hands > 0:
                return num_hands
            else:
                print("Please enter a number greater than zero.")
        except:
            print("Invalid entry. Please enter a number.")

def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    num_hands = get_num_hands()
    total_score = 0
    while num_hands > 0:
        hand = deal_hand(HAND_SIZE)
        hand_score = play_hand(hand, word_list)
        print("---------")
        replay = ""
        while replay not in ["yes", "no"]:
            replay = input("Would you like to replay the hand? ")
            if replay == "yes":
                hand_score = play_hand(hand, word_list)
            elif replay == "no":
                total_score += hand_score
                num_hands -= 1
    print("---------")
    print("Total score over all hands:", total_score)
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
