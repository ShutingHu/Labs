from string import punctuation, whitespace

book = 'origin.txt'

with open(book, 'r') as fd:
    words = fd.read().split()

def clean(word):
    cleansed = ''
    for characters in word:
        if ((characters in punctuation) or (characters in whitespace)):
            pass
        else:
            cleansed += characters.lower()
    return cleansed
        
print( "{} has {} 'words'".format(book, len([clean(word) for word in words])))
