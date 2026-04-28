class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)  
        self.tail = Node(None, None) 
        self.head.next = self.tail
        self.tail.prev = self.head

    def _delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._delete_node(node)
            self._append(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self._delete_node(node)
        elif len(self.cache) == self.capacity:
            del self.cache[self.head.next.key]
            self._delete_node(self.head.next)
        node = Node(key, value)
        self._append(node)
        self.cache[key] = node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)