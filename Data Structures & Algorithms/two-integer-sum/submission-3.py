from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for i , val in enumerate(nums):
            second = target - val
            
            if second in dic:
                return([dic[second],i])
            
            dic[val]=i
            