# Although still 0(n^2) 
# It always maintains a sorted sublist in the lower position of the list 
# Each new item is then inserted back into the previous sublist 
# we begin by assuming that a list with one item (position 0) is already sorted 
# On each pass , one of each item 1 to n-1, the current itemis checked with those alreday in current sublist 
# we shift items that are greter to right 

alist = [54,26,93,17,77,31,44,55,20]
def insertion_sort(alist):
    for index in range(1,len(alist)):
    
        currentvalue= alist[index]
        position = index
      
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1] 
            position = position-1
        alist[position]= currentvalue
    return alist



answer= insertion_sort(alist)
print(answer)