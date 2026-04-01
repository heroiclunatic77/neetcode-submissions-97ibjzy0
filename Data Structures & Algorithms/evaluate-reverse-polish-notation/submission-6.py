class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            stack =[]
            for token in tokens:
                if token == "-":
                    res = int(stack[-2]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == "+":
                    res = int(stack[-2]) + int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == "*":
                    res = int(stack[-2]) * int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif token == "/":
                    res = int(stack[-2]) / int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(token)
            return int(stack[0])

            
             