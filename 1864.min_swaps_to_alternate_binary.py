class Solution:
    def minSwaps(self, s: str) -> int:
        count_1s = s.count("1")
        count_0s = s.count("0")
        if abs(count_1s - count_0s) == 0 or abs(count_1s - count_0s) == 1:
            alter_10 = "".join(["10"] * 501)
            diff1 = int.bit_count(int(s, 2) ^ int(alter_10[: len(s)], 2))
            diff2 = int.bit_count(int(s, 2) ^ int(alter_10[1 : len(s) + 1], 2))
            if diff1 % 2 == 0 and diff2 % 2 == 0:
                return min(diff1 // 2, diff2 // 2)
            return diff1 // 2 if diff1 % 2 == 0 else diff2 // 2
        else:
            return -1
