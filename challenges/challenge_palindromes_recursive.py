def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if word == "" or word[0] != word[-1]:
        return False
    if len(word) <= 2:
        return True
    word = word[1:-1]
    return is_palindrome_recursive(word, 0, len(word) - 1)


word = "ANA"
print(is_palindrome_recursive(word, 0, len(word) - 1))
