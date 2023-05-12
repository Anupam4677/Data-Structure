def even_odd(num):
    if (num%2) == 0:
        return 'odd'
    else:
        return 'even'
    
ans = even_odd(13)
print(ans)

alist = [1,2,3,5,7]
# if we want the function to work for this list which has many nos. we ll use map
# map function takes a function and *iterable as parameter
# it means that it will apply even_odd() func for each num 
map(even_odd,alist)
# it will return a map object - lazy loading - momory has not been inuntiated yet 
# covert it into list to inuntiate memory 
alist = [1,2,3,5,7]
print(list(map(even_odd,alist)))
['even', 'odd', 'even', 'even', 'even']

