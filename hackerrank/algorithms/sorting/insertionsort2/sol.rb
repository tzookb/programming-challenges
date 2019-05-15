def sort(arr)
	size = arr.size
	
	indexMain = 0
	while indexMain < size

		indexInside = 0

		while indexInside < size 
			if indexMain != indexInside
				if arr[indexMain] < arr[indexInside]
					arr.delete_at(indexMain)
					arr.insert(indexInside, arr[indexMain])
				end	
			end
			
			indexInside += 1
		end
		
		print arr, "\n"

		indexMain += 1
	end
end

sort([1,4,3,5,6,2])