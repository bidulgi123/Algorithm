a = gets.chomp.to_i
cnt = 0
for i in 1..a do 
    print "#{i} "
    cnt += 1
    if (cnt != 0 && cnt % 6 == 0) || i == a 
        print "Go! "
    end
end
