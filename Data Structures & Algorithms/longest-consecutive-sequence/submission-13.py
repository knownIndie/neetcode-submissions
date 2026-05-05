class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        long=0
        if not n:
            return 0
        for i in n:
            if i-1 not in n:
                length = 1
                # long=max(long,length)
                while (i+length) in n:
                    length+=1
                long = max(long,length)

        return long