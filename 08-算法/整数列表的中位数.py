'''
[1,2,3]


2

[1,2,3,4]
(2 + 3) / 2
'''

class Median:
    def __init__(self):
        self.data = []
    def insert(self,num):
        self.data.append(num)
        self.data.sort()
    def getMedian(self):
        length = len(self.data)
        if length % 2 == 1:
            return self.data[length // 2]
        return (self.data[length // 2] + self.data[length // 2 - 1]) / 2.0
median = Median()
median.insert(20)
median.insert(10)
median.insert(30)
median.insert(15)
print(median.getMedian())