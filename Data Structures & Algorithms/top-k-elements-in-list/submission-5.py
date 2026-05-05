class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b=[[] for _ in range(len(nums)+1)]
        d={}
        res=[]


        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for key , value in d.items():
            b[value].append(key)

        for i in range(len(b)-1,0,-1):
            for a in b[i]:
                res.append(a)
            if len(res)==k:
                return res