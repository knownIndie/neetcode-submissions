class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idx, l in enumerate(numbers):
            r = len(numbers) - 1
            while idx < r:
                sum = l + numbers[r]
                if sum == target:
                    return [idx+1, r+1]
                elif sum>target:
                    r-=1
                else:
                    
                    break