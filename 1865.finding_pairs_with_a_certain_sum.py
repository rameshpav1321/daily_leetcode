from collections import Counter


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.nums1_dict = Counter(nums1)
        self.nums2_dict = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = self.nums2[index] + val
        self.nums2[index] = new_val
        self.nums2_dict[old_val] -= 1
        self.nums2_dict[new_val] += 1

    def count(self, tot: int) -> int:
        total_count = 0
        for num, count in self.nums1_dict.items():
            if tot - num in self.nums2_dict:
                total_count += count * self.nums2_dict[tot - num]
        return total_count
