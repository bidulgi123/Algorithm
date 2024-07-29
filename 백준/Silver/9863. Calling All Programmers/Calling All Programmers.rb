while true
  a, b, c = gets.split.map(&:to_i)
  break if a == 0 && b == 0 && c == 0
  ans = 0
  t = (1..a).to_a
  c.times do
    b.times do
      t.push(t.shift)
    end
    ans = t.pop
  end
  puts ans
end