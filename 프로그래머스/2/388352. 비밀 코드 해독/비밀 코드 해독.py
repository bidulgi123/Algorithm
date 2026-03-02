from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    num_list = [_ for _ in range(1, n+1)]
    q = [set(i) for i in q]

    for comb in combinations(num_list, 5):
        comb = set(comb)
        middle = 1
        
        for idx in range(len(q)) :
            if len(q[idx] & comb) != ans[idx]:
                middle = 0
                
        answer += middle
            
    return answer