class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        curr_gas=0          
        deficit_gas=0        
        for i in range(len(gas)):
            curr_gas+=gas[i]-cost[i]
            if curr_gas<0:            
                start=i+1        
                deficit_gas+=curr_gas
                curr_gas=0         
        return start if (curr_gas+deficit_gas)>=0 else -1