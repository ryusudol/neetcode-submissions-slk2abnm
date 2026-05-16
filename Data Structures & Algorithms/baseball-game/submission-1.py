class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for idx, op in enumerate(operations):
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operations[idx]))
        return sum(stack)