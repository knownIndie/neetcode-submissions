from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group=defaultdict(int)
        for val in nums:
            group[val]+=1

        frequentVal=sorted(group ,key=group.get, reverse=True)[:k]
        return frequentVal