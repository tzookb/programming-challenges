class NumberToString

	@@plainNumbers = {
		'1'=>'one', '2'=>'two', '3'=>'three', '4'=>'four', '5'=>'five', '6'=>'six', '7'=>'seven', '8'=>'eight',
		'9'=>'nine', '10'=>'ten', '11'=>'eleven', '12'=>'twelve', '13'=>'thirteen', '15'=>'fifteen'
	}

	@@groupPlainNumbers = {
		'10'=>'teen',
		'20'=>'twenty'
	}

	def getStringOfNumber(number)
		resStr = ''

		if @@plainNumbers[number.to_s]
			return @@plainNumbers[number.to_s]
		end

		if number >= 20
			resStr += @@groupPlainNumbers['20']+" "
		end


	end

end

class TimeInToWords

	@@plainNumbers = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

	@@specialMinuteNumbers = {
		'1' => 'one minute past {HOUR}',
		'2-10' => '{MINUTE} minutes past {HOUR}',
		'30' => 'half past {HOUR}',
		'45' => 'quarter to {HOUR+1}'
	}
	

	def initialize()
		
	end


	def getTimeInStr(time)
		hour, minutes = self.getHourAndMinutes(time)

		#puts "here"
		if self.isSpecialMinute(minutes)
			finalString = self.getSpecialMinuteString(minutes)
			#puts "there"
			#puts finalString
			return self.insertValsToTimeString(@@plainNumbers[hour], minutes, finalString)
		end

		if minutes < 30

		else

		end


		return @@plainNumbers[hour]+' o`clock'
	end


	def insertValsToTimeString(hour, minutes, timeStr)
		timeStr.sub '{HOUR}', hour.to_s
	end


	def isSpecialMinute(minutes)
		@@specialMinuteNumbers.has_key?(minutes.to_s)
	end

	def getSpecialMinuteString(minutes)
		@@specialMinuteNumbers[minutes.to_s]
	end

	protected
	def getHourAndMinutes(time)
		time.split(':').map(&:to_i)
	end

	def getPlain()
		print @@specialMinuteNumbers
	end

end

if false
	ob = TimeInToWords.new
	puts ob.getTimeInStr('3:30')
end