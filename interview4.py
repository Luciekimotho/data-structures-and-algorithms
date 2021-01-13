# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")

#maxProfit=0  O(1)
#loop through arr(i) 
  #loop (j) j=i+1
     #profit = arr[j] - arr[i]
     #maxProfit = max(maxProfit, profit)  O(n^2)


#leastprice     12,11,11,9,9,8,8,8,8   Time = 0(n) 0(1)
#profitForToday 0,-1,2,0,3,0,6,5,7 = min O(1)

# [12, 11, 13, 9, 12, 8, 14, 13, 15] 
# 

#frontProfit 
#backPointer 
#loop arr[i] = sellday   buy = a[i-1]  profit=                [            ]

def stock(arr):
    leastprice = arr[0]
    profitToday = 0
    maxProfit = 0

    for price in arr:
        if price < leastprice:
            leastprice = price

        profitToday = price - leastprice
        maxProfit = max(maxProfit, profitToday)
    return maxProfit

arr = [12, 11, 13, 9, 12, 8, 14, 13, 15]
print(stock(arr))