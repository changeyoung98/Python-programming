# Flie: queue.py
# Class queue
# By: Daisy
class queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return (self.items==[])
    def getLen(self):
        return (len(self.items))
