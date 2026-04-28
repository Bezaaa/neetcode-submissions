import bisect 

class TimeMap:
    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))  # Store timestamp first to make binary search easier

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        time_value_list = self.timemap[key]
        
        # Extract timestamps to binary search
        timestamps = [t for t, _ in time_value_list]
        
        # Find rightmost timestamp <= given timestamp
        idx = bisect.bisect_right(timestamps, timestamp) - 1
        
        if idx >= 0:
            return time_value_list[idx][1]  # return value
        return ""
