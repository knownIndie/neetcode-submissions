class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        area=0
        

        while l<r:
            m=min(heights[l], heights[r])*(r-l)
            if heights[l]<heights[r]:
                area=max(area,m)
                l+=1

            else:
                area=max(area,m)
                r-=1
                
                
        return area