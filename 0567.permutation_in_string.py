class Solution:
    def check_chunk(self, my_dict, chunk):
        for char in chunk:
            if char not in my_dict:
                return False
            my_dict[char] -= 1
            if my_dict[char] == 0:
                del my_dict[char]
        return True if len(my_dict) == 0 else False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        my_dict = {}
        for char in s1:
            my_dict[char] = 1 + my_dict.get(char, 0)
        for i in range(s2_len - s1_len + 1):
            temp = copy.deepcopy(my_dict)
            if self.check_chunk(temp, s2[i : i + s1_len]):
                return True
        return False
