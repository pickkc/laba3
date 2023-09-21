class PriorityQueueNode:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item, priority):
        new_node = PriorityQueueNode(item, priority)
        if self.head is None or priority >self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and priority <= current.next.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if not self.is_empty():
            item = self.head.item
            self.head = self.head.next
            return item

pq = PriorityQueue()
while(True):
    task = input("введите задачу: ")
    if task == ".":
        break
    else:
        priority = int(input("введите приоритет задачи: "))
        pq.enqueue(task, priority)

while not pq.is_empty():
    item = pq.dequeue()
    print("Выполняется:", item)



