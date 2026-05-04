from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)

        values=[]
        for i in nums:
            seen[i]+=1
        
        for idx , val in sorted(seen.items(), key=lambda items:items[1], reverse=True):
            values.append(idx)
            if len(values)== k:
                
                
                break
        
        return values