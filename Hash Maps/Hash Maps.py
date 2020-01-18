class node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.Next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [node('dummy','dummy') for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = self.hashf(key)
        cur = self.map[idx]
        while cur.Next:
            if cur.Next.key==key:
                cur.Next.val = value
                return
            
            cur = cur.Next
        
        cur.Next = node(key, value)
        
    
    def hashf(self,key):
        return key % len(self.map)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = self.hashf(key)
        cur = self.map[idx]
        while cur.Next:
            if cur.Next.key==key:
                return cur.Next.val
            
            cur = cur.Next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = self.hashf(key)
        prev = self.map[idx]
        cur = prev.Next
        while cur:
            if cur.key==key:
                prev.Next = cur.Next
                return
            
            prev = cur
            cur = cur.Next
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)