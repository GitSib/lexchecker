# -*- coding: utf-8 -*-

import nltk
import pymorphy2
import codecs
import re

Morph = pymorphy2.MorphAnalyzer()
FinalSentence = []

"""
----- Creating list of lexical minimum -----
"""


def LexicalMinimumList(LexicalMinimumListFileName):
    LexicalMinimum = []

    fp = open(LexicalMinimumListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        LexicalMinimum.append(word)
        line = fp.readline()
    fp.close()
    return LexicalMinimum

"""
----- Sentences tokenization -----
Text from file -> list of sentences
"""


def SentenceCutter(FullText):
    ListofSentences = nltk.PunktSentenceTokenizer().tokenize(FullText)
    for s in ListofSentences:
        WordCutter(s)

"""
----- Words tokenization -----
List of sentences -> List of words
"""


def WordCutter(Sentence):
    ListofWords = re.split(r'[\s+\t\n\.\|\:\/\,\?\!\"()]+', Sentence)
    for w in ListofWords:
        Lemmatization(w)

    SentenceChecker(FinalSentence)

    del FinalSentence[:]
    return

"""
----- Lemmatization -----
Word from list of words -> ["word", "POS", "lemma"]
"""


def Lemmatization(Word):
    WordObject = []
    WordObject.append(Word)
    Word = Word.lower()
    try:
        WordinWork = Morph.parse(Word)[0]
        WordObject.append(WordinWork.tag.POS)
        WordObject.append(WordinWork.normal_form)
        FinalSentence.append(WordObject)
    except IndexError:
        return

"""
----- Checking sentence -----
Lemma -> yes/no
If no, then count += 1
"""


def SentenceChecker(Sentence):
    count = 0
    for OneWord in Sentence:
        if OneWord[2] in LexicalMinimum:
            continue
        else:
            count += 1

    if count > 1:
        print u"Complicate sentence"
    else:
        print u"Simple sentence"

"""
----- Data -----
"""


LexMin = codecs.open('Data/lexmin.txt', 'r', 'utf-8')
LexicalMinimum = LexMin.read()

TextFile = codecs.open('Data/corpus.txt', 'r', 'utf-8')
Text = TextFile.read()

#For loading data from file please uncomment and edit following strings
#import csv
#Text = csv.reader(open('Data/file.csv', 'rb'), delimiter='', quotechar = '')

SentenceCutter(Text)
