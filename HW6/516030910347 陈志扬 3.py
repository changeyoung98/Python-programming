# Flie: duplicate.py
# A program to delete the repeated elements.
# By: Daisy
def cancel(a):
    for i in range(len(a)):
        x=a[:i+1]
        y=a[i+1:]
        for e in a[i+1:]:
            if e==a[i]:
                y.remove(e)
        a=x+y
    return a
def _cancel(a):
    for h in range(len(a)):
        try:
            a[h]=cancel(a[h])
        except TypeError:
            a[h]
    return a
def _delete(a):
    _cancel(a)
    for i in range(len(a)):
        x=a[:i+1]
        y=a[i+1:]
        for e in a[i+1:]:
            if e==a[i]:
                y.remove(e)
            else:
                try:
                    for k in a[i]:
                        if k==e:
                            y.remove(e)
                        else:
                            try:
                                for j in e:
                                    if j==k:
                                        e.remove(j)
                            except TypeError:
                                y
                except TypeError:
                    try:
                        for j in e:
                            if j==a[i]:
                                e.remove(j)
                    except TypeError:
                        y
        try:
            x[-1]=_delete(x[-1])
        except TypeError:
            x
        a=x+y
    return a
def de_duplicate(a):
    if len(a)==1:
        try:
            a=_delete(a[0]) 
        except TypeError:
            a=a
        return a
    else:
        return _delete(a)
def main():
    a=input("Enter the list to be deduplicated. ")
    print de_duplicate(a)

main()
