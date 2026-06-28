class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr  = sorted(arr)

        if arr[0] != 1:
            arr[0]  = 1

        for i in range(1,len(arr)):
            if not abs(arr[i-1] - arr[i]) <=1:
                arr[i] = arr[i-1] + 1

        return max(arr)
            


        