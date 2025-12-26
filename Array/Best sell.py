class solution():
    def bestsell(self,prices):
        ans=0
        min_value=prices[0]

        for i in range(1,len(prices)):
            profit = prices[i]-min_value
            if profit > ans :
                ans= profit
            if prices[i] < min_value:
                min_value=prices[i]
        return ans
obj=solution()
print(obj.bestsell([7,1,5,3,6,4]))
