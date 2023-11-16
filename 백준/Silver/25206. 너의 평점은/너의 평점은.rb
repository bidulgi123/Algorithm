n = 20
grade_dict = {'A+'=>4.5,
              'A0'=>4.0,
              'B+'=>3.5,
              'B0'=>3.0,
              'C+'=>2.5,
              'C0'=>2.0,
              'D+'=>1.5,
              'D0'=>1.0,
              'F'=>0}
total = 0
score = 0
n.times do
  subject, hak, grade = gets.chomp.split.map(&:to_s)
  hak = hak.to_f
  if grade != 'P'
    total += hak
    score += hak * grade_dict[grade]
  end
end
puts "#{(score / total)}"