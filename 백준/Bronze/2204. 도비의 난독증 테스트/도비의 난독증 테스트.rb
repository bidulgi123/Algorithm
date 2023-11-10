a = 999
while a != 0
  a = gets.chomp.to_i
  if a != 0
    arr = []
    for i in 0..a-1 do
      q = gets.chomp.to_s 
      t = q.downcase
      arr << [t, q]  
    end
    arr = arr.sort
    puts arr[0][1]
  end
end