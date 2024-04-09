n = int(input())
def hanoi_top(n,start,end):
    if n == 1:
        print(start,end) 
        return
    hanoi_top(n-1,start,6-start-end) 
    print(start,end) 
    hanoi_top(n-1,6-start-end,end) 
print(2**n-1)
hanoi_top(n,1,3)