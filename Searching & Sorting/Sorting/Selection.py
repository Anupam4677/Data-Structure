# Logic -1 
# selection sort improves the bubble sort by making only one exchange at every pass
# a selection sort looks for the largest value and place it in its place 
# as in bubble chart after the ist pass the largest item is at it place, 2nd pass the next largest is at its place
# requires n-1 pass t sort n elements

alist = [54,26,93,17,77,31,44,55,20]
def selection_sort(alist):
    # for element in range(len(alist)-1,0,-1):
     for i in range(0,len(alist)-1):
        # print('i:',i)
        curr_min_index = i
        for j in range(i+1,len(alist)):
            print('j:',j)
            if alist[curr_min_index] > alist[j]:
                # print('current_min:',alist[curr_min_index])
                # print('compare:',alist[curr_min_index],alist[j])
                curr_min_index = j
                # print('new_min:',alist[curr_min_index])
        # print('before:',alist)
        alist[curr_min_index],alist[i] = alist[i] ,alist[curr_min_index]
        # print('After:',alist)

        # return alist

            

          

          
  

selection_sort(alist)
print(alist)