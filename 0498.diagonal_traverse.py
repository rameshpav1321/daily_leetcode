class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        my_dict = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                my_dict[i + j].append(mat[i][j])
        res = []
        for key, value in my_dict.items():
            if key % 2 == 0:
                res.extend(value[::-1])
            else:
                res.extend(value)
        return res
