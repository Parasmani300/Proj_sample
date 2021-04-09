wordfile = open("abc.txt","r")
word_line = wordfile.readlines()
list_word = []
for line in word_line:
    ll = [x.strip() for x in line.split(" ")]
    list_word = list_word + ll
wordfile.close()

symbol_file = open("symbols.txt","r")
symbol_line = symbol_file.readlines()
list_symbol = []
for line in symbol_line:
    ll = [x.strip() for x in line.split(" ")]
    list_symbol =  list_symbol + ll

symbol_file.close()


list_constants = ["buy","sell","selling","buying"]
result = []
for word in list_word:
    if word in list_constants:
        index_of_word = list_word.index(word)
        try:
            symbol = list_word[index_of_word + 1]
            if symbol in list_symbol:
                result.append(word + " " + symbol)
            list_word.remove(word)
        except:
            pass

print(result)
                

