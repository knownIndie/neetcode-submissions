class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r,f,b=[0]*len(nums),[0]*len(nums),[0]*len(nums)


        for idx,i in enumerate(nums):
            if idx ==0:
                f[idx]=1
            else:
                f[idx]=f[idx-1]*nums[idx-1]
        
        for w in range(len(nums)-1,-1,-1):
            if w ==len(nums)-1:
                b[w]=1
            else:
                b[w]=b[w+1]*nums[w+1]

        for k in range(len(r)):
            r[k]=f[k]*b[k]
        return r