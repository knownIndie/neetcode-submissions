class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}

        for idx,val in enumerate(nums):
            diff=target-val
            print(diff)
            print(seen)
            if diff in seen:
                # print(idx,seen[val])
                return [seen[diff] ,idx]
            else:
                seen[val]=idx
        return [0,0]