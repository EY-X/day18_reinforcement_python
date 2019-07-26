
def word_counter(string): 
    words_list = []
    
    for words in string: 
        string_x = string.split()
        if words == None: 
            return 0  
        else: 
            for word in string_x:  
                words_list.append(word)
        
        return len(words_list)