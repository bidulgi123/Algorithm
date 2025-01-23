import sys
input = sys.stdin.readline
while True :
    try :
        a = int(input()) * 10000000
        b = int(input())
        total = [int(input()) for _ in range(b)]
        total.sort()
        start = 0
        end = b - 1
        flag = 0 
        if len(total) > 1 :
            while start < end :
                ans = total[start] + total[end]
                if ans > a :
                    end -= 1 
                elif ans < a :
                    start += 1    
                else :
                    print('yes',total[start], total[end])
                    flag = 1
                    break
        if flag == 0 :
            print('danger')
    except:
        sys.exit()