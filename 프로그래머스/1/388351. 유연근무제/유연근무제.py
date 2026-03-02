

def solution(schedules, timelogs, startday):
    
    def time(t):
        h = t // 100
        m = t % 100

        m += 10
        if m >= 60:
            h += 1
            m -= 60

        return h * 100 + m

    start = 0 
    end = 0
    answer = 0
    
    if startday < 7 :
        start = 6 - startday 
        end = start + 1
        
    else :
        start = 0
        end = 6
    
    for i in range(len(schedules)):
        want_time = schedules[i]
        
        chk = 1
        
        for j in range(7):
            if time(want_time) < timelogs[i][j] and j != start and j != end:
                chk = 0 
                break
                
        answer += chk
        
    return answer