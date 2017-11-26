#!/usr/bin/env python
# @Author  : pengyun


class MinStack:
    """
    带最小值的栈。思路 使用一个数组来保存最小的数。
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, data):
        self.stack.append(data)
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.stack.pop()
            return self.min_stack.pop()
        return self.stack.pop()

    def min(self):
        return self.min_stack[-1]

def valid_parentheses(s):
    """有效的括号序列"""
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack) == 0:
            return False
        else:
            stack.pop()
    return True

def eval_rpn(lst):
    """逆波兰求值"""
    stack = []
    for i in lst:
        if i == '+':
            a1, a2 = stack.pop(), stack.pop()
            stack.append(a1+a2)
        elif i == '-':
            a1, a2 = stack.pop(), stack.pop()
            stack.append(a2 - a1)
        elif i == '*':
            a1, a2 = stack.pop(), stack.pop()
            stack.append(a2 * a1)
        elif i == '/':
            a1, a2 = stack.pop(), stack.pop()
            stack.append(int(a2 / a1))
        else:
            stack.append(int(i))
    return stack[-1]

if __name__ == '__main__':
    # print(valid_parentheses('(()()((()))'))
    print(eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))