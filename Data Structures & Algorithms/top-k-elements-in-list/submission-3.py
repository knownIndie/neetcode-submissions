from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)

        for i in nums:
            seen[i] += 1
            
        return sorted(seen, key=seen.get, reverse=True)[:k]