# List,Set,Dict comprehension

# list comprehension allows you to concisely form a new list :
# by filterting elements of a collection
# transforming the element passing the filter in one concise expression
# [expr for val in collection if condition]

strings_d = ['a','as','erf','ed','io','erty']
def str_filter(strings):
    result = []
    for word in strings:
        if len(word)<=2:
            wrd_upper = word.upper()
            result.append(wrd_upper)
    return result
res = str_filter(strings_d)
print(res)
# list comprhension
comp_res = [word.upper() for word in strings_d if len(word) <=2]
print(comp_res)
len_set = {len(word) for word in strings_d}
#{1, 2, 3, 4}


# for set and dict comprehensions are natural extensions
# dict comprehension:
# - {key-expr for value-expr for value in collection if condition}
# set comprehension 
# {expr for value in collection if condition }
#len_list = [len(word) for word in strings_d]
#len_set = {len(word) for word in strings_d}
#set_list = set(len_list)
loc_mapping = {val:index for index,val in enumerate(strings_d)}
# {'a': 0, 'as': 1, 'erf': 2, 'ed': 3, 'io': 4, 'erty': 5}
