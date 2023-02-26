class MyCircularDeque:

    def __init__(self, k: int):
        self.lst = list()
        self.k = k

    def insertFront(self, value: int) -> bool:
        l=self.lst
        if len(l) < self.k:
            l.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        l=self.lst
        if len(l) < self.k:
            l.insert(len(l), value)
            return True
        return False

    def deleteFront(self) -> bool:
        l=self.lst
        if len(l) > 0:
            l.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        l=self.lst
        if len(l) > 0:
            l.pop(-1)
            return True
        return False

    def getFront(self) -> int:
        l=self.lst
        if len(l) > 0:
            return l[0]
        return -1

    def getRear(self) -> int:
        l=self.lst
        if len(l) > 0:
            return l[-1]
        return -1

    def isEmpty(self) -> bool:
        l=self.lst
        if len(l) == 0:
            return True 
        return False

    def isFull(self) -> bool:
        l=self.lst
        if len(l) == self.k:
            return True 
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()