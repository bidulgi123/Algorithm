a = gets.chomp.to_i
ans=[1,1]
for i in 1..a-1 do
    ans << (ans[i]+ans[i-1])%10
end
puts ans[i+1]