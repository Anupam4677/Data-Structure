# Searching 
# Binary search 
# in python we have an easy way to do it 
print(15 in [0,3,6,8,9])

# sequential search 
blist = [54,26,93,17,77,31,44,55,20,65]
def sequentialSearch(alist,item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return (found,'At Position:',pos)
print(sequentialSearch(blist,44))


# Binary Search 
# Takes advantage when the list is ordered 
print('...........Binary Search .............................')
def binarySearch(alist,item):
    first = 0
    last = len(alist) -1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        print('first:', first,'last:',last,'midpoint:',midpoint)
        print('midpoint',midpoint)
        if alist[midpoint] == item:
            found = True
            print('found:',found)
        else:
            if item < alist[midpoint]:
                last  = midpoint - 1
            else:
                first = midpoint + 1

    return found

blist = [17,20,26,31,44,54,55,67,89,90]

print(binarySearch(blist,31))

