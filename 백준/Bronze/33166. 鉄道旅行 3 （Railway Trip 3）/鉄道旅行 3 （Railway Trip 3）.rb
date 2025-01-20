a, b = gets.split.map(&:to_i)
c, d = gets.split.map(&:to_i)
if b > a 
puts a*c + (b-a)*d
else 
puts c*b
end
