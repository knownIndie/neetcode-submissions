class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx , val in enumerate(numbers):
            r = len(numbers)-1
            while idx<r:
                sum = val + numbers[r]
                if sum>target:
                    r-=1
                elif sum<target :
                    idx+=1
                elif sum == target:
                    return[idx+1,r+1]
        return []
