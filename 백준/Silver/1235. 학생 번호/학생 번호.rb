require 'set'
a=gets.chomp.to_i
arr=[]
for i in 0..a-1 do 
    arr << gets.chomp.to_s
end
for i in 1..arr[0].length() do
    t=Set.new
    for j in 0..a-1 do
        t << arr[j][-(i)..-1]
    end
    break if t.length == a
end
puts i