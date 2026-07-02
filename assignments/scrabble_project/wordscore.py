"""wordscore.py: Module providing a function returning score for a given word for Scrabble game"""

def score_word(word: str):
    """
    Calculate the score for a given word based on the Scrabble score dictionary
    
    Args:
        word (str): The word for which to calculate the score
        
    Returns:
        int: the score for the word
    """
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10}

    return sum(scores[letter.lower()] for letter in word)
