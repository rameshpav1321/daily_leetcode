class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        char_grp = {}
        char_map = {chr(97 + i): -1 for i in range(26)}
        ind = 0
        for i in range(len(s1)):
            if char_map[s1[i]] == -1 and char_map[s2[i]] == -1:
                char_map[s1[i]] = char_map[s2[i]] = ind
                char_grp[ind] = [s1[i], s2[i]]
                ind += 1
            elif char_map[s1[i]] == -1:
                char_map[s1[i]] = char_map[s2[i]]
                char_grp[char_map[s2[i]]].append(s1[i])
            elif char_map[s2[i]] == -1:
                char_map[s2[i]] = char_map[s1[i]]
                char_grp[char_map[s1[i]]].append(s2[i])
            elif char_map[s1[i]] != char_map[s2[i]]:
                for c in char_grp[char_map[s2[i]]]:
                    char_map[c] = char_map[s1[i]]
                    char_grp[char_map[s1[i]]].append(c)
        res = ""
        for char in baseStr:
            if char_map[char] == -1:
                res += char
            else:
                res += sorted(char_grp[char_map[char]])[0]
        return res
