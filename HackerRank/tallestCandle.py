# You are in charge of the cake for your nieces birthday and
# have decided the cake will have one candle for each year of her total age.
# When she blows out the candles, she’ll only be able to blow out the tallest ones.
# Your task is to find out how many candles she can successfully blow out.
# For example, if your niece is turning  years old, and the cake will have  candles of height
# 4, 1, 4, 3, she will be able to blow out 2 candles successfully, since the tallest candles are
# of height  and there are  such candles.

def birthdayCakeCandles(ar):
    tallestCandles = max(ar)
    return ar.count(tallestCandles)
