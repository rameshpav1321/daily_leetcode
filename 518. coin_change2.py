class Solution:
    def dp(self,i,amount,memo,coins):
        if amount==0:
            return 1
        if i==len(coins):
            return 0
        if (i,amount) not in memo:
            if coins[i]>amount:
                memo[(i,amount)]=self.dp(i+1,amount,memo,coins)
            else:
                memo[(i,amount)]=self.dp(i,amount-coins[i],memo,coins)+self.dp(i+1,amount,memo,coins)
        return memo[(i,amount)]
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        return self.dp(0,amount,memo,coins)