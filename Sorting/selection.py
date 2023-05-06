# The selection sort improves on the bubble sort by only making one exchange 
# It looks for the largest value as it makes the pass and after completing the first pass the largest item is in the right place 
# As like bubble sort the largest item is at the right place after the first pass
# After the second pass the second largest item is in the right place 
# this process requires (n-1) pass to complete for n items in the list 


# solution 
#lenghth of list = 9 
alist = [54,26,93,17,77,31,44,55,20]
def Selection_sort(alist):
    for passum in range(len(alist)-1,0,-1):
        postion_max = 0
        print(f"no of pass: {passum}")
        for location in range(1,passum+1):
            print(f"location: {location}")
            
            if alist[postion_max] < alist[location]:
                print(f"compare:  {alist[postion_max]} and {alist[location]}")
                postion_max = location
                print(f"max position: {postion_max}")
        temp = alist[passum]
        print(f"temp: {temp}")
        print(f"postion_max: {alist[postion_max]}")
        alist[passum] = alist[postion_max]
        alist[postion_max] = temp
        print(f"Final LIst after {passum} pass: {alist}")
    return alist
         


answer = Selection_sort(alist)
print(answer)