class MedianFinder:
    '''
    goal: 
    we add elements incrementally and want to return the median values

    heap implementation taken by itself would be O(1)
        but O(m*logn) for addNum(), 
        and, O(m) for findMedian()
    '''

    def __init__(self):
        # initialize the data structures here
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # goal: check for order or size 

        # -1 here because default heap in py is min heap, 
        # so to be able to get the max heap, we multiply with -1 !

        # now need to make sure every num in small <= num in large
        if (self.small and self.large and (-1*self.small[0]) > self.large[0]):
            # if true then take the num from small and push it to large
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # now need to check for uneven size, size diff of 2
        if len(self.small) > len(self.large) + 1:
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1*self.small[0] + self.large[0])/2