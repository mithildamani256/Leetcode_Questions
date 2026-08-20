class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        visit = set()
        wordList = set(wordList)

        def bfs(word):
            q = deque()

            visit.add(word)
            q.append((word, 1))

            while q:
                current, steps = q.popleft()

                if current == endWord:
                    return steps

                for i in range(len(current)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new_word = current[:i] + ch + current[i+1:]

                        if new_word in wordList and new_word not in visit:
                            visit.add(new_word)
                            q.append((new_word, steps + 1))
            
            return 0

        return bfs(beginWord)





