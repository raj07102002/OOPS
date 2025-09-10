def word_frequency(sentence): 
    words=sentence.split()
    freq={} 
    for word in words: 
        freq[word]=fr.get(word,0)+1 

        return freq 
    print(word_frequency("my name is khan"))