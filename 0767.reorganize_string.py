from queue import PriorityQueue
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        q = PriorityQueue()
        res = ""
        for key, value in Counter(s).items():
            q.put((-value, key))
        while q.empty() == False:
            first_count, first_char = q.get()
            if not len(res) or res[-1] != first_char:
                res += first_char
                if first_count + 1 != 0:
                    q.put((first_count + 1, first_char))
            else:
                if q.empty() == True:
                    return ""
                second_count, second_char = q.get()
                res += second_char
                if second_count + 1 != 0:
                    q.put((second_count + 1, second_char))
                q.put((first_count, first_char))
        return res
