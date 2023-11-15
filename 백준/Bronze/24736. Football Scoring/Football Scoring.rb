a = gets.chomp.split.map(&:to_i)
b = gets.chomp.split.map(&:to_i)
puts '%d %d' % [a[0]*6+a[1]*3+a[2]*2+a[3]+a[4]*2, b[0]*6+b[1]*3+b[2]*2+b[3]+b[4]*2]