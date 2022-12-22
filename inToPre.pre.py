# step1 => Traverse the infix expression and check if given character is an operator or an operand.



# step2 => If it is an operand, then push it into operand stack.



# step3 => If it is an operator, then check if priority of current operator is greater than or less than or equal to the operator at top of the stack.
# If priority is greater, then push operator into operator stack. 
# Otherwise pop two operands from operand stack, pop operator from operator stack and push string operator + operand 2 + operand 1 into operand stack.
# Keep popping from both stacks and pushing result into operand stack until priority of current operator is less than or equal to operator at top of the operator stack.



# step4 => If current character is ‘(‘, then push it into operator stack.



# step5 => If current character is ‘)’, then check if top of operator stack is opening bracket or not.
# If not pop two operands from operand stack, pop operator from operator stack and push string operator + operand 2 + operand 1 into operand stack.
# Keep popping from both stacks and pushing result into operand stack until top of operator stack is an opening bracket.



# step6 =>The final prefix expression is present at top of operand stack.


# Python3 program to convert infix to prefix.
 
# Function to check if
# given character is
# an operator or not.
def isOperator(c):
    return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))
 
# Function to find priority
# of given operator.
def getPriority(C):
    if (C == '-' or C == '+'):
        return 1
    elif (C == '*' or C == '/'):
        return 2
    elif (C == '^'):
        return 3
    return 0
 
# Function that converts infix
# expression to prefix expression.
def infixToPrefix(infix):
    # stack for operators.
    operators = []
 
    # stack for operands.
    operands = []
 
    for i in range(len(infix)):
        # If current character is an
        # opening bracket, then
        # push into the operators stack.
        if (infix[i] == '('):
            operators.append(infix[i])
 
        # If current character is a
        # closing bracket, then pop from
        # both stacks and push result
        # in operands stack until
        # matching opening bracket is
        # not found.
        elif (infix[i] == ')'):
            while (len(operators)!=0 and operators[-1] != '('):
                # operand 1
                op1 = operands[-1]
                operands.pop()
 
                # operand 2
                op2 = operands[-1]
                operands.pop()
 
                # operator
                op = operators[-1]
                operators.pop()
 
                # Add operands and operator
                # in form operator +
                # operand1 + operand2.
                tmp = op + op2 + op1
                operands.append(tmp)
 
            # Pop opening bracket
            # from stack.
            operators.pop()
 
        # If current character is an
        # operand then push it into
        # operands stack.
        elif (not isOperator(infix[i])):
            operands.append(infix[i] + "")
 
        # If current character is an
        # operator, then push it into
        # operators stack after popping
        # high priority operators from
        # operators stack and pushing
        # result in operands stack.
        else:
            while (len(operators)!=0 and getPriority(infix[i]) <= getPriority(operators[-1])):
                op1 = operands[-1]
                operands.pop()
 
                op2 = operands[-1]
                operands.pop()
 
                op = operators[-1]
                operators.pop()
 
                tmp = op + op2 + op1
                operands.append(tmp)
            operators.append(infix[i])
 
    # Pop operators from operators
    # stack until it is empty and
    # operation in add result of
    # each pop operands stack.
    while (len(operators)!=0):
        op1 = operands[-1]
        operands.pop()
 
        op2 = operands[-1]
        operands.pop()
 
        op = operators[-1]
        operators.pop()
 
        tmp = op + op2 + op1
        operands.append(tmp)
 
    # Final prefix expression is
    # present in operands stack.
    return operands[-1]
 
s = "(A-B/C)*(A/K-L)"
print( infixToPrefix(s))