"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []

        for interval in intervals:
            time.append([interval.start, 1])
            time.append([interval.end, -1])
        
        time.sort(key= lambda x: (x[0], x[1]))
        count = 0
        maxCount = 0
        for t in time:
            count += t[1]
            maxCount = max(count, maxCount)
        return maxCount