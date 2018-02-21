# This function computes all permutations
def permute (a, lo):
  hi = len(a)
  if (lo == hi):
    if (is_right_bench(a)):
        print(a)
  else:
    for i in range (lo, hi):
      a[lo], a[i] = a[i], a[lo]
      permute (a, lo + 1)
      a[lo], a[i] = a[i], a[lo]
def is_right_bench(a):
    for i in range(1,len(a)-1):
        if (a[i]=='A'):
            if (a[i-1]!='B' and a[i+1]!='B'):
                return False
        elif (a[i]=='B'):
            if (a[i-1]!='A' and a[i+1]!='A'):
                return False
        elif (a[i]=='C'):
            if (a[i-1]=='D' or a[i+1]=='D'):
                return False
        elif (a[i]=='D'):
            if (a[i-1]=='C' or a[i+1]=='C'):
                return False
    if ((a[0]=='A' and a[1]!='B') or (a[0]=='B' and a[1]!='A')):
        return False
    return True
def main():
    letters = ['A','B','C','D','E']
    permute(letters,0)
main()
