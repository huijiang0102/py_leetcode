class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        stack = list()
        operator = "+"
        num = 0

        for i, e in enumerate(s):
            if e.isdigit():
                num *= 10
                num += ord(e) - ord("0")
            if (not e.isdigit() and not e.isspace()) or i == len(s) - 1:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack.append(stack.pop() * num)
                elif operator == "/":
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)

                operator = e
                num = 0
        return sum(stack)
