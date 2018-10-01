h=0
N=5
L=25
s=[2,11,14,17,21]
for k in range (N-h):
    S=s
    del S[k]
    print s
    t=[S[0]]
    for j in range(1,N-h-1):
        t.append(S[j]-S[j-1])
    m=L-S[N-h-2]
    t.append(m)
print t
