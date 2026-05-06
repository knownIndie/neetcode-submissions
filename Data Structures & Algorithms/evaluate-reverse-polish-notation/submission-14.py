class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=0
        o={ "+":"ad", "-":"sub", "*":"mul", "/":"div"}
        s=[]
        for i in range(len(tokens)):
            if tokens[i] not in o:
                s.append(int(tokens[i]))
                print('t',s)
            else:
                a=s.pop()
                print('a',a)
                b=s.pop()
                print('b',b)
                if o[tokens[i]]=="ad":
                    s.append(a+b)
                    print('ad',a+b)
                elif o[tokens[i]]=="mul":
                    s.append(a*b)
                    print('m',a*b)
                elif o[tokens[i]]=="sub":
                    s.append(b-a)
                    print('s',a-b)
                else:
                    s.append(int(b/a))
                    print('d',int(b/a))
                print('b',s)
        return s.pop()