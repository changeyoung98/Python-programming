def main():
    L,N,M=input("Enter\n")
    s=[0]*(N+1)
    for i in range(N):
        s[i+1]=input("")
    s.append(L)
    for h in range(M):
        u=[]
        for k in range (1,N+1-h):
            t=[]
            for j in range(N-h):
                if j==k-1:
                    t.append(s[j+2]-s[j])
                elif j==k:
                    t=t
                else:
                    t.append(s[j+1]-s[j])
            u.append(min(t))
        a=max(u)
        b=u.index(a)
        del s[b+1]
    print a

main()
