# I would like you to write a program which is run on the command line.
# The program takes two arguments: the name of a file contain words,
# each separated by a newline, and a list of letters. The program should
# output the longest words from the file which can be made using the letters
# in the list.


def longest_words(words, letters):
    """Check valid words that can be made up from letters.
    :param words: List of words.
    :param letters: String of letters.
    """
    letters = {x: letters.count(x) for x in letters}  # Make dictionary
    max_min = len(letters)  # Maximum number of erases
    longest_valid_words = []  # Longest valid words according to their erases

    # Iterate words
    for word in words:
        # Create a dictionary from each word
        temp = {x: word.count(x) for x in word}
        # Get ocurrences from word if is valid
        current_word_ocurrences = check_valid(temp, letters)
        # There are ocurrences
        if current_word_ocurrences:
            if current_word_ocurrences == max_min:
                longest_valid_words.append(word)
            elif current_word_ocurrences < max_min:
                max_min = current_word_ocurrences
                longest_valid_words = [word]
                # min_word.append(word)
    return longest_valid_words


def check_valid(word, letters):
    """Take a word as a dictionary and checks that is valid.
    :param word: Word as a dictionary
    :param letters: Letters as a dictionary
    :returns: Return False if not valid or deletes performed on letters
    """
    curr_min = len(letters)  # Minimum erases set to len of letters
    # Traverse each letter in word and their occurence
    for k, val in word.items():
        # Check if the char (key) appears in letters
        if k in letters:
            # Check that there are less occurrences in val than letters
            if val > letters[k]:
                return False  # Invalid word
            curr_min -= val  # Remove char occurrences from curr_min
        # Key does not appear in letters
        else:
            return False  # Invalid word
    return curr_min  # Return len(letters) - removed occurrences


def run_main():
    """Get longest valid words that can be made up from letters."""
    words = ["aab", "cab", "abba", "abacus", "scabs", "scab", "bacca", "ab",
             "abssss", "aabbscb"]
    letters = "aabbscb"
    test = longest_words(words, letters)
    print(test)


run_main()  # run main
