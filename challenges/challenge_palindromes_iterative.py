def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if word[::-1] != word or word == "":
        return False
    return True
