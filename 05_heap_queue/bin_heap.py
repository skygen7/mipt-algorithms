class BinHeap:
    def __init__(self, heap: list):
        self.heap = heap
        self.size = len(heap) - 1

        self.balance()

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)

        if left <= self.size and self.heap[left] > self.heap[i]:
            largest = left
        else:
            largest = i

        if right <= self.size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]

            self.heapify(largest)

    def get_heap(self):
        return self.heap

    def balance(self):
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)

    def push(self, i):
        self.heap.append(i)
        self.size += 1
        self.balance()

    def pop(self, i):
        self.heap.remove(i)
        self.size -= 1

        self.balance()


hp = BinHeap([0, 0, 9, 5, 23, 0, 0, 2, 2, 1, 4, 0, 12, -1, 0])
print(f"Init binary heap: {hp.get_heap()}")

push_el = 7
hp.push(push_el)
print(f"Push element '{push_el}'.\nNew heap: {hp.get_heap()}")

pop_el = 4
hp.pop(4)
print(f"Pop element: {pop_el}.\nNew heap: {hp.get_heap()}")
