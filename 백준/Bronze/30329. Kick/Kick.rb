a = gets.chomp
cnt = 0
i = 0
while i < a.length
    if a[i..i+3] == 'kick'
      cnt += 1
    end
    i += 1
end
puts cnt 