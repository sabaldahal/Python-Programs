from urllib.request import urlopen
import os

url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

all_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def has_alphabets(word, string):
    """ 
    checks if the word in the dictionary contains the exact same alphabets 
    passed in the string
    order does not matter
    """
    a = len(string)
    if a == 0:
        return True
    else:
        if string[0] in word:
            word = word.replace(string[0], '', 1)
            return True and has_alphabets(word, string[1:])
        else:
            return False


def list_alphabets(string):
    """
    return an array containing the anagram words for string

    """
    anagram = []
    for word in words:
        if(len(word) != len(string)):
            continue
        else:
            check = has_alphabets(word, string)
            if check:
                anagram.append(word)
    return anagram


def step(a):
    """ 
        concatanate (a) with all alphabets in each iteration
        return an array containing all the anagram words for
        string a + alpbhabets

    """
    anagram = []
    a = a.upper()
    for alphabet in all_alphabet:
        b = a + alphabet
        anagram = anagram + list_alphabets(b)
    return (anagram)

# Run test program


def test():
    x = step('APPLE')
    y = step('orange')
    z = step('mango')

    print(x)
    print(y)
    print(z)


if __name__ == "__main__":
    test()
