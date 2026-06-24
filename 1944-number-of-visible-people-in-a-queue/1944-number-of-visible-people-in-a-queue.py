class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = []
        stack = []

        for i in reversed(heights):
            cnt = 0

            while stack and stack[-1] < i:
                cnt +=1
                stack.pop()

            if stack :
                cnt +=1

            ans.append(cnt)
            stack.append(i)

        rev  = []

        for i in reversed(ans):
            rev.append(i)

        

        return rev
        