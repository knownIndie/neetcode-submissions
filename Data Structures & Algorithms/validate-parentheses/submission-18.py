class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {
        "]": "[",
        ")": "(",
        "}": "{"}

        for i in s:
            if i not in d:
                st.append(i)
            else:
                if not st:
                    return False
                t=st[-1]
                if d[i]==t:
                    st.pop()
                else:
                    return False
            
        if not st:
            return True
        else:
            return False 


