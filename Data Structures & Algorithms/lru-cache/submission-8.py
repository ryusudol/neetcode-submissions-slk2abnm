class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.memo = {}

    def get(self, key: int) -> int:
        if key not in self.memo: return -1
        self.memo[key] = self.memo.pop(key)
        return self.memo[key]

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            self.memo.pop(key)
            self.memo[key] = value
        elif len(self.memo) == self.cap:
            del self.memo[next(iter(self.memo))]
        self.memo[key] = value