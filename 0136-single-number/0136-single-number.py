class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        nums = sorted(nums)

        if len(nums) ==1:
            return nums[0]

        stack=[]

        for i in nums:

            if not stack:
                stack.append(i)

            elif stack[-1] == i:
                stack.pop()

            else:
                stack.append(i)

        return stack[0] 

       




        
        