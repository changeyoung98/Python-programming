# File:puddle.py
def main():
    n=input("Enter the number of the puddles. ")
    s=input("Enter the height of each puddle in the form of a list.")
    a=max(s)
    i=s.index(a)
    w1=0
    while i>1:
        b=max(s[:i])
        j=s.index(b)
        w1=w1+(i-j-1)*b
        if j+2<=i:
            for x in s[j+1:i]:
                w1=w1-x
            i=j
        else:
            i=j
    s.reverse()
    l=s.index(a)
    w2=0
    while l>1:
        c=max(s[:l])
        k=s.index(c)
        w2=w2+(l-k-1)*c
        if k+2<=l:
            for y in s[k+1:l]:
                w2=w2-y
            l=k
        else:
            l=k
    w=w1+w2
    print w

main()
