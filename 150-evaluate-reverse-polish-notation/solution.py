class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x in "+-*/":
                # Pop the top two elements for operation
                b, a = stack.pop(), stack.pop()
                if x == '+':
                    stack.append(a + b)
                elif x == '-':
                    stack.append(a - b)
                elif x == '*':
                    stack.append(a * b)
                elif x == '/':
                    # For division, ensure the result is truncated towards zero
                    stack.append(int(a / b))
            else:
                # x is a number, not an operator; convert to int and append
                stack.append(int(x))

        return stack[0]