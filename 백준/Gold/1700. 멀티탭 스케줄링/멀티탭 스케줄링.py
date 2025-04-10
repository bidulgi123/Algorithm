a, b = map(int, input().split())
total = list(map(int, input().split()))
tab = []
set_tab = set()
cnt = 0
for i in range(b):
    if total[i] in set_tab:
        continue

    if len(tab) < a:
        tab.append(total[i])
        set_tab.add(total[i])
        continue

    q = -float('inf')
    final_index = -float('inf')
    
    for idx, j in enumerate(tab):
        try:
            last_index = total[i+1:].index(j)
        except :
            final_index = idx
            break
        if last_index > q:
            q = last_index
            final_index = idx
    
    set_tab.remove(tab[final_index])
    set_tab.add(total[i])
    tab[final_index] = total[i]
    cnt += 1

print(cnt)
