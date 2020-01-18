class node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.Next = None
        self.prev = None

class doublylinkedlist:
    def __init__(self):
        self.back = node('dummy','dummy')
        self.front = node('dummy','dummy')
        self.back.Next = self.front
        self.front.prev = self.back

    def addToFront(self,key,val):
        new = node(key,val)
        t = self.front.prev
        self.front.prev = new
        new.Next =self.front
        new.prev = t
        t.Next = new
        return new
    
    def delete(self,node):
        new = node
        p = new.prev
        n = new.Next
        p.Next = n
        n.prev = p
    
    def deleteFromBack(self):
        t = self.back.Next
        u = self.back.Next.Next
        u.prev =self.back
        self.back.Next = u
        return t
    
    
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = doublylinkedlist()
        self.countnodes = 0
        self.inCache = {}
        
        

    def get(self, key: int) -> int:
        if key in self.inCache:
            self.nodes.delete(self.inCache[key])
            n = self.nodes.addToFront(key,self.inCache[key].val)
            self.inCache[key] = n
            return self.inCache[key].val
        return -1
            
        

    def put(self, key: int, value: int) -> None:
        if key in self.inCache:
            self.nodes.delete(self.inCache[key])
            n = self.nodes.addToFront(key,value)
            self.inCache[key] = n
        else:
            n = self.nodes.addToFront(key,value)
            self.inCache[key] = n
            self.countnodes+=1
            if self.countnodes > self.capacity:
                t = self.nodes.deleteFromBack()
                self.countnodes-=1
                del self.inCache[t.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)