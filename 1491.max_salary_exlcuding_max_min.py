class Solution:
    def average(self, salary: List[int]) -> float:
        max_sal = min_sal = salary[0]
        total_sum = 0
        for i in range(len(salary)):
            total_sum += salary[i]
            if salary[i] > max_sal:
                max_sal = salary[i]
            if salary[i] < min_sal:
                min_sal = salary[i]
        return (total_sum - max_sal - min_sal) / (len(salary) - 2)
