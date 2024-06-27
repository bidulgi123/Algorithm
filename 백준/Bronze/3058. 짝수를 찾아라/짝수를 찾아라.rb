a = gets.to_i
a.times do
  t = gets.split.map(&:to_i)
  q = []
  t.each do |j|
    if j.even?
      q << j
    end
  end
  puts "#{q.sum} #{q.min}"
end