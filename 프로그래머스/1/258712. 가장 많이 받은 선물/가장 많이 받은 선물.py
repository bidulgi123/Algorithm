def solution(friends, gifts):
    answer = 0
    table = {x: {y: 0 for y in friends if y != x} for x in friends}
    gift_power = {i : 0 for i in friends}
    
    for detail in gifts : 
        send, get = detail.split(" ")
        table[send][get] += 1
        gift_power[send] +=1
        gift_power[get] -=1 
    
    
    for name in friends :
        middle = 0
        for bigyo in table[name].keys():
            
            if table[name][bigyo] > table[bigyo][name]:
                middle +=1
            elif table[name][bigyo] == table[bigyo][name]:
                if gift_power[name] > gift_power[bigyo] :
                    middle +=1
                else :
                    continue
            else :
                continue
                
        if middle > answer :
            answer = middle
            
    return answer