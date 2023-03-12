class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.curr_capacity=0
        self.map={}
        
    def get(self, key: int) -> int:
        if key in self.map:
            val=self.map[key]
            del self.map[key]
            self.map[key]=val
            return val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            del self.map[key]
            self.map[key]=value
        else:
            if self.curr_capacity<self.capacity:
                self.map[key]=value
                self.curr_capacity+=1
            else:
                del self.map[list(self.map)[0]]
                self.map[key]=value