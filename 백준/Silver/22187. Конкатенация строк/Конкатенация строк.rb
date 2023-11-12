arr=gets.chomp.to_s
ans=''
mid=''
flag=0
for i in 0..arr.length()-1 do
    if flag == 0 
        ans << arr[i]
    end
    if flag == 1  
        mid << arr[i]
    end
    if arr[i] == '('
        ans.chop!
        flag=1
    end
    if arr[i] == ')'
        flag=0
        mid.chop!
        mid.reverse!
        ans << mid
        mid=''
    end 
end
puts ans