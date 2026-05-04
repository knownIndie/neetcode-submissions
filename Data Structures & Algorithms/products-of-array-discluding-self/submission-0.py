class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val=[]
        a=1
        zeroidx=[]

        for idx,i in enumerate(nums):
            if i == 0:
                a=a*1
                zeroidx.append(idx)
            else:
                a=a*i
        print(a)
        for idx,i in enumerate(nums):
            if len(zeroidx)==1:
                if idx in zeroidx:
                    val.append(a)
                else:
                    val.append(0)
            elif len(zeroidx)==0:
                val.append(a//i)
            else:
                return [0]*len(nums)


        return val

    