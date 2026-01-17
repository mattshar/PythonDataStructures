
stack = []


stack.append(10)
stack.append(20)
stack.append(30)
print(stack)  


top = stack[-1]
print(top)  

# Pop
popped = stack.pop()
print(popped)  
print(stack)   

# Check empty
print(len(stack) == 0)  

