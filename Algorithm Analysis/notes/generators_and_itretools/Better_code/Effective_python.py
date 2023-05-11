# 1. Consider Generators instead of returning list 

# simple choice of function that produces a seq of result is to return a list item 
# i.e Find the index of every word in a string 

address = "Four score and seven years ago . . ."
result = []
if address:
    result.append(0)
for index, word in enumerate(address):
    print(index,word)