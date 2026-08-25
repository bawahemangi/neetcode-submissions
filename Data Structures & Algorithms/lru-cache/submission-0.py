class Node:
    def __init__ (self,key,val):
        self.key,self.val=key,val
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.right=Node(0,0)
        self.left=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def insert(self,node):
        prev=self.right.prev
        prev.next=node
        node.prev=prev

        node.next=self.right
        self.right.prev=node

        self.right.prev=node
        node.next=self.right

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)

            del self.cache[lru.key]
        
