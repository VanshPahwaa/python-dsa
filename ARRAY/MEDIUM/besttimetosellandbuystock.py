# import sys
# class Solution:
#     def maxProfit(self, prices) -> int:
#         maximum=-sys.maxsize-1
#         for i in range(0,len(prices)-1):
#             for j in range(i+1,len(prices)):
#                 temp=prices[i]-prices[j]
#                 maximum=max(maximum,temp)
#         if(maximum<0):
#             return 0
#         return maximum
# obj=Solution()
# print(obj.maxProfit([7,1,5,3,6,4]))

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice=-1
        sellPrice=-1
        maxProfit=0
        for i in range(0,len(prices)):
            if(buyPrice<0):
                buyPrice=prices[i]
            else:    
                if(prices[i]<buyPrice):
                    profit=sellPrice-buyPrice
                    if(profit>maxProfit):
                        maxProfit=profit
                    buyPrice=prices[i]
                    sellPrice=-1
                else:
                    if(prices[i]>sellPrice):
                        sellPrice=prices[i]
                        profit=sellPrice-buyPrice
                        if(profit>maxProfit):
                            maxProfit=profit

                        
        return maxProfit


        