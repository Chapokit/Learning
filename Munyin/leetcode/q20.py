
def isValid(s):
    stack = []
    for bracket in s:
        if bracket == "(" or bracket == "[" or bracket == "{":
            stack.append(bracket)
        elif bracket == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
        elif bracket == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()
        elif bracket == "}":
            if not stack or stack[-1] != "{":
                return False
        
            stack.pop()
    return len(stack) == 0



        
s = "(]"
print(isValid(s))