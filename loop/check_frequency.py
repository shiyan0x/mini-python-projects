def longest_word(list):
    largest = 0
    Lword = {}
    for word in list:
        print(f"{word} : {len(word)}")
        current = len(word)
        if current > largest:
            largest = current
    for char in word:
        if char in Lword:
            Lword[char] += 1
        else:
            Lword[char] = 1
    
    print(f"largest word is {word} : {current}")
    print(Lword)
    
    

  
list2 = ["hello", "friends", "compatibility", "auxillary-controls"]
longest_word(list2)






def longest_word(list):
    largest = 0
    Lword = {}
    for word in list:
        print(f"{word} : {len(word)}")
        current = len(word)
        if current > largest:
            largest = current
            listw = word
    for char in listw:
        if char in Lword:
            Lword[char] += 1
        else:
            Lword[char] = 1
    
    print(f"largest word is {word} : {current}")
    print(Lword)
    
  
list2 = ["hello", "friends", "compatibility", "auxillary-controls"]
longest_word(list2)