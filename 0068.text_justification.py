class Solution:
    def build_line(self, line, max_width, last_line):
        remaining_width, word_count = max_width - len(" ".join(line)), len(line)
        if word_count == 1 or last_line:
            return " ".join(line) + " " * remaining_width
        else:
            space = remaining_width // (word_count - 1)
            extra_space = remaining_width % (word_count - 1)
            for i in range(extra_space):
                line[i] += " "
            for i in range(word_count - 1):
                line[i] += " " * space
            return " ".join(line)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        allowed_width, temp, lines = maxWidth, [], []
        for word in words:
            if len(word) <= allowed_width:
                temp.append(word)
                allowed_width -= len(word) + 1
            else:
                lines.append(temp)
                temp, allowed_width = [word], maxWidth - len(word) - 1
        lines.append(temp)
        res, curr_words, last_line = [], 0, False
        for line in lines:
            curr_words += len(line)
            if curr_words == len(words):
                last_line = True
            res.append(self.build_line(line, maxWidth, last_line))
        return res
