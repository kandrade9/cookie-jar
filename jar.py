class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "\U0001F36A"

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
print(jar.capacity)
jar.deposit(12)
print(jar)
jar.withdraw(3)
print(jar)
