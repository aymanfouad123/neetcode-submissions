class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        wordMap = {}
        for word in words:
            for letter in word:
                wordMap[letter] = set()

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
                    wordMap[word2[x]].add(word1[x])     
                    # word2 letter must come before word1
                    break   # first mismatch tells us the alien order

        # now to build graph
        visiting = set()    # detecting cycles
        completed = set()
        result = [] 

        def dfs(char):
            if char in visiting: return False
            if char in completed: return True   # processed letter

            visiting.add(char)

            for neigh in wordMap[char]:
                if not dfs(neigh): return False
            
            visiting.remove(char)
            completed.add(char)
            result.append(char)
            return True
        
        # traverse through wordMap and return order of the graph
        for letter in wordMap:
            if not dfs(letter): return ""

        return "".join(result)

            


                