# makes multiple pass through a list 
# It compares adjacent item and exchanges those that are not in order 
# if there are n items in the list then no of comparisions will be (n-1)
# if there are n-1 items left to be sorted means that there are n-2 pairs to be compared 
# since each pass places the next largest value at place - no of passes required will be n-1
# the smallest item will be at correct position so no furture processing is required \\

#lenghth of list = 9 
alist = [54,26,93,17,77,31,44,55,20]
def bubble_sort(alist):
    #print(f"length:{len(alist)}")
    for index in range(len(alist)-1,0,-1):
        #print(f"index:{index}")
        for i in range(index):
            #print(f"i:{i}")
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

result = bubble_sort(alist)
print(result)