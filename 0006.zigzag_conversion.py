class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        reverse = True
        res = [""] * numRows
        row_ind = 0
        for char in s:
            res[row_ind] += char
            if row_ind == 0 or row_ind == numRows - 1:
                reverse = not reverse
            if reverse:
                row_ind -= 1
            else:
                row_ind += 1
        return "".join(res)
