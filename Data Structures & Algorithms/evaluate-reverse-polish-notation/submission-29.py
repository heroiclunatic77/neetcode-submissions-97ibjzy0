class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token =="+":
                new = int(stack[-2])+int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new)
            elif token =="-":
                new = int(stack[-2])-int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new)
            elif token =="*":
                new = int(stack[-2])*int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new)
            elif token =="/":
                new = int(stack[-2])/int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new)
            else:
                stack.append(token)
        return int(stack[0])
            