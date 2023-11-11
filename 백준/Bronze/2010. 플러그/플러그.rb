a = gets.chomp.to_i
ans=0
for i in 0..a-1 do
    ans += gets.chomp.to_i
end
print(ans-(a-1))