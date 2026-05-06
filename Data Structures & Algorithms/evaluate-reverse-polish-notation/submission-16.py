class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in range(len(tokens)):
            if tokens[i] not in ('+', '-', '*', '/'):
                s.append(int(tokens[i]))
                print('t',s)
            else:
                a=s.pop()
                print('a',a)
                b=s.pop()
                print('b',b)
                if tokens[i]=="+":
                    s.append(a+b)
                    print('ad',a+b)
                elif tokens[i]=="*":
                    s.append(a*b)
                    print('m',a*b)
                elif tokens[i]=="-":
                    s.append(b-a)
                    print('s',a-b)
                else:
                    s.append(int(b/a))
                    print('d',int(b/a))
                print('b',s)
        return s.pop()