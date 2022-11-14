# its a divide an conquer algorithm 
# breaks down problem into multiple subproblems recurcively untill they become simple to solve 
# solutions are combind to solve original problem 
# principle :
# 1. split the array into half 
# 2. Call merge sort on each half to sort them recursively
#  arr = [2,6,5,1,7,4,3]
 # divide the arr1 = [2,6,5,1], arr2 = [7,4,3]
# This dividing goes recursively
# divide arr1: arr1.1 = [2,6],arr1.2 = [5,1]

# dividing will go on till all the subarray has only one entry left 
# now start merging all the subarray 
arr = [2,6,5,1,7,4,3]
def merge_sort(arr):
    if len(arr) > 1:
        left_arr= arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion 
        merge_sort(left_arr)  
        merge_sort(right_arr)  

        # merge
        # comapre leftmost element of ist array with left most element of another array 
        i = 0 # left array index 
        j = 0 # right array index 
        k = 0 # merged array index 
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1 # in both the cases we have to increment k so we pull it out 
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1








blist = [54,26,93,17,77,31,44,55,20]
merge_sort(blist)
print(blist)
