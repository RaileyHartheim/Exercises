def search_for_vowels(phrase:str) ->set:
    """function returns vowels that were found in typed word"""
    vowels = set("aeiou")
    return vowels.intersection(set(phrase))

def search_for_letters(phrase: str, letters:str="aeiou") ->set:
    """"function returns a set of letters from "letters" set that were found in typed phrase"""
    return set(letters).intersection(set(phrase))