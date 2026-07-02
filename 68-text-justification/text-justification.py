class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        i = 0

        while i < len(words):
            line_len = 0
            current = []

            while (i < len(words)) and (line_len + len(current) + len(words[i]) <= maxWidth):
                current.append(words[i])
                line_len += len(words[i])
                i += 1
            
            spaces_needed = maxWidth - line_len
            gaps = len(current) - 1

            if i == len(words) or gaps == 0:
                line = " ".join(current)
                line += " " * (maxWidth - len(line))
                result.append(line)
            else:
                # Fully justify
                space_each = spaces_needed // gaps
                extra = spaces_needed % gaps

                line = ""

                for j in range(len(current) - 1):
                    line += current[j]
                    line += " " * space_each

                    if extra > 0:
                        line += " "
                        extra -= 1

                line += current[-1]
                result.append(line)

        return result
