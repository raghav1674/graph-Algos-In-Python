class MinHeap:

    def __iter__(self):
        return iter(self.arr[:self.size+1])

    def __init__(self, size=10):

        self.cap = size
        self.arr = [float('+inf')]*size
        self.size = -1

    def __str__(self):
        if self.size == -1:
            return "[]"
        return ",".join([str(self.arr[num]) for num in range(self.size+1)])

    def put(self, data):

        if self.size + 1 <= self.cap:
            self.size += 1
            index = self.size
            parent_index = (index - 1)//2
            temp = data

            while index > 0 and temp <= self.arr[parent_index]:

                self.arr[index] = self.arr[parent_index]
                index = parent_index
                parent_index = (index - 1)//2

            self.arr[index] = temp

    def __len__(self):
        return self.size+1

    def get(self):

        if self.size == -1:
            raise Exception("Heap Underflow")
        # number To return
        num = self.arr[0]

        # last element to whom we need to replace
        temp = self.arr[self.size]
        self.arr[self.size] = float("+inf")

        self.size -= 1

        if self.size == -1:
            return num

        index = 0

        left = 2 * index + 1

        right = 2 * index + 2

        if temp <= self.arr[left] and temp <= self.arr[right]:

            self.arr[index] = temp
        else:
            while left <= self.size and right <= self.size:

                if self.arr[left] <= self.arr[right]:

                    self.arr[index] = self.arr[left]

                    index = left
                    left = 2 * index + 1

                else:
                    self.arr[index] = self.arr[right]

                    index = right
                    right = 2 * index + 2

            self.arr[index] = temp
        return num


if __name__ == '__main__':
    mypq = MinHeap()
    mypq.put(-100000)
    mypq.put(-2)
    mypq.put(-100000)
    mypq.put(-100001)

    for i in mypq:
        print(i)
