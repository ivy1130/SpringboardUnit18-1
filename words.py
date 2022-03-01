def print_upper_words(words):
    """
    Given a list of words, it will print out each word on a separate line, but in all uppercase.
    """

    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])



def print_e_words(words):
    """
    Given a list of words, it will print out only the words that start with the letter ‘e’ (either upper or lowercase).
    """

    for word in words:
        if word[0] in 'eE':
            print(word.upper())

print_e_words(["hello", "hey", "eggs", "bacon", "elephant"])



def print_certain_words(words, must_start_with):
    """
    Given a list of words, you are able to pass in a set of letters, and it will only prints words that start with one of those letters.
    """

    for word in words:
        if word[0] in must_start_with:
            print(word.upper())

print_certain_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})