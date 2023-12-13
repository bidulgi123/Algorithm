a=int(input())
total=[380,425,450,495,570,590,620,780]
color=["cute","Violet","Indigo","Blue","Green","Yellow","Orange","Red"]
if a==780:
    print('Red')
else :
    for i in range(1,len(total)):
        if a >= total[i-1] and a < total[i]:
            print(color[i])