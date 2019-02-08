def combine(a,b,idxA):
    if idxA == len(a) :
        if len(b) > 2 :
            print(b)
            return
    else:
        c = b[:]
        b.append(a[idxA])
        idxA += 1
        combine(a,b,idxA)
        combine(a,c,idxA)

def main():
    a = ['a','b','c']
    b = []
    combine(a,b,0)
main()
