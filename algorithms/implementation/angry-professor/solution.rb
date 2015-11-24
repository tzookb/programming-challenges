
def isCanceledOrNot(totalStudents, minStudents, arrivalTimes)
	studentsArrivedOnTime = 0

	arrivalTimes.each do |x|
		studentsArrivedOnTime += 1 if x <= 0
	end

	puts studentsArrivedOnTime >= minStudents ? "NO" : "YES"
end

numOfTests = gets().strip.to_i


1.upto(numOfTests) do |i| 
	totalStudents, minStudents = gets().strip.split(" ").map(&:to_i)

	arrivalTimes = gets().strip.split(" ").map(&:to_i)

	isCanceledOrNot(totalStudents, minStudents, arrivalTimes)
end