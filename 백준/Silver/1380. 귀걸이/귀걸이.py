import sys
input=sys.stdin.readline
scenario=0
while True:
    scenario+=1
    a=int(input().rstrip())
    if a == 0 :
        break
    else : 
        Attendance={}
        pack=set()
        for i in range(1,a+1):
            student=input().rstrip()
            Attendance[i]=student
        for j in range(2*a-1):
            num, alpha = map(str,input().split())
            num=int(num)
            if num not in pack :
                pack.add(num)
            else :
                del Attendance[num]
        print(scenario, *Attendance.values())