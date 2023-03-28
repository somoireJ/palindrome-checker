def is_palindrome(word):
    """
    Returns True if a word is a palindrome, False otherwise.
    """
    return word == word[::-1]

with open("words_in_english_dictionary.txt", "r") as f:
    for line in f:
        word = line.strip()
        if is_palindrome(word):
            print(word, "is a palindrome!")