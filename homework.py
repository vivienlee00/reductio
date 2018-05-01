#Vivien Lee
#Softdev2 pd7
#K18 -- Reductio ad Absurdum
#2018-04-30

from functools import reduce

#read text file, remove line breaks and empty strings
tempest = open('thetempest.txt', 'r')
tempest_words = tempest.read().replace("\n", " ").split(" ")
tempest_words = filter(None, tempest_words)

def word_frequency(word):
    #remove punctuation, uppercase letters
    #add 1 for each occurance of the word
    count = [1 for x in tempest_words if word.lower() == x.lower().strip("?!.,_[]")]
    if len(count) != 0:
        return reduce((lambda x, y: x + y), count)
    else:
        return 0

#print word_frequency("Prospero")

def group_word_frequency(words):
    #only works with lists !!
    #find frequency for each word in list
    counts = [word_frequency(x) for x in words]

    #sum counts for each word in list
    count = reduce((lambda x, y: x + y) , counts)
    return count

#print group_word_frequency(["Prospero", "the", "yolo"])

def most_frequent_word():

    #creates a set of all words in The Tempest -- no repeating words
    words = {x for x in tempest_words}
    counts = [word_frequency(x) for x in words]
    return max(counts)

#print most_frequent_word()
#takes very long.
#it's "the".
