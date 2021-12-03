# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:34:36 2021

@author: harun adiyaman
"""

def text_reader(f):
    '''Takes the file location as an argument 'f', reads the file and returns the content as a string'''
    file = open(f ,'r') #open file
    text = file.read() #read file onto string
    file.close() #close file
    return text #return string

def punc_remove(text):
    '''Takes a string as an argument, and removes all punctuation marks. Returns string without punctuation marks'''
    punc_list = [",",";",":",".","?","!","[",
                 "]","*","(",")","-","'",'"'] #list of punctuation marks
    newstr = [] #empty list
    for t in text:
        newstr.append(t)#adds each letter to new list
        for p in punc_list:
            if t == p: #if an element in the string matches anything in the punc_list, it is removed from the new list
                newstr.remove(t)
    return ''.join(newstr) #joins the list into a string and returns

def sentence_counter(text):
    '''Takes a string as an argument and returns the number of sentences'''
    snt_endrs = ['.', '?', '!'] #list of sentence enders
    counter = 0 #initialize number of sentences
    for t in text:
        for p in snt_endrs:
            if t == p: #Essentially counts the number of sentence enders within the string and adds one to 'counter'
                counter += 1   
    return counter #returns number of sentences

def dict_words(text):
    '''Takes a string as an argument and returns a dictionary with each word and it's frequency within the string'''
    wordlist = text.split() #creates a list of parameter string
    word_freq = [] #empty list of word frequencies
    wrd_frq = {} #dictionary of word frequencies
    complist = [] #comparative list to compare duplicate words
    for x in wordlist:
        if x not in complist: #for every element in the string, if it is not already in complist, append it to complist
            complist.append(x)
    for t in complist: #for every element in complist, count the number of times it occurs in the original string, and append that count to word_freq list
        count = 0
        for f in wordlist:
            if t == f:
                count += 1
        word_freq.append(count)
    for i, x in enumerate(complist):
        wrd_frq[x] = word_freq[i] #creates the dictionary with the words as keys and frequencies as the values
    return wrd_frq #returns the dictionary

def avg_word(text):
    '''Takes a string as an argument and returns both the total number of words, and total number of unique words'''
    wordlist = text.split() #creates a list of parameter string
    uniqword = [] #empty list of each unique word
    for x in wordlist:
        if x not in uniqword: #if an word in the string is not in uniqword list, then append it to uniqword
            uniqword.append(x) 
    numword = len(wordlist) #number of total words is length of wordlist
    numuniq = len(uniqword) #number of total unique words is length of uniqword
    return numword, numuniq #return ints of num of words and unique words
                
def output(sentences, words, uniqwords, wordfreq={}):
    '''Takes the number of sentences, words, unique words, and a dictionary containing each word and its frequency as an agrument
    and outputs this infomation in an organized manner'''
    print("Number of sentences: {}".format(sentences)) #print num of sentences
    print("Number of words: {}".format(words)) #print num of words
    print("Number of unique words: {}".format(uniqwords)) #print num of unique words
    print("The 15 most common words:") 
    sortdict = dict(sorted(wordfreq.items(), key=lambda item: item[1], reverse=True)) #sorts the dictionary by ascending value
    count = 0
    for i in sortdict:
        count+=1
        print(i, sortdict[i]) #prints each element in the sorted dictionary
        if count == 15:
            break #once it prints 15 elements, stop printing/break from loop
    