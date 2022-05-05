import heapq


class TaskQueue:
    def __init__(self):
        self.queue = []

    def push(self, priority, obj):

        heapq.heappush(self.queue, (-priority, obj))

    def pop(self):
        return heapq.heappop(self.queue)[-1]

    def get_queue(self):
        return [heapq.heappop(self.queue) for _ in range(len(self.queue))]


q = TaskQueue()
q.push(4, 'a')
q.push(2, 'b')
q.push(3, 'd')
q.push(1, 'c')

print(q.get_queue())


