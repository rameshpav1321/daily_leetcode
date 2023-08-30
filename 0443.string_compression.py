class Solution:
    def compress(self, chars: List[str]) -> int:
        i, index = 0, 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            chars[index] = chars[i]
            index += 1
            if j - i > 1:
                count_str = str(j - i)
                for c in count_str:
                    chars[index] = c
                    index += 1
            i = j
        return index
