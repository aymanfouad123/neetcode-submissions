class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # approach - topological sort using bfs (kahn) 
        wordMap = {}
        indegree = {}

        for word in words:
            for letter in word:
                wordMap[letter] = set()
                indegree[letter] = 0

        for n in range(len(words) - 1):
            word1 = words[n]
            word2 = words[n + 1]
            minLen = min(len(word1), len(word2))

            # a longer word cannot come before its exact prefix
            # i.e, "abc" before "ab" is invalid
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            # now we need to track the alien order
            for x in range(minLen):
                if word1[x] != word2[x]:
                    before = word1[x]
                    after = word2[x]
                    
                    # avoid updating indegree because of duplicates
                    if after not in wordMap[before]:    
                        # bfs topo order: prereq -> item     
                        wordMap[before].add(after)
                        indegree[after] += 1

                    break   # first mismatch tells us the alien order

        # graph logic - bfs kahn 
        q = deque()
        result = []
        # letters with nothing req before them.
        for letter in indegree:
            if indegree[letter] == 0:
                q.append(letter)

        while q:
            char = q.popleft()
            result.append(char)

            for neighbor in wordMap[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(result) != len(wordMap):
            # cycle prevented us from processing every letter
            return ""   

        return "".join(result)

            


                