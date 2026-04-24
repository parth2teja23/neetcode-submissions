class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        entries = self.hmap[key]
        if not entries:
            return ""
        res = ""
        l = 0
        r = len(entries) - 1
        while l <= r:
            mid = (l + r) // 2

            if entries[mid][1] <= timestamp:
                res = entries[mid][0]
                l = mid + 1
            else:
                r = mid-1

        return res

        
