a = gets.chomp.to_i
arr = []
for i in 0..2 do
  arr << gets.chomp.to_i
end
fruit = ["Watermelon", "Pomegranates", "Nuts"]
cnt = arr.find_index { |x| x <= a }
puts cnt ? fruit[cnt] : "Nothing"