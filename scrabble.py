"""scrabble.py:  Module providing a function returning all valid Scrabble words that 
can be made from inputted rack, plus their associated scores"""

from wordscore import score_word

def run_scrabble(rack: str):
    """
    Find all valid Scrabble words that can be made from inputted rack, plus their associated scores
    
    Args:
        rack (str): The inputted rack of letters for Scrabble containing 2 to 7 letters (or wildcards)
        
    Returns: 
        Tuple(valid_words, len(valid_words)): A tuple containing:
        - List of valid word tuples, which each contain the score and the word in uppercase
            - Sorted by score, then alphabetically
        - The total number of valid words (an integer)
        OR
        Error Message (if any)
    """

    # Error Handling: Check if the inputted string is between 2 and 7 characters:
    if len(rack) > 7 or len(rack) < 2:
        return "Error: The Rack must contain between 2 and 7 letters or wildcards (*,?)"

    # Error Handling: Check if there are invalid characters within the rack:
    invalid_characters = set(rack.lower()) - set("abcdefghijklmnopqrstuvwxyz*?")
    if len(invalid_characters) > 0:
        return f"Error: The rack must only contain letters or wildcards but you inputted {invalid_characters}"

    # Error Handling: Check if the inputted string contains more than 2 valid wildcards:
    if rack.count("*") > 1 or rack.count("?") > 1:
        return "Error: You cannot input more than 2 wildcards, one ? and one *"

    # Load Scrabble dictionary:
    with open("sowpods.txt", "r") as infile:
        raw_input = infile.readlines()
        scrabble_dict = [datum.strip('\n').upper() for datum in raw_input]

    # Core of function - valid word finder:
    valid_words = []
    for word in scrabble_dict:
        rack_letters_remaining = list(rack.upper())
        rack_letters_used = []
        for letter in word:
            if letter in rack_letters_remaining:
                rack_letters_used.append(letter)
                rack_letters_remaining.remove(letter)
            elif '*' in rack_letters_remaining:
                rack_letters_remaining.remove('*')
            elif '?' in rack_letters_remaining:
                rack_letters_remaining.remove("?")
            else:
                break
        else:
            valid_words.append((score_word(rack_letters_used), word))

    # Sort the found words by score (use - symbol for reverse order), then alphabetically:
    valid_words.sort(key=lambda x: (-x[0], x[1]))

    # Return:
    # 1) The total list of valid Scrabble words that can be constructed from the rack as (score, word) tuples, 
    #    sorted by the score and then by the word alphabetically
    # 2) The total number of valid words as an integer
    return valid_words, len(valid_words)
