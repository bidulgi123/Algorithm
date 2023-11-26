a = gets.chomp.split.map(&:to_i)
b = gets.chomp.split.map(&:to_i)
ans=a[1]*b[0]+a[1]*b[1]
for i in 1...(b.length()) do
    t=a[1]*b[i]+b[i-1]*a[1]
    if ans > t
        ans = t
    end
end
puts ans