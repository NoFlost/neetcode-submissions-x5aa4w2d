class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val not in ['+','-','*','/']:
                stack.append(int(val))
            else:
                y = stack.pop()
                x = stack.pop()
                res = self.calculate(x, y, val)
                stack.append(res)
        
        return stack.pop()

    def calculate(self, x: int, y: int, operator: str) -> int:
        if operator == '+':
            return x + y

        if operator == '-':
            return x - y

        if operator == '*':
            return x * y

        if operator == '/':
            return int(x / y)
        
        return None

