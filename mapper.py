"""mapper.py"""

import sys
import nltk

for line in sys.stdin: #input comes from STDIN 
    print(line)
    line = line.strip() #remove leading and trailing whitespace
    tokenize_words = nltk.tokenize.word_tokenize(str(line)) #tokenize into words

    for word in tokenize_words: #iterate through each token
        print('%s\t%s' % (word, 1)) #write the results to STDOUT 

