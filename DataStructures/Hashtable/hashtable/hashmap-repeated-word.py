from hashtable.hashtable   import HashTable
import re

def repeated_word(text):
    """
        Write a function called repeated word that finds the first word to occur more than once in a string
        Arguments: string
        Return: string

    """
    hashtable = HashTable()
    words = list(map(lambda word : word.lower(), re.findall(r"\w+", text)))
    if len(list(words)) <= 1:
        raise Exception("String provided contains an invalid number of keys.")
    for word in words:
        if hashtable.contains(word):
            return word
        hashtable.set(word, None)
    return 

