def matchWords(words):
    cntr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            cntr =+ 1
            lst.append(word)
        
    print("List of words that have the same first and last character: ", lst)
    return cntr

count = matchWords(['abc', 'xyz' 'aba' '121' 'cfc'])
print("Number of words with the same first and last character: ", count)
