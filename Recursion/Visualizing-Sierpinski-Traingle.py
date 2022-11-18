# import turtle
# # Drawing spiral with turtle graphics
# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()

# def drawSpiral(myTurtle,linelen):
#     if linelen > 0:
#         myTurtle.forward(linelen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle,linelen)

# drawSpiral(myTurtle,100)
# myWin.exitonClick()

# write a programme to find factorail of a no 

# def factorial(num):
#     output = 1
#     for i in range(1,num+1):
#         output = output * i
#     return output
# Your code goes here
# this function fac() will return us the factorial of the number n



alist = [1,3,5,7,9]
def listSum(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return alist[0] + listSum(alist[1:])
        1+[3,5,7,9]
res = listSum(alist)
print(res)
def fac(n):
    if n == 0:
        return 1 
    # recursion call
    return n*fac(n-1)  
result = fac(11)
print(result)




