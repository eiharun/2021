# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:03:37 2021

@author: harun adiyaman
"""
#imports module
import TextAnalyzer as ta

#Gets the string of the output of text_reader function from the file
text = ta.text_reader(r"C:\Users\harun\OneDrive\Documents\GMU\CYSE130\ProjNo3\MLK.txt")

#Creates a new string that excludes punctuation
new_text = ta.punc_remove(text)

#Saves number of works and unique words
numwords, numuniq = ta.avg_word(new_text)#Uses string without punctuation because punctuation isn't included in words

#Outputs in an organized manner
ta.output(
    ta.sentence_counter(text),
    numwords,
    numuniq,
    ta.dict_words(new_text)#Uses string without punctuation because punctuation isn't included in words
    )