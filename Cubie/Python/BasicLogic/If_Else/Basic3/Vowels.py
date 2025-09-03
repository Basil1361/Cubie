value = list("aeiou")

def checkvovels():
    x = input("Enter a letter: ")
    if len(x) > 1 or not x.isalpha():
        print("Invalid input")
    if x in value:
        print("Is a vovel")
    elif x.lower() == 'y':
        print("Vowel & Consonant at the same time")
    else:
        print("Is a consonant")
        
checkvovels()