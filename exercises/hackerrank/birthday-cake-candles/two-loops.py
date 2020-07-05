def birthdayCakeCandles(candles):
    highest_candle_val = max(candles)

    highest_candles_count = 0
    for cur_candle_height in candles:
        if cur_candle_height == highest_candle_val:
            highest_candles_count += 1

    return highest_candles_count

candles = [2, 3, 1, 3]
res = birthdayCakeCandles(candles)
print(res)
