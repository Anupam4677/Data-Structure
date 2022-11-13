# maintains  sorted sublist in the lower position of the list 
blist = [54,26,93,17,77,31,44,55,20]

[54,26,93,17,77,31,44,55,20] # assume 54 is sorted list of 1 item
[26,54,93,17,77,31,44,55,20]  #inserted 26 
[26,54,93,17,77,31,44,55,20]  #inserted 93
[17,26,54,93,77,31,44,55,20]  #inserted 17
[17,26,54,77,93,31,44,55,20]  #inserted 77
[17,26,31,54,77,93,44,55,20]  #inserted 31
[17,26,31,44,54,77,93,55,20]   #inserted 44
[17,26,31,44,54,55,77,93,20]   #inserted 55
[17,20,26,31,44,54,55,77,93]   #inserted 20

def insertion_sort(alist):
    for index_insertion in range(1,len(alist)):
        current_value = alist[index_insertion]
        position = index_insertion
        while position > 0 and alist[position-1] > current_value:
            alist[position] = alist[position-1]
            position = position-1
        alist[position] = current_value
    return alist
res = insertion_sort(blist)
print(res)
# for loop 1 to 8 
# for loop index_insertion = 1 ---current value = 26, position = 1
# while loop - as position is greater than 0 and 54 > 26 --  exchange and position = 0 - Get out of loop 
# outcome = [26,54,93,17,77,31,44,55,20]  #inserted 26 

# for loop index_insertion = 2 ---current value = 93, position = 2
# position > 0 but 54 is not greater than 93
# outcome = [26,54,17,93,77,31,44,55,20]  #inserted 93 17 and 93 swapped
# again the position > 0 and 54 > 17
#outcome = [26,17,54,93,77,31,44,55,20]  #inserted 17 and 54  swapped

# for loop index_insertion = 3 ---current value = 17, position = 3
# position > 0 but 93 > 17
# switch will happen [26,54,17,93,77,31,44,55,20] and position = 2

# it will go on till the position > 0

