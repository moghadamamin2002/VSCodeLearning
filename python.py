
# Stack Creation
def create_stack():
    stack = list()            #declaring an empty list
    return stack


# Checking for empty stack
def Isempty(stack):
    return len(stack) == 0


# Inserting items into the stack
def push(stack, n):
    stack.append(n)
    print("pushed item: " + n)


# Removal of an element from the stack
def pop(stack):
    if (Isempty(stack)):
        return "stack is empty"
    else:
        return stack.pop()

# Displaying the stack elements
def show(stack):
    print("The stack elements are:")
    for i in stack:
        print(i)
        
stack = create_stack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))
print("popped item: " + pop(stack))
show(stack)