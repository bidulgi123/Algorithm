a = gets.chomp.to_i
arr = []
for i in 0..a-1 do
    arr << gets.chomp.to_s
end
for n in arr
    if n.include?('S')
        puts n
    end
end