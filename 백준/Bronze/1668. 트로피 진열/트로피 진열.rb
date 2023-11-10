a = gets.chomp.to_i
arr = []
for i in 0..a-1 do
  q = gets.chomp.to_i 
  arr << q 
end
left_cnt = right_cnt = 0
left_max = right_max = 0
arr.each do |n|
  if n > left_max
    left_max = n
    left_cnt += 1
  end
end
arr.reverse_each do |n|
  if n > right_max
    right_max = n
    right_cnt += 1
  end
end
puts left_cnt
puts right_cnt