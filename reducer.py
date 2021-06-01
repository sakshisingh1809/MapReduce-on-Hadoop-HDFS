"""reducer.py"""

import sys
import nltk
import string

freq ={} #empty dictionary to store words and their counts

for line in sys.stdin: #input comes from STDIN
    
    stopwords = nltk.corpus.stopwords.words('english')+list(string.punctuation) #list of words to be filtered out
    porter = nltk.stem.porter.PorterStemmer() 
    line = line.strip() #remove leading and trailing whitespace
    word = line.split('\t', 1) #parse the input we got from mapper.py
    
    word = [w.lower() for w in word] #convert to lower case
    word = [word for word in word if word.isalnum()] #remove isalnum
    word = [word for word in word if not word.isdigit()] #remove digits
    word = [word for word in word if not word in stopwords] #remove stopwords
    word = [porter.stem(word) for word in word] #stem words
    
    for w in word: #for each word
        if w in freq: #if the word exists in dictionary, then increment
            freq[w] +=1 #increment counter
        else:
            freq[w] = 1 #the word is encountered first time in dictionary

for key in freq: #print result
    print(key,'\t',freq[key]) #write result to STDOUT
    
print("\nTop 10 occuring words are:")
sorted_list = sorted(freq.items(), key=lambda keyvalue:keyvalue[1], reverse=True)[0:10] #sort dictionary in reverse order
for i in sorted_list:
    print(i)


