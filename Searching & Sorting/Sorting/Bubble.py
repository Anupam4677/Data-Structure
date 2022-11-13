# Logic 1:
# 3 bubble sort need to be make multiple passes through the list
# in a list in first pass 54 will be compared with 26 and there will be exchange , Then 54 will compare to 93 and no exchange
# this will happen len(alist)-1


# def bubble_Sort_firstPass(alist):
#     # first_pass = []
#     for item in range(len(alist)-1):
#         # print(item)
#         if alist[item] > alist[item+1]:
#             alist[item],alist[item+1] = alist[item+1],alist[item]
#             print(alist)

# bubble_Sort_firstPass(alist)

# Logic 2:
# now at the start of 2nd pass largest no is already at last place , Now we ll have to sort n-1 items
# it means there will ne n-2 pairs 
# Total no of passes needed n-1
alist = [54,26,93,17,77,31,44,55,20]
def bubble_Sort(alist):
    for passum in range(len(alist)-1,0,-1):
        print('passum:',passum)
        for item in range(passum):
            print('item:',item)
            if alist[item] > alist[item+1]:
                print('Compare:',alist[item],alist[item+1])
                alist[item],alist[item+1] = alist[item+1],alist[item]
                print('List:',alist)
    print('Final List:',alist)

bubble_Sort(alist)

# n-1 passes will be made to sort the list of size n 
