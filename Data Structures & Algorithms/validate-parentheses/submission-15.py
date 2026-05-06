class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {
        "]": "[",
        ")": "(",
        "}": "{"}

       
        for i in s:
            if i in d and st:
                t=st[-1]
                print('i',i,'t', t, 'st' ,st)
                print("d[i]",d[i] ,"t", t)
                if d[i] == t:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
                print('if-','i',i, 'st' ,st ,"\n")

        if not st:
            return True
        else:
            return False
                
            