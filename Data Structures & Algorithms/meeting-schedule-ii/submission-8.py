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
        for i in intervals:
            time.append([i.start, 1])
            time.append([i.end, -1])

        time.sort(key= lambda x: (x[0], x[1]))

        maxCount = 0
        count = 0
        for i in time:
            count += i[1]
            maxCount = max(count, maxCount)
        return maxCount