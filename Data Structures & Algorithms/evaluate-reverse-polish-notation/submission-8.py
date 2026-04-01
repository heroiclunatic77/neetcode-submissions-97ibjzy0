class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token =="+":
                s = int(stack[-2]) + int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(s)
            elif token =="-":
                s = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(s)
            elif token =="/":
                s = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(s)
            elif token =="*":
                s = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(s)
            else:
                stack.append(token)
        return int(stack[0])

            