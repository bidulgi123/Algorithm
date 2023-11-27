a = gets.chomp.to_i
b = gets.chomp.split.map(&:to_i)
puts [a,(b[0]/2+b[1])].min