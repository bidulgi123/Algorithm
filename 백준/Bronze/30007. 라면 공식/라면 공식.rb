a=gets.chomp.to_i
for i in 0..a-1 do 
    b = gets.chomp.split.map(&:to_i)
    puts b[0]*(b[2]-1)+b[1]
end