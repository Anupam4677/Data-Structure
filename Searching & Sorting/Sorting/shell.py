# diminishing increment sort - improves on the insertion sort by breaking into sub-lists
# each of the sublist are sorted unsig insertion sort 
# instead of breaking the list into sublist of contiguous items,the shell sort uses an increment i(gap) to create sublist

# shell sort is an algorithm that first sorts the element far apart from each other 
# It successively reduces the interval between the elements to be sorted
# elements at specific interval are sorted
# the interval between the elements are gradually decreased based on sequence used
# The performance depends on the type of seuence used 

blist = [54,26,93,17,77,31,44,55,20]
# if we take gap = 3:
#     [54,26,93,17,77,31,44,55,20] -  (54,17,44) has to be sorted

#     [17,26,93,44,77,31,54,55,20] - sublist 1 soted. Now sort(26,77,55)
#     [54,26,93,17,55,31,44,77,20] - sublist 2 soted. Now sort(93,31,20)
#     [54,26,20,17,77,31,44,55,93] - sublist 3 soted.

# elemnet 1 - Now find min all the rows of 3 sublist = [17,54,54] -  min = 17
# elemnet 2 - Now find min all the rows of 3 sublist = [26,26,26] -  min = 26
# elemnet 3 - Now find min all the rows of 3 sublist = [93,93,20] -  min = 20

# elemnet 4 - Now find min all the rows of 3 sublist = [44,17,17] -  min = 44 - 17 already taken 
# elemnet 5 - Now find min all the rows of 3 sublist = [77,55,77] -  min = 55
# elemnet 6 - Now find min all the rows of 3 sublist = [31,31,31] -  min = 31

# elemnet 7 - Now find min all the rows of 3 sublist = [54,44,44] -  min = 54 - 44 already taken
# elemnet 8 - Now find min all the rows of 3 sublist = [55,77,55] -  min = 77 - 55 already taken 
# elemnet 9 - Now find min all the rows of 3 sublist = [20,20,93] -  min = 93

# Output = [17,26,20,44,55,31,54,77,93]
blist = [54,26,93,17,77,31,44,55,20]
def shell_sort(alist):
    gap = len(alist) // 2
    print('gap:',gap)
    while gap > 0 :
        for i in range(gap,len(alist)):
            print('i:',i)
            temp = alist[i]
            print('temp:',temp)
            j = i
            print('j:',j)
            print('check:',j,' is greater than','gap:',gap ,'and' ,alist[j-gap], ' greater than ',temp)
            # print('check:',j)
            while j>=gap and alist[j-gap] > temp:
                print('compare',alist[j-gap] ,temp)
                alist[j]=alist[j-gap]
                j = j-gap
                print('pre:',alist)
            alist[j] = temp
            print('afr:',alist)
        gap = gap//2
    return alist
print(blist)
print(shell_sort(blist))

# blist = [54,26,93,17,77,31,44,55,20]
# def s_sort(blist):
#     gap = len(blist) // 2
#     while gap > 0:
#         for i in range(gap,len(blist)):
#             temp = blist[i]
#             j = i 
#             while j>= gap and blist[j-gap] > temp:
#                 blist[j] = blist[j-gap]
#                 j = j-gap
#             blist[j] = temp
#         gap = gap // 2
