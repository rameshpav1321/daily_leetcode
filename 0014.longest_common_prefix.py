class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        search_word=strs[0]
        flag=False
        for i in range(len(search_word),0,-1):
            for word in strs:
                if not word.startswith(search_word[:i]):
                    flag=False
                    break
                else:
                    flag=True
            if flag:
                return search_word[:i]
        return ''