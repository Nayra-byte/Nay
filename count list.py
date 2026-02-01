def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word [0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("The list of words with the first and last character are")
    return ctr
count = match_words(['242', 'ghj','282','585','283','abc','nan','nnn'])
print("And the number of words are.................",count," words")
