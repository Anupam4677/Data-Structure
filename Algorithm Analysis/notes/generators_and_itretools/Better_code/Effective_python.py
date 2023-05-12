# 1. Consider Generators instead of returning list 

# simple choice of function that produces a seq of result is to return a list item 
# i.e Find the index of every word in a string 

address = "Four score and seven years ago . . ."
def index_word(text):
    result = []
    if text:
        result.append(0)
    for index,letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result

index_word(address)

# there are 2 problems with the function 
# 1. dense and noicy- each new result is found , we use append function 
# generators are produced by functions that use yield expression 
def index_word_iter(text):
    if text:
        yield 0
    for index , letter in enumerate(text):
        if letter == ' ':
            yield index+1
    

# when called , a generator function dosent actually run but return an iterator 
it = index_word_iter(address) 

# with each call to the next buildin function , the iterator advances the generator to its next yield expression
print(next(it))
print(next(it))
print(next(it))
result =  list(index_word_iter(address))
print(result)

# 2. the second prob iis that it requires all result to be stored in a list befor being retuned 
# for huge inputs it can cause a program to run out of memory and crash 
# in contrast, a generator version of this function can easily be adapted to take inputs of arbitary length 
# --due to its bound memory requirement 


# Things to remember
# using a generator can be clearer than the alternative of having a function return a list of accumulated result 
# The iterator returned by a generator produces a set of values passed to yield expression within gen func body
# Gen can produce seq of outputs for arbitary large inputs becausethere working memory dosnet include all inputs and outputs 
