class Solution:
    def maxProduct(self, lst: List[int]) -> int:
        first_largest = 0
        second_largest = 1
        for i in range(1, len(lst)):
            if lst[i] > lst[first_largest]:
                second_largest = first_largest
                first_largest = i
            elif lst[second_largest] < lst[i] <= lst[first_largest]:
                second_largest = i
        return (lst[first_largest]-1)*(lst[second_largest]-1)