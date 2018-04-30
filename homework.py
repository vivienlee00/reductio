#Vivien Lee
#Softdev2 pd7
#K18 -- Reductio ad Absurdum
#2018-04-30

from functools import reduce

#read text file, remove line breaks and empty strings
tempest = open('thetempest.txt', 'r')
tempest_lines = tempest.read().replace("\n", " ").split(" ")
tempest_lines = filter(None, tempest_lines)

def word_frequency(word):
    #remove punctuation, uppercase letters
    #add 1 for each occurance of the word
    count = [1 for x in tempest_lines if word.lower() == x.lower().strip("?!.,_[]")]
    if len(count) != 0:
        return reduce((lambda x, y: x + y), count)
    else:
        return 0

#print word_frequency("Prospero")

def group_word_frequency(words):
    counts = [word_frequency(x) for x in words]
    count = reduce((lambda x, y: x + y) , counts)
    return count

print group_word_frequency(["Prospero", "hi", "hey"])
