from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        # Extract timestamps and sort them
        timestamps = [t[1] for t in self.hashmap[key]]
        sorted_times = sorted(timestamps)

        # Find the largest timestamp <= requested timestamp
        prevTime = None
        for t in sorted_times:
            if t <= timestamp:
                prevTime = t
            else:
                break

        # If no timestamp is <= requested timestamp, return ""
        if prevTime is None:
            return ""

        # Find the value corresponding to prevTime
        for value, t in self.hashmap[key]:
            if t == prevTime:
                return value