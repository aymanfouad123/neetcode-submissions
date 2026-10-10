class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        initial idea: hashmaps

        we could keep track of the k values using a heap
        O(nlogk)
        
        we can also compute the k top indexes during the first run
        -> done through bucket sort
        this gives us O(n) time
        """

        # Solution using bucket sort - O(n) time
        
        freq = [[] for i in range(len(nums) + 1)]
        # why +1? because all elements can be the same, hence the freq for that element will be == len(nums)
        count = {}
        for ele in nums:
            count[ele] = 1 + count.get(ele, 0)
        # now we have each element and their freq's 

        # now bucket sort table logic 
        for ele, val in count.items():
            freq[val].append(ele)
        
        """
        now we have a freq table that looks like - 
        freq = [[], [3], [2], [1], [], [], []]
        
        we now need to traverse from the end to remove the top k elements
        """

        result = []      
        for i in range(len(freq)-1, 0, -1):            
            # now count frequency can have multiple values i.e, for count 3 we could have freq[3] = [2,3]
            for val in freq[i]:
                result.append(val)
                if len(result) == k:
                    return result

        """
        # Solution using heap - 
        heap = []

        count = {}  # keeping track of elements and their freq

        for ele in nums:
            count[ele] = 1 + count.get(ele, 0)  # use this syntax since you cant += to a record that doesnt exist
        
        # now we can go through the dict and generate the min heap
        for num in count.keys(): 
            heapq.heappush(heap, (count[num], num))
            #                    frequency, number
            # since python can pop min freq because, (1, 3) < (2, 2) < (3, 1)

            if len(heap) > k:
                heapq.heappop(heap)     # this way we maintain a k heap and push out any smaller element
        
        '''
        # now we have a top k heap, we need to return the top k values

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

        here we dont need to use heap 
        and can do a direct heap[1] call such as 
        a direct return would look like 
        -> return [pair[1] for pair in heap]

        that will be better! 
        since the return above would be O(k) time complexity
        whereas using heappop we get O(klogk) **

        Heap operations complexity table :-
        peek smallest	            heap[0]	                        O(1)
        insert	                    heapq.heappush(heap, item)	    O(log h)
        remove smallest	            heapq.heappop(heap)	            O(log h)
        turn a list into a heap	    heapq.heapify(items)	        O(h)
        '''

        return [pair[1] for pair in heap]
            
        """