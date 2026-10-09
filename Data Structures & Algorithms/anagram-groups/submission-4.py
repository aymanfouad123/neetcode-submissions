class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        initial ideas: 
        hashmap + sort? 

        goal: m*n time, m number of elements and n longest string  
        avoiding sort since its logn time, we can compute ascii values instead
        '''

        ref = defaultdict(list)
        for ele in strs:
            '''
            with ascii values make sure to not rely on the overall sum of the words!
            since different words can have the same sum - 
            "ad" = 97 + 100 = 197 and "bc" = 98 + 99  = 197
            '''
            count = [0] * 26    # hence this approach preserves the letter ordering and also accounts for repeated letters

            for c in ele:
                count[ord(c) - ord('a')] += 1   # keeping track of letter occurences
            
            ref[tuple(count)].append(ele)

        return list(ref.values())