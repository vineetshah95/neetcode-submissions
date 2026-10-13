class MedianFinder:

    def __init__(self):
        self.res = []
        self.re1 = []

    def addNum(self, num: int) -> None:
        self.res.append(num)
        m,n = 0,0

    def findMedian(self) -> float:
        # k = len(self.res)
        self.res.sort()
        total = 0
        if len(self.res) % 2 == 0:
            print(self.res)
            length = len(self.res)
            m = self.res[length//2 - 1]
            n = self.res[length//2]
            return (m + n) / 2
        else:
            return self.res[len(self.res)//2]

        