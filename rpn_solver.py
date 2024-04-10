#Maya Akins
#1001651922
#Turned in on October 20th, 2023 @4:20pm 
#MacOS
#Python 3.11.6
#CSE 3302 - TTH 3:30 section
#RPN (Reverse Polish Notation) Calculator using Python

import os
from collections import deque

def invalidNotation():      #Function that pushes message to the stack 
    stack.append("Invalid Notation!")

def ifEmpty():              #returns True if stack is EMPTY 
    if len(stack) == 0:
        return True

f = open("input_RPN.txt","r")       #opening file

while 1:     #while there are still lines in the text file 
    expression=f.readline()     #saving current line into expression
    if bool(expression) == False:       #if end of file quit 
        break
    lineLength = len(expression)      #getting length of the current line 
    stack = deque()
    printedstring=expression
    for x in range(0,lineLength):       #for every token in the current line
        if expression[x] == "+" :       #if ADDITION
            if ifEmpty()== True:
                invalidNotation()
                break                   #break and go to next line
            x2 = stack.pop()            #POP
            if ifEmpty()== True:
                invalidNotation()
                break
            x1 = stack.pop()            #POP
            sum = int(x1) + int(x2)     #calculate
            stack.append(str(sum))

        elif expression[x] == "-" :     #if SUBTRACTION
            if ifEmpty()== True:
                invalidNotation()
                break
            x2 = stack.pop()
            if ifEmpty()== True:
                invalidNotation()
                break
            x1 = stack.pop()
            difference = int(x1) - int(x2)
            stack.append(difference)

        elif expression[x] == "/" :     #if DIVISION
            if ifEmpty()== True:
                invalidNotation()
                break
            x2 = stack.pop()
            if ifEmpty()== True:
                invalidNotation()
                break
            x1 = stack.pop()
            quotient= int(x1) / int(x2)
            stack.append(quotient)

        elif expression[x] == "*" :     #if MULTIPLICATION 
            if ifEmpty()== True:
                invalidNotation()
                break
            x2 = stack.pop()
            if ifEmpty()== True:
                invalidNotation()
                break
            x1 = stack.pop()
            product = int(x1) * int(x2)
            stack.append(product)

        elif expression[x] == " " :     #allows program to pass all spaces : " "
           continue
        
        else:                           #else PUSH number on stack
            stack.append(expression[x])

        if expression[x] == "\n":       #if at the end of current line
            stack.pop()                 #POP \n
            lastPop = stack.pop()       #POP the answer of the expression, but save it 
            if ifEmpty() != True:       #if the stack is not empty then there were extra numbers
                stack.clear()           #clearing stack to add invalid message to stack
                invalidNotation()   
            else:
                stack.append(lastPop)   # add the last value that was popped 

    print(str(stack[0]))
    
f.close()
   


