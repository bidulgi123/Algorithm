a = gets.chomp.to_i
ans = gets.chomp.split.map(&:to_i)
ans = ans.each_with_index.map { |element, index| [index, element] }
total=[]
while ans.any?
    t=ans.shift
    total << (t[0] + 1)
    if t[1] > 0
        ans=ans.rotate((t[1]-1))
    end
    if t[1] < 0
        ans=ans.rotate((t[1]))
    end
end
print total.join(' ')
