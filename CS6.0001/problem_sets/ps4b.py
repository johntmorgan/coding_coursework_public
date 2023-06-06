# Problem Set 4B
# Name: John "JMo" Morgan
# Collaborators: None

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'ps4_words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        word_list = load_words(WORDLIST_FILENAME)
        word_array = text.lower().split(" ")
        valid_words = []
        for word in valid_words:
            if is_word(word_list, word):
                word_array += [word]
        self.valid_words = word_array

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        shift_dict = {}
        upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in upper_chars:
            shift_dict[char] = upper_chars[(upper_chars.index(char) + shift) % 26]
        lower_chars = "abcdefghijklmnopqrstuvwxyz"
        for char in lower_chars:
            shift_dict[char] = lower_chars[(lower_chars.index(char) + shift) % 26]
        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        letter_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        encrypted_message = ""
        for char in self.message_text:
            if char in letter_chars:
                encrypted_message += shift_dict[char]
            else:
                encrypted_message += char
        return encrypted_message

    def __str__(self):
        return "Testing"

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_shift = 0
        best_shift_words = 0
        letter_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        word_list = load_words(WORDLIST_FILENAME)
        for shift in range(26):
            possible_decrypted_text = self.apply_shift(shift)
            punct_strip_decrypted_text = ""
            for char in possible_decrypted_text:
                if char in letter_chars or char == " ":
                    punct_strip_decrypted_text += char
            decrypted_word_array = punct_strip_decrypted_text.split(" ")
            valid_words = 0
            for word in decrypted_word_array:
                if is_word(word_list, word):
                    valid_words += 1
            if valid_words > best_shift_words:
                best_shift = shift
                best_shift_words = valid_words
        return (best_shift, self.apply_shift(best_shift))

if __name__ == '__main__':

    # Just in case a future employer looks at this:        
    # I'm slacking on the tests for the sake of moving forward fast
    # Would not do in production code, but for a review course... yes!
    # Ask me about the ~80k tests written in rspec for Sparkmesh!
    failure = False
    message = Message("Test message text")
    if message.get_message_text() != "Test message text":
        print('FAILURE: message message_text attribute not set')
        print('Expected output:', "Test message text")
        print('Actual output:', message.get_message_text())
        failure = True
    if message.get_valid_words() != ["test", "message", "text"]:
        print('FAILURE: message valid_words attribute set wrrong')
        print('Expected output:', ["test", "message", "text"])
        print('Actual output:', message.get_valid_words())
        failure = True
    # Ensure copy returned
    valid_words = message.get_valid_words()
    valid_words += ["badadd"]
    if "badadd" in message.get_valid_words():
        print('FAILURE: returned actual list and mutated it')
        failure = True
    shift_dict = message.build_shift_dict(5)
    if len(shift_dict) != 52 or shift_dict['C'] != 'H' or \
        shift_dict['c'] != 'h' or shift_dict['Z'] != 'E' or \
        shift_dict['z'] != 'e':
        print('FAILURE: shift dict not built')
        failure = True
    encrypted_message = message.apply_shift(5)
    if encrypted_message != "Yjxy rjxxflj yjcy":
        print("FAILURE: basic message not encoded")
        failure = True
    punct_message = Message("Testing, so much testing!")
    punct_encrypted_message = punct_message.apply_shift(10)
    if punct_encrypted_message != "Docdsxq, cy wemr docdsxq!":
        print("FAILURE: punctuated message not encoded")
        failure = True

    plaintext = PlaintextMessage('hello', 2)
    if plaintext.get_message_text_encrypted() != "jgnnq":
        print('Expected Output: jgnnq')
        print('Actual Output:', plaintext.get_message_text_encrypted())
        failure = True
    plaintext.change_shift(4)
    if plaintext.get_message_text_encrypted() != "lipps":
        print('Expected Output: lipps')
        print('Actual Output:', plaintext.get_message_text_encrypted())
        failure = True 
    ciphertext = CiphertextMessage('jgnnq')
    if ciphertext.decrypt_message() != (24, 'hello'):
        print('Expected Output:', (24, 'hello'))
        print('Actual Output:', ciphertext.decrypt_message())
        failure = True 
    ciphertext_2 = CiphertextMessage("Docdsxq, cy wemr docdsxq!")
    if ciphertext_2.decrypt_message() != (16, "Testing, so much testing!"):
        print('Expected Output:', (16, "Testing, so much testing!"))
        print('Actual Output:', ciphertext_2.decrypt_message())
        failure = True
    if failure == False:
        print("Message loading works!")

    encrypted_text = CiphertextMessage(get_story_string())
    decrypted_text = encrypted_text.decrypt_message()
    print(decrypted_text)
    
    # (12, 'Jack Florey is a mythical character created on the spur of a 
    # moment to help cover an insufficiently planned hack. He has been 
    # registered for classes at MIT twice before, but has reportedly never 
    # passed a class. It has been the tradition of the residents of East 
    # Campus to become Jack Florey for a few nights each year to educate 
    # incoming students in the ways, means, and ethics of hacking.')
    
