class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num=''
        for num in digits:
            str_num+=str(num)
        res_str_num=str(int(str_num)+1)
        res=[int(num) for num in res_str_num]
        return res