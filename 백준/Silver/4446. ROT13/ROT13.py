while True:
    try:
        a=input()
        t=['a', 'i', 'y', 'e', 'o', 'u']
        t_set={'a', 'i', 'y', 'e', 'o', 'u'}
        b=['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
        b_set={'b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f'}
        st=''
        flag=0
        for i in a :
            if i.isupper()==True:
                flag=1
            if i.lower() in t_set :
                if flag==1:
                    idx=t.index(i.lower())+3
                    idx%=6
                    st+=t[idx].upper()
                else :
                    idx=t.index(i)+3
                    idx%=6
                    st+=t[idx]
            elif i.lower() in b_set :
                if flag==1:
                    idx=b.index(i.lower())+10
                    idx%=len(b)
                    st+=b[idx].upper()
                else :
                    idx=b.index(i)+10
                    idx%=len(b)
                    st+=b[idx]
            else :
                st+=i
            flag=0
        print(st)
    except:
        break