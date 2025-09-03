# Runtime 42ms, Beats 76.41%
class MyHashMap:
    # 类变量：所有 MyHashMap 实例共享同一个桶大小
    BUCKET_SIZE = 2069  # 选取一个质数作为桶的大小

    def __init__(self):
        self.buckets = [[] for _ in range(self.BUCKET_SIZE)]

    def _hash(self, key):
        return key % self.BUCKET_SIZE

    def put(self, key: int, value: int) -> None:
        bucket_index = self._hash(key)
        current_bucket = self.buckets[bucket_index]

        for i, (existing_key, existing_value) in enumerate(current_bucket):
            if existing_key == key:
                current_bucket[i] = [key, value]
                return

        current_bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket_index = self._hash(key)
        current_bucket = self.buckets[bucket_index]

        for existing_key, existing_value in current_bucket:
            if existing_key == key:
                return existing_value

        return -1

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        current_bucket = self.buckets[bucket_index]

        for i in range(len(current_bucket)):
            if current_bucket[i][0] == key:
                del current_bucket[i]
                return
