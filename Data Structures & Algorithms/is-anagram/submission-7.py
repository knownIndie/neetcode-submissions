class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for val in s:
            seen[val] = seen.get(val, 0) + 1
        for val in t:
            if val not in seen:
                return False
            else:
                seen[val]-=1
            
            if seen[val] < 0:
                return False

        for count in seen.values():
            if count == 0:
                return True

        return False