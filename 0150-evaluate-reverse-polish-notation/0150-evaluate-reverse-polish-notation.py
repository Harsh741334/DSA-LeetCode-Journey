class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        sign = ["+","-","*","/"]

        stack = []

        for i in tokens:
            if not stack:
                stack.append(int(i))
            else:

                if  i in sign:
                    r = stack.pop()
                    l = stack.pop()
                    if i == "+":
                        stack.append(l+r)
                    elif i == "-":
                        stack.append(l-r)
                    elif i == "*":
                        stack.append(l * r)
                    else:
                        ans = int(l/r)
                        stack.append(ans)
                        # if ans <= 0:
                        #  stack.append(0)
                        # else:
                        #     stack.append(ans)


                else:
                    stack.append(int(i))

        return stack.pop()
        