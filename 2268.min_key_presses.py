class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c = collections.Counter(s)
        sorted_c = sorted(c.values(), reverse=True)
        res, key_press = 0, 0
        for i in range(len(sorted_c)):
            if i % 9 == 0:
                key_press += 1
            res += key_press * sorted_c[i]
        return res
