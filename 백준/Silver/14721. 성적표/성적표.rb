a = gets.chomp.to_i
arr =[]
for i in 0..a-1 do
    arr << gets.chomp.split.map(&:to_i)
end
q=9999999999999
x=0
y=0
for i in 1..100 do 
    for j in 1..100 do 
        s=0
        for t in 0..a-1 do 
            s += ((arr[t][0]*i + j)-arr[t][1])**2
        end
        if s < q 
            q=s
            x=i
            y=j
        end
    end
end
print x,' ',y