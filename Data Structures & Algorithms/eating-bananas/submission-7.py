from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        start_speed = 1
        end_speed = max(piles)
        answer=0
        # for speed in range(start_speed, end_speed + 1):
        while start_speed<=end_speed:
            mid = start_speed +(end_speed-start_speed) // 2
            total_hours = 0
            for pile in piles:
                hours_needed = ceil(pile / mid)
                total_hours += hours_needed 
                # print("total_hours",total_hours,"mid",mid)
            if total_hours <= h:
                answer = mid
                end_speed=mid-1
            elif total_hours>h:
                start_speed=mid+1
        
        return answer