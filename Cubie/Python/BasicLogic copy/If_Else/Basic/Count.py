def letter():
    while True:
        letter = input("Enter a letter: ").lower()
        if len(letter) == 1 and letter.isalpha():
            return letter
        print("Please enter exactly one alphabetic character.")
        
def word():
    while True:
        word = input("Enter a word: ").strip().lower()
        if word.isalpha():
            return word
        print("Please enter an appropriate word.")

def collect():
    l = letter()
    w = word()
    return l, w

def checking():
    l, w = collect()
    count = 0
    for i in w:
        if i == l:
            count += 1
        
    print(f"There {'is' if count == 1 else 'are'} {count} {l}{''if count == 1 else's'} within the word {w}")
    return count

checking()

