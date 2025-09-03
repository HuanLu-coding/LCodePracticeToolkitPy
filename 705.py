# class MyHashSet:
#     def __init__(self):
#         self.size = 1000001  # 覆盖 0 到 10^6
#         self.buckets = [False] * self.size
#
#     def add(self, key: int) -> None:
#         self.buckets[key] = True
#
#     def remove(self, key: int) -> None:
#         self.buckets[key] = False
#
#     def contains(self, key: int) -> bool:
#         return self.buckets[key]
#
# Runtime: 12ms, Beats 97.20%
class MyHashSet:
    def __init__(self):
        self._size = int(1e3) // 2
        self.hashed = [[] for _ in range(self._size)]

    def _hash(self, key: int) -> int:
        return key % self._size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if not key in self.hashed[idx]:
            self.hashed[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.hashed[idx]:
            self.hashed[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.hashed[idx]
