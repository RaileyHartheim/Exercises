word = input("Provide  a word to search for vowels: ")
vowels = set('aeiou')
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)