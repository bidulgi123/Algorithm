from string import ascii_uppercase

alphabet_dict = {}
total=[]
for i in ascii_uppercase:
    alphabet_dict[i] = 0
for j in range(int(input())):
    a=input()
    total.append(a)
    q=0
    a=reversed(a)
    for t in a:
        alphabet_dict[t] += 10**q
        q+=1
ans = sorted(alphabet_dict.items(), key=lambda x:x[1], reverse=True)
total_ans=[]
for i in range(len(ans)):
    if ans[i][1] == 0:
        break
    total_ans.append(ans[i][0])
dictionary = {string : 9-i for i,string in enumerate(total_ans)}
ans_list=[]
for p in range(len(total)):
    li=''
    for u in total[p]:
        li+=str(dictionary[u])
    ans_list.append(int(li))
print(sum(ans_list))