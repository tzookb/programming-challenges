def birthdayCakeCandles(candles):
    candles_heights = [0, 0, 0, 0, 0]
    for cur_candle_height in candles:
        candles_heights[cur_candle_height] += 1

    print(candles_heights)
    

	# maxVal = 0
	# for key in mappings:
	# 	if mappings[key] > maxVal:
	# 		maxVal = mappings[key]

	# return maxVal


candles = [2, 1, 0,2]
res = birthdayCakeCandles(candles)
print(res)

1, 2, 3, 4, 5