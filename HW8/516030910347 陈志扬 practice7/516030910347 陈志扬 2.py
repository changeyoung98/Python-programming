# File: list.py
# By:Daisy
def count_in_list(A,x):
    n=0
    for i in A:
        if i==x:
            n=n+1
        else:
            try:    
                for j in i:
                    if j==x:
                        n=n+1
            except:
                TypeError
                    
    print n
def main():
    A=[1,2,3,[1,2],1,[1,2,1]]
    x=1
    count_in_list(A,x)
main()
