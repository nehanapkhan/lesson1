def match_words(words):
    ctr = 0
    list =[]
    for word in words:
         if len(word)>1 and word[0] == word[-1]:
              ctr= ctr+1
              list.append(word)
    print("list of the words with first and last character same \n",list)

    return ctr

count = match_words(['abc','cfc','xyz','aba','1221'])
print("number of words having first and last charcter same",count)          