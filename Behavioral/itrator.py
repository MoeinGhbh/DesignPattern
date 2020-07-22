class Itration:
    def __init__(self, value):
        self.value = value

    def __next__(self):
        if self.value == 0:
            raise StopIteration('End of sequence ...')
        for i in range(0, self.value):
            value = self.value
            self.value -= 1
            return value


class Itrable:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return Itration(self.value)

I1 = Itrable(9)
I2 = iter(I1)

print(next(I2))
print(next(I2))
print(next(I2))
print(next(I2))
print(next(I2))
print(next(I2))
print(next(I2))
print(next(I2))
print(next(I2))
print(next(I2))
