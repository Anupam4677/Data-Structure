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


