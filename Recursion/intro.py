# Recursion is a method of solving problem that involves breaking the prob down to smaller and smaller sub-prob
# Untill you get a small enugh problem you can solve trivilaay 

# calculating sum of list of a no 
# the iterative way to solve the problem 
# alist = [1,3,5,7,9]
# def listSum(alist):
#     theSum = 0
#     for i in alist:
#         theSum += i
#     return theSum
# res = listSum(alist)
# print(res)

# if we dont have for or while loop
# the list can be written and added as :
# (1+(3+(5+(7+9))))
# (1+(3+(5+(16))))
# (1+(3+(21)))
# (1+24)
# 25
alist = [1,3,5,7,9]
def listSum(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return alist[0] + listSum(alist[1:])
        1+[3,5,7,9]
res = listSum(alist)
print(res)


#  [1] + listSum([3,5,7,9]) # 25
#          [3] + listSum([5,7,9]) #24
#                   [5] + listSum[7,9] #21
#                         [7] + list[9] # 16


# Lows of recursion :
# A recursion algorithm must have a base case  
## Base case in a condition that allows the algorithm to stop recursively 
## The chnage in state means that some data the algorithm is using is modifed

# A recurcise algo must change its state and move towards the base case 
## ususlly the data which represnts our prob get smaller
## in above ex our primary data structure is a list so we must focus on state changing effor on list 
## since the base case is list lenghth 1 , natural progression toward the base case is to shorten the list 

# A recursive algorithm must call it self recurcively 
# Final law is the algorithm to call itself


# Converting integer to a string in Any base
